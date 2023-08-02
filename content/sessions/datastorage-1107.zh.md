---
title: "Push down partial aggregate through Join"
date: "2023-08-18T14:30:00" 
track: "datastorage"
presenters: "王玉明"
stype: "中文演讲"
---
先Join，再aggregation是数据库常用的操作之一，aggregation往往会使输出的数据变少。为了优化这类查询，可以把aggregation中的partial aggregate下推到join之前执行，在下推了partial aggregate之后，可能会减少shuffle的数据量，sort的数据量以及join的数据量，因此可能会产生更好的计划。本次议题详细介绍怎样在Spark SQL中实现该优化，TPC-DS性能测试结果以及上生产后的效果。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230605/1650461080.jpg" width="200" /><br>王玉明: eBay, 软件工程师, eBay SQL on Hadoop 团队软件开发工程师，Apache Spark PMC Member and Committer，2022 SIGMOD Systems Award 获得者。从Spark 1.5.0开始参与Apache Spark的开发，并成为最活跃的代码贡献者之一。专注于SQL查询性能优化。
 <br><br>