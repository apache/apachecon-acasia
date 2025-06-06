import os
import pandas as pd

print("开始执行脚本...")
# 从Excel文件读取会议session数据
sessions = pd.read_excel('ApacheConSessions.xlsx')
print(f"Excel文件读取完成，共有{len(sessions)}行数据")

# 确保目标目录存在
output_dir = "content/sessions"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"创建目录: {output_dir}")

# 定义track(轨道/分类)的映射字典，将中文/英文分类名映射为URL友好的格式
tracks_dictionary = {"Cloud Native": "cloudnative",
                     "DataOpts": "dataopts",
                     "Streaming": "streaming",
                     "Incubator": "incubator",
                     "Data Lake & Data Warehouse": "datalake",
                     "OLAP & Data Analysis": "olap",
                     "Community": "community",
                     "Data Storage & Computing": "datastorage",
                     "Web Application & Framework": "webapplication",
                     "AI": "ai",
                     "IoT": "iot",
                     "Message": "message",
                     "Microservice": "microservice",
                     "Observability": "observability",
                     "Rust": "rust",
                     "General": "general",
                     "Keynote": "keynote",
                     "5-mins-Lightning-Talk": "5minslightningtalk",
                     }
# 定义session类型的英文映射字典
session_types_dictionary = {"Chinese": "Chinese Session",
                            "English": "English Session"}
# 定义session类型的中文映射字典
session_types_chinese_dictionary = {"中文演讲": "中文演讲",
                                    "Regular Session": "英文演讲"}

# 移除演讲者信息中的email地址(如果有)
def remove_speakers_email(speakers):
    if pd.isnull(speakers):
        return ""
    speaker_list = speakers.split(",") # 将多个演讲者按逗号分隔
    result_list = []
    for speaker in speaker_list:
        result_list.append(remove_speaker_email(speaker)) # 对每个演讲者移除email
    return ', '.join(result_list) # 重新组合为字符串

# 移除单个演讲者的email地址(格式通常为"姓名 <email>")
# 取<符号前的部分并去除空格
def remove_speaker_email(speaker):
    parts = speaker.split('<')
    if len(parts) > 1:
        return parts[0].strip()
    return speaker.strip()

# 遍历所有session数据
for index in sessions.index:
    # 只处理状态为"Accepted"的被接受的session
    if sessions.at[index, 'Status'] == 'Accepted':
        # create the markdown file
        
        # 获取track值
        track_value = tracks_dictionary.get(sessions.at[index, 'Track'], "unknown")
        session_id = str(sessions.at[index, 'Session Id'])
        
        # 生成文件名: Track-Session Id
        file_name = f"{track_value}-{session_id}"
        
        # 创建英文和中文的markdown文件路径
        en_file_path = os.path.join(output_dir, file_name + ".md")
        zh_file_path = os.path.join(output_dir, file_name + ".zh.md")
        
        
        # 创建英文和中文的markdown文件
        markdown_en_file = open(en_file_path, "w+", encoding="utf-8")
        markdown_zh_file = open(zh_file_path, "w+", encoding="utf-8")
        
        # markdown文件的元数据模板
        mate_data = '---\ntitle: "{}"\ndate: "{}" \ntrack: "{}"\npresenters: "{}"\nstype: "{}"\n---\n'
        schedule_time = ""
        if not pd.isnull(sessions.at[index, 'Date Submitted']):
            schedule_time = sessions.at[index, 'Date Submitted']
        # 获取英文标题
        title = sessions.at[index, 'Title']

        # map the session type
        session_type = session_types_dictionary.get(sessions.at[index, 'Language'])

        # update the track information
        # 映射track分类到URL友好格式
        track = track_value
        # 处理演讲者信息(移除email)
        speakers = remove_speakers_email(sessions.at[index, 'Owner'])
        # 获取英文摘要和演讲者简介
        abstract = sessions.at[index, "Description"] if not pd.isnull(sessions.at[index, "Description"]) else ""
        speaker_bios = sessions.at[index, "Bio"] if not pd.isnull(sessions.at[index, "Bio"]) else ""
        
        speaker_image = ""
        if not pd.isnull(sessions.at[index, 'Profile Picture']):
            speaker_image = sessions.at[index, 'Profile Picture']
            head_img_html = f'<img src="images/speaker/{speaker_image}" width="200" />'
        else:
            head_img_html = '' 
        
        # 写入英文markdown文件
        markdown_en_file.write(mate_data.format(title,
                                               schedule_time,
                                               track,
                                               speakers,
                                               session_type))
        markdown_en_file.write(abstract)
        markdown_en_file.write("\n ### Speakers: \n ")
        if head_img_html:
            markdown_en_file.write(head_img_html + "\n\n")
        markdown_en_file.write(speaker_bios)
        markdown_en_file.close()
        
        # 处理中文内容(如果存在)
        if not pd.isnull(sessions.at[index, 'Chinese Title']):
            title = sessions.at[index, 'Chinese Title']
        if not pd.isnull(sessions.at[index, "Chinese Abstract"]):
            abstract = sessions.at[index, "Chinese Abstract"]
        if not pd.isnull(sessions.at[index, "Chinese Bios"]):
            speaker_bios = sessions.at[index, "Chinese Bios"]

        # map the session type
        session_zh_type = session_types_chinese_dictionary.get(sessions.at[index, 'Language'])

        markdown_zh_file.write(mate_data.format(title,
                                               schedule_time,
                                               track,
                                               speakers,
                                               session_zh_type))
        markdown_zh_file.write(abstract)
        markdown_zh_file.write("\n ### 讲师: \n ")
        if head_img_html:
            markdown_zh_file.write(head_img_html + "\n\n")
        markdown_zh_file.write(speaker_bios)
        markdown_zh_file.close()
