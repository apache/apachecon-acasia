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
import os
import pandas as pd

path = "../content/sessions/"
files = os.listdir(path)
sessions = pd.read_excel('ApacheConSessions.xlsx')
no_schedule_status = "未安排"
schedule_field_key = "日程安排"

for file_name in files:
    if file_name.startswith("keynote"):
        continue
    # get file id mapping excel line number
    file_id = file_name.split("-")[1].split(".")[0]
    line_id = int(file_id) - 1000
    print(line_id)
    # get schedule from excel
    session_date = sessions.at[line_id, schedule_field_key]
    if session_date == no_schedule_status:
        continue
    session_date_t = session_date.strftime("%Y-%m-%dT%H:%M:%S")
    print(session_date_t)
    file = path + file_name
    with open(file, 'r+', encoding='utf-8') as u:
        lines = u.readlines()
        lines[2] = 'date: "' + session_date_t + '"\n'
        u.seek(0)
        u.truncate()
        u.writelines("".join(lines))
        u.flush()
        u.close()
