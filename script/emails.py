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


def get_speakers_email(speakers):
    speaker_list = speakers.split(",")
    result_list = []
    for speaker in speaker_list:
        result_list.append(get_speaker_email(speaker))
    return result_list


def get_speaker_email(speaker):
    parts = speaker.partition('<')
    email = (parts[2]).partition('>')[0]
    names = parts[0].partition(' ')
    first_name = names[0]
    last_name = ''
    if names[1] == ' ':
        last_name = names[2]
    return "{0},{1},{2}\n".format(email, first_name, last_name)


# Extract the emails information from session data

email_csv = open("email-apachecon.csv", "w+")
email_csv.write("Email, FirstName, LastName\n")


for index in sessions.index:
    if sessions.at[index, 'Status'] == 'accept':
        # create the markdown file
        print(sessions.at[index, 'English Title'])

        speakers_email = get_speakers_email(sessions.at[index, 'Speaker(s)'])
        for speaker_email in speakers_email:
            email_csv.write(speaker_email)

email_csv.close()
