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

from io import UnsupportedOperation
import json
import openpyxl
import csv
import os

def update(path,url):
    with open(path,'r+',encoding='utf-8') as u:
        lines=u.readlines()
        lines[5]=lines[5]+'speechLink: "'+url+'"\n'
        u.seek(0)
        u.truncate()
        u.writelines("".join(lines))
        u.flush
        u.close

with open('json/bilibili_data.json','r+',encoding='utf-8') as rf:
    bili_data=json.load(rf)
    fileList=os.listdir("content/sessions/")

    for data in bili_data:
        url=data['url']
        url = "//player.bilibili.com/player.html?bvid=" + url.split("video/")[1]

        titles=data['title'].split('：')
        if len(titles)==0 :
            titles=data['title'].split(':')
        name=titles[1].split('-')[0].strip()
        title=titles[1].split('-')[1].strip()
         
        for file in fileList:
            fileName="content/sessions/"+file
            #print(fileName)     
              
            with open(fileName,'r+',encoding='utf-8') as md:
                lines=md.readlines()
                
                mdTitle=lines[1].split(':')[1].split('"')[1]
                flag=False
                if title == mdTitle :
                    mdNum=fileName
                    flag=True
                    urlSplit=file.split('.',)
                    if len(urlSplit)==3:
                        update(fileName,url)
                    if len(urlSplit)==2:
                        file=urlSplit[0]+".zh."+urlSplit[1]
                        fileName="content/sessions/"+file
                        update(fileName,url)
                    break

        if flag==False:
            for file in fileList:
                fileName="content/sessions/"+file
                #print(fileName)
                with open(fileName,'r+',encoding='utf-8') as md:
                    lines=md.readlines()
                    
                    nameOrRoom=lines[4].split(':')[0]
                    if nameOrRoom=="room":
                        mdName=lines[5].split(':')[1].split('"')[1]
                    else :
                        mdName=lines[4].split(':')[1].split('"')[1]
                    if name == mdName :
                        mdNum=fileName
                        flag=True
                        urlSplit=file.split('.',)
                        if len(urlSplit)==3:
                            update(fileName,url)
                        if len(urlSplit)==2:
                            file=urlSplit[0]+".zh."+urlSplit[1]
                            fileName="content/sessions/"+file
                            update(fileName,url)
                        break
    
# Open the EXECL file
collect=openpyxl.load_workbook("./已完成修改部分-fix-all.xlsx")

# Gets the active table object
collect_active=collect.active

for cell in collect_active['A']:
    url=cell.value
    if url != None and url != "页面地址" :
        hugo_url=url.split("sessions/")[1].split(".")[0] +".md"
        youtube_url=collect_active.cell(cell.row,5).value
        if len(youtube_url) > 30 :
            youtube_url = "https://www.youtube.com/embed/" + youtube_url.split("=")[1]
        else :
            youtube_url = "https://www.youtube.com/embed/" + youtube_url.split("be/")[1]
        hugo_url = "content/sessions/" + hugo_url
        update(hugo_url, youtube_url)
