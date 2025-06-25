/**
 * ---------------------------------------------------------------------------
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ---------------------------------------------------------------------------
 */

const fs = require('fs');
const xlsx = require('xlsx');
const path = require('path');
const tracks_dictionary = require('./tracks_dictionary.json');
const { console } = require('inspector');

const outputDir = path.join(__dirname, '../content', 'sessions');
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// 读取Excel文件中的会议session数据
function readExcelFile(filePath) {
  const workbook = xlsx.readFile(filePath);
  const sheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[sheetName];
  // 将工作表转换为JSON对象数组
  return xlsx.utils.sheet_to_json(worksheet);
}

// 定义session类型的英文映射字典
const sessionTypesDictionary = {
  "Chinese": "Chinese Session",
  "English": "English Session"
};

// 定义session类型的中文映射字典
const sessionTypesChineseDictionary = {
  "Chinese": "中文演讲",
  "English": "英文演讲"
};

function formatExcelDate(excelDate) {
  if (!excelDate) return '';
  const date = new Date(Math.round((excelDate - 25569) * 86400 * 1000));
  return date.toISOString().slice(0, 19);
}

function updateFileContent(filePath, newFrontmatter, newContent) {
  if (fs.existsSync(filePath)) {
    console.log('File already exists skip');
  } else {
    const fullContent = `---\n${newFrontmatter}\n---\n\n${newContent}`;
    fs.writeFileSync(filePath, fullContent, 'utf8');
  }
}


function processAndGroupSessions(sessions) {
  const sessionMap = new Map();
  
  sessions.forEach(session => {
    const sessionId = session['Session Id'];
    if (!sessionId) return;
    
    if (!sessionMap.has(sessionId)) {
      // 首次遇到该 Session Id，创建基础数据
      sessionMap.set(sessionId, {
        ...session,
        speakers: [], // 存储所有讲师信息对象数组
      });
    }
    
    // 获取当前存储的数据
    const existingData = sessionMap.get(sessionId);
    
    // 构建讲师信息对象
    if (session['FirstName'] || session['LastName']) {
      const speakerInfo = {
        name: `${session['FirstName'] || ''} ${session['LastName'] || ''}`.trim(),
        avatar: `<img src="${session['Profile Picture']}" width="200" /><br/>\n` || '',
        bio: session['Bio'] || '',
        tagline: session['TagLine'] || '',
      };
      
      // 检查是否已存在相同讲师（通过名字判断）
      const existingSpeaker = existingData.speakers.find(s => s.name === speakerInfo.name);
      if (!existingSpeaker) {
        existingData.speakers.push(speakerInfo);
      }
    }
  });
  
  // 处理合并后的数据
  return Array.from(sessionMap.values()).map(session => ({
    ...session,
    // speakers数组已经是我们需要的格式，不需要额外处理
    speakers: session.speakers
  }));
}


/**
 * 主函数 - 处理Excel文件并生成Markdown文件
 */
function main() {
  const rawSessions = readExcelFile('./ApacheConSessions.xlsx');
  
  // 处理和合并数据
  const processedSessions = processAndGroupSessions(rawSessions);
  
  // 遍历所有session数据
  for (let index = 0; index < processedSessions.length; index++) {
    const session = processedSessions[index];
    
    // 只处理状态为"accept"的被接受的session
    // if (session['Status'] === 'Accepted') {
      const track = tracks_dictionary[session['Track']];
      const fileName = `${track}-${session['Session Id']}`;
      const enFilePath = path.join(outputDir, `${fileName}.md`);
      const zhFilePath = path.join(outputDir, `${fileName}.zh.md`);
      // 获取日期信息
      let scheduleTime = "";
      // if (session['Date Submitted']) {
      //   scheduleTime = formatExcelDate(session['Date Submitted']);
      // }
      
      // 获取英文标题
      let title = session['Title'];
      
      // 映射session类型
      const sessionType = sessionTypesDictionary[session['Language']];
    
      const speakers = session['speakers'].map(v => v.name).join(', ');
      
      // 获取英文摘要和演讲者简介
      const abstract = session['Description'];
      let speakerBios = '';
      session['speakers'].forEach(speaker => {
        speakerBios += `\n${speaker.avatar}\n${speaker.name}: ${speaker.tagline}\n\n${speaker.bio}\n\n`;
      })
      
      // 修改后:
      const enFrontmatter = `title: "${title}"
date: "${scheduleTime}"
track: "${track}"
presenters: "${speakers}"
stype: "${sessionType}"`;
      const enContent = `${abstract}\n\n### Speakers:\n\n${speakerBios}`;
      updateFileContent(enFilePath, enFrontmatter, enContent);


      // .zh.md
      const sessionZhType = sessionTypesChineseDictionary[session['Language']];
      const zhFrontmatter = `title: "${title}"
date: "${scheduleTime}"
track: "${track}"
presenters: "${speakers}"
stype: "${sessionZhType}"`;
        const zhContent = `${abstract}\n\n### 讲师:\n\n${speakerBios}`;
      updateFileContent(zhFilePath, zhFrontmatter, zhContent);
    // }
  }
}


main()