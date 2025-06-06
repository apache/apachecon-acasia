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
    console.log(`创建目录: ${outputDir}`);
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

/**
 * 移除演讲者信息中的email地址(如果有)
 * @param {string} speakers - 多个演讲者的字符串，以逗号分隔
 * @returns {string} 移除email后的演讲者列表
 */
function removeSpeakersEmail(speakers) {
  if (!speakers) return '';
  
  // 将多个演讲者按逗号分隔
  const speakerList = speakers.split(',');
  const resultList = [];
  
  // 对每个演讲者移除email
  for (const speaker of speakerList) {
    resultList.push(removeSpeakerEmail(speaker));
  }
  
  // 重新组合为字符串
  return resultList.join(', ');
}

/**
 * 移除单个演讲者的email地址(格式通常为"姓名 <email>")
 * @param {string} speaker - 单个演讲者信息
 * @returns {string} 移除email后的演讲者名称
 */
function removeSpeakerEmail(speaker) {
  // 取<符号前的部分并去除空格
  return speaker.split('<')[0].trim();
}

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

function updateFileContent(filePath, newFrontmatter, newContent) {
  if (fs.existsSync(filePath)) {
    const existingContent = fs.readFileSync(filePath, 'utf8');
    const parts = splitFrontmatterAndContent(existingContent);
    
    if (parts) {
      // update frontmatter
      const updatedContent = `---\n${newFrontmatter}---\n${parts.content}`;
      fs.writeFileSync(filePath, updatedContent, 'utf8');
    } else {
      const fullContent = `---\n${newFrontmatter}---\n${newContent}`;
      fs.writeFileSync(filePath, fullContent, 'utf8');
    }
  } else {
    const fullContent = `---\n${newFrontmatter}---\n${newContent}`;
    fs.writeFileSync(filePath, fullContent, 'utf8');
  }
}

/**
 * 主函数 - 处理Excel文件并生成Markdown文件
 */
function main() {
  // 读取Excel文件
  const sessions = readExcelFile('./ApacheConSessions.xlsx');
  
  // 遍历所有session数据
  for (let index = 0; index < sessions.length; index++) {
    const session = sessions[index];
    
    // 只处理状态为"accept"的被接受的session
    if (session['Status'] === 'Accepted') {
      const track = tracksDictionary[session['Track']];
      if (track === 'dataops') {
        console.log(`找到对应的track: ${session['Track']}，跳过该session`);
      }
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
    
      
      // 处理演讲者信息(移除email)
      const speakers = removeSpeakersEmail(session['Owner']);
      
      // 获取英文摘要和演讲者简介
      const abstract = session['Description'];
      const speakerBios = session['Bio'];
      let enAbstract = abstract;
      if (enAbstract && enAbstract.includes('标题：')) {
        enAbstract = abstract.split('标题：')[0];
      }
      
      // 处理演讲者头像
      let headImgHtml = '';
      if (session['Profile Picture']) {
        const speakerImage = session['Profile Picture'];
        headImgHtml = `<img src="${speakerImage}" width="200" /><br/>`;
      }
      
      // 修改后:
      const enFrontmatter = `title: "${title}"
date: "${scheduleTime}"
track: "${track}"
presenters: "${speakers}"
stype: "${sessionType}"`;
      const enContent = `${abstract}\n### Speakers:\n${headImgHtml}\n${speakerBios}`;
      updateFileContent(enFilePath, enFrontmatter, enContent);
      
      // 处理中文内容
      let zhTitle = title;
      let zhAbstract = abstract;
      let zhSpeakerBios = speakerBios;
      
      // 如果存在中文版本，则使用中文内容
      if (zhAbstract && zhAbstract.includes('标题：')) {
        zhTitle = zhAbstract.split('标题：')[1];
        if (zhTitle && zhTitle.includes('议题介绍：')) {
          const parts = zhTitle.split('议题介绍：');
          zhTitle = parts[0].trim().replaceAll(/\\n/g, '');
          zhAbstract = parts[1];
        }
      }
      
      if (session['Chinese Bios']) {
        zhSpeakerBios = session['Chinese Bios'];
      }
      
      const sessionZhType = sessionTypesChineseDictionary[session['Language']];
    
      const zhFrontmatter = `title: "${title}"
date: "${scheduleTime}"
track: "${track}"
presenters: "${speakers}"
stype: "${sessionZhType}"`;
        const zhContent = `${zhAbstract}\n### 讲师:\n${headImgHtml}\n${zhSpeakerBios}`;
      
      updateFileContent(zhFilePath, zhFrontmatter, zhContent);
    }
  }
}

// 执行主函数
main();