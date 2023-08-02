---
title: "Push down partial aggregate through Join"
date: "2023-08-18T14:30:00" 
track: "datastorage"
presenters: "王玉明"
stype: "Chinese Session"
---
Join first and then aggregation is one of the common operations in the database. aggregation tends to reduce the output data. In order to optimize this kind of query, partial aggregate in aggregation can be pushed down to execute before join. After partial aggregate is pushed down, the data volume of shuffle, sort and join may be reduced. Better plans may result. This session details how to implement this optimization in Spark SQL, the results of the TPC-DS performance test, and the effect after production.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230605/1650461080.jpg" width="200" /><br>Wang Yuming: eBay, Software engineer, Software Development Engineer, eBay SQL on Hadoop team, Apache Spark PMC Member and Committer, 2022 SIGMOD Systems Award winner. He has been involved in the development of Apache Spark since Spark 1.5.0 and has become one of the most active code contributors. Focus on SQL query performance optimization.
 <br><br>