## ---------------------------------------------------------------------------
## Licensed to the Apache Software Foundation (ASF) under one or more
## contributor license agreements.  See the NOTICE file distributed with
## this work for additional information regarding copyright ownership.
## The ASF licenses this file to You under the Apache License, Version 2.0
## (the "License"); you may not use this file except in compliance with
## the License.  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------------------------
import numpy
import pandas as pd
from youdao_translator_api import translator


sessions = pd.read_excel('ApacheConSessions.xlsx')
tracks_dictionary = {
    "Integration | 集成": "integration",
    "Integration": "integration",
    "Workflow/DataProcessing | 工作流/数据处理": "workflowdatagovernance",
    "Workflow/DataProcessing": "workflowdatagovernance",
    "Web Server/Tomcat | Web服务": "webserverandtomcat",
    "Web Server/Tomcat": "webserverandtomcat",
    "Streaming | 数据流": "streaming",
    "Streaming": "streaming",
    "Observability | 可观测性": "observability",
    "Observability": "observability",
    "Middleware | 中间件": "middleware",
    "Middleware": "middleware",
    "Messaging (Pulsar/Kafka/RocketMQ/ActiveMQ etc. ) | 消息": "messaging",
    "Messaging (Pulsar/Kafka/RocketMQ/ActiveMQ etc. )": "messaging",
    "IOT and IIOT | 物联网和工业物联网": "iot",
    "IoT and IIoT": "iot",
    "Incubator | 孵化器": "incubator",
    "Incubator": "incubator",
    "Data Visualization | 数据可视化": "datavisualization",
    "Data Visualization": "datavisualization",
    "Culture | 文化": "culture",
    "Culture": "culture",
    "Community | 社区": "community",
    "Community": "community",
    "Big Data | 大数据": "bigdata",
    "Big Data": "bigdata",
    "AI": "ai",
    "AI | 人工智能": "ai",
    "API/MicroService | API/微服务框架": "api",
    "API/Microservice": "api",
    "RPC | 远程过程调用": "rpc",
    "RPC": "rpc",
    "General | 常规": "rpc",
    "General": "general"
}
session_types_dictionary = {"中文": "Chinese Session",
                            "英文": "English Session",
                            "Chinese": "Chinese Session",
                            "English": "English Session"}

session_types_chinese_dictionary = {"中文": "中文演讲",
                                    "英文": "英文演讲",
                                    "English": "英文演讲",
                                    "Chinese": "中文演讲"}

column_name_transform_dict = {
    "translator_type": "翻译语言",
    "type": "演讲语言",
    "track": "Track",
    "title": "演讲题目",
    "status": "审核状态",
    "abstract": "内容摘要",
    "speaker_name": "讲师{}-姓名",
    "speaker_company": "讲师{}-单位名称",
    "speaker_title": "讲师{}-职称",
    "speaker_bios": "讲师{}-简介",
    "time_schedule": "日程安排"
}

trans_cn_code = "zh-CHS"
trans_en_code = "en"
session_success_status = "审核通过"
translator_type_zh = "中文"
translator_type_en = "英文"
speaker_data = '{0}: {1}, {2}, {3}'
no_speaker_flag = "无"


def write_origin_file(file, file_name, mate_data, abstract, speakers_arr):
    file.write(mate_data)
    file.write(abstract)
    file.write("\n ### Speakers: \n ")
    head_img = '<img src="images/speaker/{}" width="200" />'
    for index, speaker in enumerate(speakers_arr):
        if index == 0:
            head_img_name = file_name.split("-")[1]+".png"
        else:
            head_img_name = file_name.split("-")[1] + "_" + str(index+1) + ".png"
        file.write(head_img.format(head_img_name))
        file.write("<br>")
        file.write(speaker_data.format(speaker[0], speaker[1], speaker[2], speaker[3]))
        file.write("\r\n ")
    file.close()


def write_translate_file(file, file_name, mate_data, abstract, speakers_arr, trans_from, trans_to):
    file.write(mate_data)
    abstract = translator(abstract, trans_from, trans_to)
    file.write(abstract)
    file.write("\n ### Speakers: \n ")
    head_img = '<img src="images/speaker/{}" width="200" />'
    for index, speaker in enumerate(speakers_arr):
        name = translator(speaker[0], trans_from, trans_to)
        company = translator(speaker[1], trans_from, trans_to)
        title = translator(speaker[2], trans_from, trans_to)
        bios = translator(speaker[3], trans_from, trans_to)

        if index == 0:
            head_img_name = file_name.split("-")[1] + ".png"
        else:
            head_img_name = file_name.split("-")[1] + "_" + str(index + 1) + ".png"
        file.write(head_img.format(head_img_name))
        file.write("<br>")
        file.write(speaker_data.format(name, company, title, bios))
        file.write("\r\n ")
    file.close()


for index in sessions.index:
    session_status = sessions.at[index, column_name_transform_dict.get("status")]

    if session_status == session_success_status:
        translator_type = sessions.at[index, column_name_transform_dict.get("translator_type")]

        session_type = sessions.at[index, column_name_transform_dict.get("type")]
        track_name = sessions.at[index, column_name_transform_dict.get("track")]
        track_name = tracks_dictionary.get(track_name)
        session_title = sessions.at[index, column_name_transform_dict.get("title")]
        session_abstract = sessions.at[index, column_name_transform_dict.get("abstract")]

        speakers_arr = []
        for no in range(1, 4):
            speaker_name_key = column_name_transform_dict.get("speaker_name").format(str(no))
            speaker_name = sessions.at[index, speaker_name_key]
            if pd.isnull(speaker_name) or speaker_name == no_speaker_flag:
                continue
            speaker_company_key = column_name_transform_dict.get("speaker_company").format(str(no))
            speaker_company = sessions.at[index, speaker_company_key]
            speaker_title_key = column_name_transform_dict.get("speaker_title").format(str(no))
            speaker_title = sessions.at[index, speaker_title_key]
            speaker_bios_key = column_name_transform_dict.get("speaker_bios").format(str(no))
            speaker_bios = sessions.at[index, speaker_bios_key]
            speakers_arr.append([speaker_name, speaker_company, speaker_title, speaker_bios])
            # print(speakers_arr)

        # create the markdown file
        print(session_title)
        file_name = str(index + 1000)
        file_name = track_name + "-" + file_name
        markdown_en_file = open(file_name + ".md", "w+", encoding="utf8")
        markdown_zh_file = open(file_name + ".zh.md", "w+", encoding="utf8")
        mate_data = '---\ntitle: "{}"\ndate: "{}" \ntrack: "{}"\npresenters: "{}"\nstype: "{}"\n---\n'

        schedule_time = ""
        if not pd.isnull(sessions.at[index, column_name_transform_dict.get("time_schedule")]):
            schedule_time = sessions.at[index, column_name_transform_dict.get("time_schedule")]

        speakers_arr = numpy.array(speakers_arr)
        speakers = speakers_arr[:, 0]
        speakers = ",".join(speakers)

        if translator_type == translator_type_en:
            session_type_en = session_types_dictionary.get(session_type)
            mate_data_str = mate_data.format(session_title,
                                             schedule_time,
                                             track_name,
                                             speakers,
                                             session_type_en)
            write_origin_file(markdown_en_file, file_name, mate_data_str, session_abstract, speakers_arr)
            # Translate English to Chinese
            session_title_cn = translator(session_title, trans_en_code, trans_cn_code)
            session_type_cn = session_types_chinese_dictionary.get(session_type)
            mate_data_str_cn = mate_data.format(session_title_cn,
                                                schedule_time,
                                                track_name,
                                                speakers,
                                                session_type_cn)

            write_translate_file(markdown_zh_file, file_name,  mate_data_str_cn, session_abstract, speakers_arr, trans_en_code,
                                 trans_cn_code)

        elif translator_type == translator_type_zh:
            session_type_cn = session_types_chinese_dictionary.get(session_type)
            mate_data_str = mate_data.format(session_title,
                                             schedule_time,
                                             track_name,
                                             speakers,
                                             session_type_cn)
            write_origin_file(markdown_zh_file, file_name, mate_data_str, session_abstract, speakers_arr)
            # Translate Chinese to English
            session_type_en = session_types_dictionary.get(session_type)
            session_title_en = translator(session_title, trans_cn_code, trans_en_code)
            mate_data_str_en = mate_data.format(session_title_en,
                                                schedule_time,
                                                track_name,
                                                speakers,
                                                session_type_en)
            write_translate_file(markdown_en_file, file_name, mate_data_str_en, session_abstract, speakers_arr, trans_cn_code,
                                 trans_en_code)
