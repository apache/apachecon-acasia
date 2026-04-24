#!/usr/bin/env python3
"""
批量增强 Session Markdown 文件 - DeepSeek 版本
- 通过 DeepSeek API 提取 depth, practice_level, projects, audience
- 更新 front matter，确保数组字段换行显示
- related_sessions 字段自动补齐
"""

import os
import sys
import json
import time
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any

import yaml
from openai import OpenAI
import frontmatter
from tqdm import tqdm

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ========== 自定义 YAML 序列化：强制列表换行 ==========
def represent_list(dumper, data):
    """强制列表使用块序列格式（flow_style=False）"""
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=False)

yaml.add_representer(list, represent_list, Dumper=yaml.SafeDumper)

# ========== 字段取值说明 ==========
DEPTH_OPTIONS = ["beginner", "intermediate", "advanced"]
AUDIENCE_OPTIONS = ["架构师", "开发者", "SRE/运维", "产品/经理", "通用"]
PROJECT_EXAMPLES = ["skywalking", "kafka", "flink", "spark", "camel", "dubbo", "rocketmq", "pulsar", "calcite", "hadoop", "hive"]


def build_prompt(title: str, abstract: str) -> str:
    """构造发给大模型的提示词"""
    return f"""你是一个技术会议议题分析助手。请根据以下议题的标题和摘要，提取结构化信息。

标题：{title}
摘要：{abstract}

请返回一个 JSON 对象，包含以下字段：
- depth: 技术深度，必须是 "beginner"（初级）、"intermediate"（进阶）或 "advanced"（深度）之一。
- practice_level: 实战性评分，1-5 的整数，5 表示实战性最强（含案例、演示、实操等）。
- projects: 涉及的 Apache 项目或知名开源项目列表（数组），例如 {", ".join(PROJECT_EXAMPLES[:8])} 等。如果未涉及，返回空数组。
- audience: 目标听众角色列表（数组），可从 {AUDIENCE_OPTIONS} 中选择，可多选。

只返回有效的 JSON，不要包含任何额外说明或 Markdown 标记。"""


def call_deepseek(prompt: str, model: str = "deepseek-chat", api_key: Optional[str] = None, base_url: str = "https://api.deepseek.com") -> Dict[str, Any]:
    """调用 DeepSeek API"""
    key = api_key or os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        raise ValueError("请设置 DEEPSEEK_API_KEY 环境变量或传入 api_key 参数")

    client = OpenAI(api_key=key, base_url=base_url)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是一个精确的 JSON 输出助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=500,
            )
            content = response.choices[0].message.content.strip()
            # 清理可能的 Markdown 代码块
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
            result = json.loads(content)
            return result
        except json.JSONDecodeError as e:
            logger.warning(f"JSON 解析失败 (尝试 {attempt+1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
        except Exception as e:
            logger.error(f"API 调用失败: {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(5)


def validate_and_clean(result: Dict[str, Any]) -> Dict[str, Any]:
    """验证并清理大模型返回的字段"""
    cleaned = {}
    
    # depth
    depth = result.get("depth", "").lower()
    if depth in DEPTH_OPTIONS:
        cleaned["depth"] = depth
    else:
        logger.warning(f"无效 depth '{depth}'，设为默认 'general'")
        cleaned["depth"] = "general"
    
    # practice_level
    try:
        level = int(result.get("practice_level", 3))
        cleaned["practice_level"] = max(1, min(5, level))
    except (ValueError, TypeError):
        cleaned["practice_level"] = 3
    
    # projects
    projects = result.get("projects", [])
    if isinstance(projects, list):
        cleaned["projects"] = [str(p).lower() for p in projects if p]
    else:
        cleaned["projects"] = []
    
    # audience
    audience = result.get("audience", [])
    if isinstance(audience, list):
        valid_aud = [a for a in audience if a in AUDIENCE_OPTIONS]
        cleaned["audience"] = valid_aud if valid_aud else ["通用"]
    else:
        cleaned["audience"] = ["通用"]
    
    return cleaned


def process_file(file_path: Path, args) -> bool:
    """处理单个 Markdown 文件，返回是否成功"""
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # 检查是否需要处理（所需字段是否都已存在）
        required_fields = ["depth", "practice_level", "projects", "audience", "related_sessions"]
        if not args.force and all(k in post.metadata for k in required_fields):
            logger.debug(f"跳过已处理文件: {file_path}")
            return True
        
        title = post.metadata.get("title", "")
        abstract = post.content.strip() if post.content else ""
        
        if not title:
            logger.warning(f"文件缺少 title: {file_path}")
            return False
        
        abstract_short = abstract[:1000] if len(abstract) > 1000 else abstract
        
        logger.info(f"处理: {file_path.name} - {title}")
        prompt = build_prompt(title, abstract_short)
        
        result = call_deepseek(
            prompt, 
            model=args.model, 
            api_key=args.api_key, 
            base_url=args.base_url
        )
        
        cleaned = validate_and_clean(result)
        
        # 更新 front matter
        post.metadata["depth"] = cleaned["depth"]
        post.metadata["practice_level"] = cleaned["practice_level"]
        post.metadata["projects"] = cleaned["projects"]
        post.metadata["audience"] = cleaned["audience"]
        
        # 确保 related_sessions 字段存在（目前为空数组）
        if "related_sessions" not in post.metadata:
            post.metadata["related_sessions"] = []
        
        # 使用自定义 YAML 序列化，保证数组换行
        yaml_str = yaml.safe_dump(dict(post.metadata), allow_unicode=True, sort_keys=False)
        file_content = f"---\n{yaml_str}---\n{post.content}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        return True
        
    except Exception as e:
        logger.error(f"处理文件失败 {file_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="增强 Session Markdown 文件 (DeepSeek)")
    parser.add_argument("directory", type=str, help="包含 session 文件的目录路径")
    parser.add_argument("--model", type=str, default="deepseek-chat", help="DeepSeek 模型名称")
    parser.add_argument("--api-key", type=str, help="DeepSeek API Key (也可通过 DEEPSEEK_API_KEY 环境变量设置)")
    parser.add_argument("--base-url", type=str, default="https://api.deepseek.com", help="API Base URL")
    parser.add_argument("--force", action="store_true", help="强制覆盖已有字段")
    parser.add_argument("--dry-run", action="store_true", help="仅预览不实际写入文件")
    parser.add_argument("--delay", type=float, default=1.0, help="每次 API 调用间隔秒数")
    parser.add_argument("--extensions", nargs="+", default=[".md"], help="要处理的文件扩展名")
    
    args = parser.parse_args()
    
    root_dir = Path(args.directory)
    if not root_dir.exists():
        logger.error(f"目录不存在: {root_dir}")
        sys.exit(1)
    
    all_files = []
    for ext in args.extensions:
        all_files.extend(root_dir.rglob(f"*{ext}"))
    all_files = list(set([f for f in all_files if f.is_file()]))
    
    if not all_files:
        logger.warning("未找到任何匹配的文件")
        return
    
    logger.info(f"找到 {len(all_files)} 个文件待处理")
    
    if args.dry_run:
        logger.info("=== 预览模式 ===")
        for f in all_files:
            print(f"  {f}")
        return
    
    success_count = 0
    for file_path in tqdm(all_files, desc="处理进度"):
        if process_file(file_path, args):
            success_count += 1
        time.sleep(args.delay)
    
    logger.info(f"处理完成: 成功 {success_count}/{len(all_files)}")


if __name__ == "__main__":
    main()