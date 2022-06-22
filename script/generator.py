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

import pandas as pd

sessions = pd.read_excel('ApacheConSessions.xlsx')
tracks_dictionary = {"Integration": "integration",
                     "Workflow/Data Governance": "workflowdatagovernance",
                     "Web Server/Tomcat": "webserverandtomcat",
                     "Streaming": "streaming",
                     "Observability": "observability",
                     "Middleware": "middleware",
                     "Messaging": "messaging",
                     "IoT/IIoT": "iot",
                     "Incubator": "incubator",
                     "Data Visualization": "datavisualization",
                     "Culture": "culture",
                     "Community": "community",
                     "Big Data": "bigdata",
                     "API / Microservice": "api"
                     }
session_types_dictionary = {"中文演讲": "Chinese Session",
                             "Regular Session": "English Session"}

session_types_chinese_dictionary = {"中文演讲": "中文演讲",
                             "Regular Session": "英文演讲"}


def remove_speakers_email(speakers):
    speaker_list = speakers.split(",")
    result_list = []
    for speaker in speaker_list:
        result_list.append(remove_speaker_email(speaker))
    return ', '.join(result_list)


def remove_speaker_email(speaker):
    return speaker.split('<')[0].strip()


for index in sessions.index:
    if sessions.at[index, 'Status'] == 'accept':
        # create the markdown file
        print(sessions.at[index, 'English Title'])
        file_name = str(index + 1000)
        markdown_en_file = open(file_name + ".md", "w+")
        markdown_zh_file = open(file_name + ".zh.md", "w+")
        mate_data = '---\ntitle: "{}"\ndate: "{}" \ntrack: "{}"\npresenters: "{}"\nstype: "{}"\n---\n'
        schedule_time = ""
        if not pd.isnull(sessions.at[index, 'Time schedule']):
            schedule_time = sessions.at[index, 'Time schedule']
        title = sessions.at[index, 'English Title']

        # map the session type
        session_type = session_types_dictionary.get(sessions.at[index, 'Type'])

        # update the track information
        track = tracks_dictionary.get(sessions.at[index, 'Category'])
        speakers = remove_speakers_email(sessions.at[index, 'Speaker(s)'])
        abstract = sessions.at[index, "English Abstract"]
        speaker_bios = sessions.at[index, "English Bios"]
        markdown_en_file.write(mate_data.format(title,
                                                schedule_time,
                                                track,
                                                speakers,
                                                session_type))
        markdown_en_file.write(abstract)
        markdown_en_file.write("\n ### Speakers: \n ")
        markdown_en_file.write(speaker_bios)
        markdown_en_file.close()

        if not pd.isnull(sessions.at[index, 'Chinese Title']):
            title = sessions.at[index, 'Chinese Title']
        if not pd.isnull(sessions.at[index, "Chinese Abstract"]):
            abstract = sessions.at[index, "Chinese Abstract"]
        if not pd.isnull(sessions.at[index, "Chinese Bios"]):
            speaker_bios = sessions.at[index, "Chinese Bios"]

        # map the session type
        session_zh_type = session_types_chinese_dictionary.get(sessions.at[index, 'Type'])

        markdown_zh_file.write(mate_data.format(title,
                                                schedule_time,
                                                track,
                                                speakers,
                                                session_zh_type))
        markdown_zh_file.write(abstract)
        markdown_zh_file.write("\n ### 讲师: \n ")
        markdown_zh_file.write(speaker_bios)
        markdown_zh_file.close()
