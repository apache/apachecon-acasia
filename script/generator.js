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

// 定义track(轨道/分类)的映射字典，将中文/英文分类名映射为URL友好的格式
const tracksDictionary = {
  "Cloud Native": "cloudnative",
  "DataOps": "dataops",
  "Streaming": "streaming",
  "Incubator": "incubator",
  "Data Lake & Data Warehouse": "datalake",
  "OLAP & Data Analysis": "olap",
  "Community": "community",
  "Data Storage & Computing": "datastorage",
  "Web Application & Framework": "webserver",
  "AI": "ai",
  "IoT": "iot",
  "Messaging": "messaging",
  "Microservice": "microservice",
  "Observability": "observability",
  "Rust": "rust",
  "General": "general",
  "Keynote": "keynote",
  "5-mins-Lightning-Talk": "5minstalk"
};

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

function splitFrontmatterAndContent(fileContent) {
  const parts = fileContent.split('---\n');
  if (parts.length >= 3) {
    return {
      frontmatter: parts[1],
      content: parts.slice(2).join('---\n')
    };
  }
  return null;
}

function parseFrontmatter(frontmatter) {
  const lines = frontmatter.trim().split('\n');
  const result = {};
  lines.forEach(line => {
    const [key, ...values] = line.split(':');
    if (key && values.length) {
      result[key.trim()] = values.join(':').trim().replace(/^"(.*)"$/, '$1');
    }
  });
  return result;
}

function updateFileContent(filePath, newFrontmatter, newContent) {
  if (fs.existsSync(filePath)) {
    // 如果文件存在，读取原内容
    const existingContent = fs.readFileSync(filePath, 'utf8');
    const parts = splitFrontmatterAndContent(existingContent);
    if (parts) {
      const existingFrontmatter = parseFrontmatter(parts.frontmatter);
      const newFrontmatterObj = parseFrontmatter(newFrontmatter);
      newFrontmatterObj.title = existingFrontmatter.title;
      
      const updatedFrontmatter = Object.entries(newFrontmatterObj)
        .map(([key, value]) => `${key}: "${value}"`)
        .join('\n');
      const updatedContent = `---\n${updatedFrontmatter}\n---\n\n${parts.content}`;
      fs.writeFileSync(filePath, updatedContent, 'utf8');
    } else {
      const fullContent = `---\n${newFrontmatter}\n---\n\n${newContent}`;
      fs.writeFileSync(filePath, fullContent, 'utf8');
    }
  } else {
    const fullContent = `---\n${newFrontmatter}\n---\n\n${newContent}`;
    fs.writeFileSync(filePath, fullContent, 'utf8');
  }
}


function processAndGroupSessions(sessions) {
  // 创建 Map 用于存储分组数据
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
    if (session['Status'] === 'Accepted') {
      const track = tracksDictionary[session['Track']];
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
        speakerBios += `\n${speaker.avatar}\n${speaker.name}\n\n${speaker.bio}\n\n`;
      })
      let enAbstract = abstract;
      if (enAbstract && enAbstract.includes('标题：')) {
        enAbstract = abstract.split('标题：')[0];
      }
      
      // 修改后:
      const enFrontmatter = `title: "${title}"
date: "${scheduleTime}"
track: "${track}"
presenters: "${speakers}"
stype: "${sessionType}"`;
      const enContent = `${abstract}\n\n### Speakers:\n\n${speakerBios}`;
      updateFileContent(enFilePath, enFrontmatter, enContent);
      
      // // 处理中文内容
      // let zhTitle = title;
      // let zhAbstract = abstract;
      // let zhSpeakerBios = speakerBios;
      
      // // 如果存在中文版本，则使用中文内容
      // if (zhAbstract && zhAbstract.includes('标题：')) {
      //   zhTitle = zhAbstract.split('标题：')[1];
      //   if (zhTitle && zhTitle.includes('议题介绍：')) {
      //     const parts = zhTitle.split('议题介绍：');
      //     zhTitle = parts[0].trim().replaceAll(/\\n/g, '');
      //     zhAbstract = parts[1];
      //   }
      // }
      
      // const sessionZhType = sessionTypesChineseDictionary[session['Language']];
    
//       const zhFrontmatter = `title: "${title}"
// date: "${scheduleTime}"
// track: "${track}"
// presenters: "${speakers}"
// stype: "${sessionZhType}"`;
//         const zhContent = `${zhAbstract}\n\n### 讲师:\n\n${headImgHtml}\n\n${zhSpeakerBios}`;
      
//       updateFileContent(zhFilePath, zhFrontmatter, zhContent);
    }
  }
}


main()