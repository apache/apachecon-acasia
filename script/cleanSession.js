const fs = require('fs');
const xlsx = require('xlsx');
const path = require('path');
const tracks_dictionary = require('./tracks_dictionary.json');

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

// 清理会话文件的主函数
async function cleanupSessions() {
  try {
    // 读取 Excel 文件中的所有数据
    const rawSessions = readExcelFile('./ApacheConSessions.xlsx');
    
    // 获取所有 Accepted 状态的 Session Id
    const acceptedIds = new Set();
    rawSessions.forEach(session => {
      if (session['Status'] === 'Accepted') {
        const trackValue = tracks_dictionary[session['Track']] || 'unknown';
        const sessionId = session['Session Id'];
        const fileName = `${trackValue}-${sessionId}`;
        acceptedIds.add(fileName);
      }
    });
    
    // 读取 sessions 目录
    const sessionsDir = path.join(process.cwd(), '../content', 'sessions');
    
    const files = fs.readdirSync(sessionsDir);
    
    // 使用 Set 跟踪已处理的文件
    const processedFiles = new Set();
    let deletedCount = 0;
  
    
    // 处理每个文件
    files.forEach(file => {
      // 完全移除所有 .md 后缀
      const baseName = file.replace(/\.zh\.md$/, '').replace(/\.md$/, '');
      
      // 如果这个基础文件名已经处理过，跳过
      if (processedFiles.has(baseName)) {
        return;
      }
      processedFiles.add(baseName);
      
      // 检查是否需要删除
      if (!acceptedIds.has(baseName)) {
  
        // 删除对应的两个文件
        const mdFile = path.join(sessionsDir, `${baseName}.md`);
        const zhMdFile = path.join(sessionsDir, `${baseName}.zh.md`);
        
        if (fs.existsSync(mdFile)) {
          console.log(`准备删除: ${baseName}.md`);
          fs.unlinkSync(mdFile);
          deletedCount++;
        }
        
        if (fs.existsSync(zhMdFile)) {
          console.log(`准备删除: ${baseName}.zh.md`);
          fs.unlinkSync(zhMdFile);
          deletedCount++;
        }
      }
    });
    
    console.log(`\n清理完成，共删除 ${deletedCount} 个文件`);
    return deletedCount;
    
  } catch (error) {
    console.error('清理过程中出错:', error);
    throw error;
  }
}

cleanupSessions()