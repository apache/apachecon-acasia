---
title: "Spark SQL shuffle join在eBay的改进"
date: "2023-08-18T14:30:00" 
track: "datastorage"
presenters: "王玉明"
stype: "中文演讲"
---
Join操作是数据仓库中最重要、应用最广泛的操作之一。Apache Spark中的Join算子是最昂贵的操作符之一，尤其是Shuffle Join。

在本次演讲中，将介绍eBay最近添加的一系列Shuffle Join优化。
具体如下：
 - Unwrap连接条件使用桶连接。
 - 增强shuffle交换重用以减少表扫描。
 - 通过Join下推部分聚合。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230605/1650461080.jpg" width="200" /><br>王玉明: eBay, 软件工程师, eBay SQL on Hadoop 团队软件开发工程师，Apache Spark PMC Member and Committer，2022 SIGMOD Systems Award 获得者。从Spark 1.5.0开始参与Apache Spark的开发，并成为最活跃的代码贡献者之一。专注于SQL查询性能优化。
 <br><br>