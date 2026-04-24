#!/usr/bin/env python3
"""
读取目录下所有议题文件，使用硅基流动 Embedding API 生成向量，
每处理完一个文件立即存入 pgvector（表每次重建），
最后计算每个议题最相似的 5 个其他议题（相同 stype），
并将结果写回文件的 related_sessions 字段。
"""

import os
import sys
import time
import re
import argparse
import yaml
import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()

SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")
EMBEDDING_URL = "https://api.siliconflow.cn/v1/embeddings"
EMBEDDING_MODEL = "BAAI/bge-m3"
EMBEDDING_DIM = 1024

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

if not SILICONFLOW_API_KEY:
    print("错误: 未设置环境变量 SILICONFLOW_API_KEY", file=sys.stderr)
    sys.exit(1)

missing_db = [k for k, v in DB_CONFIG.items() if v is None and k != "port"]
if missing_db:
    print(f"错误: 未设置以下数据库环境变量: {missing_db}", file=sys.stderr)
    sys.exit(1)


def get_embedding(text: str, retries=3, delay=60) -> list:
    """调用硅基流动 API 获取文本 embedding，遇到 429 自动重试"""
    payload = {"model": EMBEDDING_MODEL, "input": text}
    headers = {
        "Authorization": f"Bearer {SILICONFLOW_API_KEY}",
        "Content-Type": "application/json",
    }
    for attempt in range(retries + 1):
        try:
            resp = requests.post(EMBEDDING_URL, json=payload, headers=headers, timeout=30)
            if resp.status_code == 429:
                print(f"触发限流 (429)，等待 {delay} 秒后重试... (尝试 {attempt+1}/{retries})")
                time.sleep(delay)
                continue
            resp.raise_for_status()
            data = resp.json()
            return data["data"][0]["embedding"]
        except requests.exceptions.RequestException as e:
            if attempt == retries:
                raise RuntimeError(f"获取 embedding 失败: {e}") from e
            print(f"请求失败: {e}，{delay} 秒后重试...")
            time.sleep(delay)


def parse_session_file(filepath: str) -> tuple:
    """解析文件，返回 (frontmatter_dict, body_text)"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter_pattern = r"^---\n(.*?)\n---\n(.*)$"
    match = re.search(frontmatter_pattern, content, re.DOTALL)
    if not match:
        raise ValueError(f"文件 {filepath} 格式不正确，缺少 frontmatter")

    yaml_text = match.group(1)
    body = match.group(2).strip()
    frontmatter = yaml.safe_load(yaml_text)
    if not frontmatter:
        frontmatter = {}
    return frontmatter, body


def write_session_file(filepath: str, frontmatter: dict, body: str):
    """将修改后的 frontmatter 和正文写回文件"""
    yaml_str = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    yaml_str = yaml_str.rstrip()
    output = f"---\n{yaml_str}\n---\n{body}"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output)


def init_db(conn):
    """删除旧表并重新创建 sessions 表，使用自增 id 主键"""
    with conn.cursor() as cur:
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        cur.execute("DROP TABLE IF EXISTS sessions;")
        cur.execute(f"""
            CREATE TABLE sessions (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                stype TEXT NOT NULL,
                title TEXT,
                content TEXT,
                embedding vector({EMBEDDING_DIM})
            );
        """)
        conn.commit()
        print("数据库表已重建（旧数据已清空）")


def store_single_embedding(conn, filename: str, stype: str, title: str, content: str, embedding: list) -> int:
    """插入单条记录到数据库，返回生成的 id"""
    with conn.cursor() as cur:
        sql = """
            INSERT INTO sessions (filename, stype, title, content, embedding)
            VALUES (%s, %s, %s, %s, %s::vector)
            RETURNING id
        """
        emb_str = "[" + ",".join(map(str, embedding)) + "]"
        cur.execute(sql, (filename, stype, title, content, emb_str))
        row = cur.fetchone()
        conn.commit()
        record_id = row[0]
        print(f"  已存入数据库 (id={record_id}): {title} ({stype})")
        return record_id


def get_similar_titles(conn, current_id: int, stype: str, embedding: list, top_k=5) -> list:
    """返回与给定议题最相似的其他标题列表（相同 stype，排除自身）"""
    emb_str = "[" + ",".join(map(str, embedding)) + "]"
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT title FROM sessions
            WHERE stype = %s AND id != %s
            ORDER BY embedding <=> %s::vector
            LIMIT %s
            """,
            (stype, current_id, emb_str, top_k),
        )
        return [row[0] for row in cur.fetchall()]


def main():
    parser = argparse.ArgumentParser(description="生成议题向量并计算相似推荐")
    parser.add_argument("--input-dir", required=True, help="存放议题文件的目录")
    args = parser.parse_args()

    input_dir = os.path.abspath(args.input_dir)
    if not os.path.isdir(input_dir):
        print(f"错误: 目录不存在 {input_dir}", file=sys.stderr)
        sys.exit(1)

    files = []
    for fname in os.listdir(input_dir):
        fpath = os.path.join(input_dir, fname)
        if os.path.isfile(fpath):
            files.append(fpath)

    if not files:
        print(f"目录 {input_dir} 中没有文件", file=sys.stderr)
        sys.exit(1)

    print(f"找到 {len(files)} 个文件")

    conn = psycopg2.connect(**DB_CONFIG)
    try:
        # 每次运行都删除并重建表
        init_db(conn)

        # 存储每个文件的 id 映射，供第二阶段使用
        file_id_map = {}  # key: (filename, stype) -> id

        # 第一阶段：逐文件解析、生成 embedding、立即存入数据库，并记录 id
        for idx, fpath in enumerate(files, 1):
            print(f"\n[{idx}/{len(files)}] 处理文件: {os.path.basename(fpath)}")
            try:
                frontmatter, body = parse_session_file(fpath)
                title = frontmatter.get("title")
                stype = frontmatter.get("stype", "")
                if not title:
                    print(f"  跳过：文件中没有 title 字段")
                    continue
                if not stype:
                    print(f"  警告：文件中没有 stype 字段，将使用空字符串")
                filename = os.path.abspath(fpath)
                text_for_embed = f"{title}\n{body}"
                embedding = get_embedding(text_for_embed)
                record_id = store_single_embedding(conn, filename, stype, title, body, embedding)
                file_id_map[(filename, stype)] = record_id
                print(f"  生成并存储 embedding 成功，维度 {len(embedding)}")
            except Exception as e:
                print(f"  处理失败: {e}，跳过该文件")
                continue

        # 第二阶段：再次遍历文件，计算相似推荐并写回文件
        print("\n" + "="*50)
        print("开始计算相似推荐并回填 related_sessions...")
        for idx, fpath in enumerate(files, 1):
            print(f"\n[{idx}/{len(files)}] 处理文件: {os.path.basename(fpath)}")
            try:
                frontmatter, body = parse_session_file(fpath)
                title = frontmatter.get("title")
                stype = frontmatter.get("stype", "")
                if not title:
                    continue
                filename = os.path.abspath(fpath)
                key = (filename, stype)
                if key not in file_id_map:
                    print(f"  未找到该文件的记录 id，跳过")
                    continue
                record_id = file_id_map[key]
                # 从数据库获取该记录的 embedding（也可以直接从第一阶段缓存，但为了安全重新查询）
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT embedding FROM sessions WHERE id = %s",
                        (record_id,)
                    )
                    row = cur.fetchone()
                    if not row:
                        print(f"  数据库中没有找到 id={record_id}，跳过")
                        continue
                    embedding = row[0]
                    if isinstance(embedding, str):
                        import ast
                        embedding = ast.literal_eval(embedding)
                similar = get_similar_titles(conn, record_id, stype, embedding, top_k=5)
                frontmatter["related_sessions"] = similar
                write_session_file(fpath, frontmatter, body)
                print(f"  写入 related_sessions: {similar}")
            except Exception as e:
                print(f"  处理失败: {e}")
                continue

    finally:
        conn.close()

    print("\n全部完成！")


if __name__ == "__main__":
    main()