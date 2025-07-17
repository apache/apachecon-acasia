const fs = require('fs');
const xlsx = require('xlsx');
const path = require('path');
const tracks_dictionary = require('./tracks_dictionary.json');

const roomJson = {
  'MainRoom - YiHe Hall': '主会场 - 颐和厅',
  'YiHe Hall': '颐和厅',
  'WanChun Hall': '万春厅',
  'JingYi Hall': '静宜厅',
  'JingMing Hall': '静明厅',
  'YuanMing Hall': '圆明厅',
  'Mtn WanShou Hall': '万寿山会议室',
  'Mtn BaiWang Hall': '百望山会议室',
  'Mtn Yang Hall': '阳山会议室',
  'Mtn YuQuan Hall': '玉泉山会议室',
}

// 读取Excel文件
function readExcelFile(filePath) {
  try {
    const workbook = xlsx.readFile(filePath);
    const sheetName = workbook.SheetNames[0];
    return xlsx.utils.sheet_to_json(workbook.Sheets[sheetName]);
  } catch (error) {
    console.error('读取Excel文件失败:', error);
    throw error;
  }
}

// 解析 frontmatter
function splitFrontmatterAndContent(fileContent) {
  const parts = fileContent.split(/^---$/m);
  if (parts.length >= 3) {
    return {
      frontmatter: parts[1].trim(),
      content: parts.slice(2).join('---').trim()
    };
  }
  return null;
}

// 格式化日期
function formatExcelDate(excelDate) {
  if (!excelDate) return '';
  const date = new Date(Math.round((excelDate - 25569) * 86400 * 1000));
  return date.toISOString().slice(0, 19);
}

async function updateSessionDates() {
  try {
    console.log('开始更新会话时间...');
    
    // 读取Excel数据
    const rawSessions = readExcelFile('./ApacheConSessions.xlsx');
    
    // 创建会话时间映射
    const sessionDates = new Map();
    rawSessions.forEach(session => {
      const trackValue = tracks_dictionary[session['Track'] || 'unknown'];
      // if (trackValue === '5minstalk') {
      //   return;
      // }
      const sessionId = session['Session Id'];
      const fileName = `${trackValue}-${sessionId}`;
      const scheduledDate = formatExcelDate(session['Scheduled At']);
      const info = {
        scheduledDate: scheduledDate,
        room: session['Room'].trim() || '' // 获取房间信息，为空时使用空字符串
      };
      sessionDates.set(fileName, info);
    });
    
    // 读取并更新文件
    const sessionsDir = path.join(process.cwd(), '../content', 'sessions');
    const files = fs.readdirSync(sessionsDir);
    let updatedCount = 0;
    
    // 使用 Set 跟踪已处理的文件
    const processedFiles = new Set();
    
    files.forEach((file, index) => {
      const baseName = file.replace(/\.zh\.md$/, '').replace(/\.md$/, '');
      
      // 跳过已处理的文件
      if (processedFiles.has(baseName)) {
        return;
      }
      processedFiles.add(baseName);
      
      // 检查是否需要更新
      const scheduledDate = sessionDates.get(baseName);
      if (scheduledDate) {
        console.log(`更新文件: ${baseName}`);
        
        // 更新两个文件（.md 和 .zh.md）
        ['.md', '.zh.md'].forEach(ext => {
          const filePath = path.join(sessionsDir, `${baseName}${ext}`);
          if (fs.existsSync(filePath)) {
            const content = fs.readFileSync(filePath, 'utf8');
            const parts = splitFrontmatterAndContent(content);
            
            if (parts) {
              // 更新 frontmatter 中的 date
              const info = sessionDates.get(baseName);
              const realRoom = (ext.includes('zh') ? roomJson[info.room] : info.room) || "";
              let updatedFrontmatter = parts.frontmatter;
              // 检查是否存在 room 字段
              if (updatedFrontmatter.includes('room:')) {
                // 更新已存在的 room 和 date
                updatedFrontmatter = updatedFrontmatter
                  .replace(/^date:.*$/m, `date: "${info.scheduledDate}"`)
                  .replace(/^room:.*$/m, `room: "${realRoom}"`);
              } else {
                // 只更新 date，并添加 room
                updatedFrontmatter = updatedFrontmatter
                  .replace(/^date:.*$/m, `date: "${info.scheduledDate}"`) + 
                  `\nroom: "${realRoom}"`;
              }
              
              // 写回文件
              const updatedContent = `---\n${updatedFrontmatter}\n---\n\n${parts.content}`;
              fs.writeFileSync(filePath, updatedContent, 'utf8');
              updatedCount++;
              
              console.log(`已更新: ${baseName}${ext}`);
            }
          }
        });
      }
    });
    
    console.log(`更新完成，共更新 ${updatedCount} 个文件`);
    return updatedCount;
    
  } catch (error) {
    console.error('更新过程中出错:', error);
    throw error;
  }
}

// 执行更新
if (require.main === module) {
  updateSessionDates().catch(error => {
    console.error('执行失败:', error);
    process.exit(1);
  });
}

module.exports = {
  updateSessionDates
};