---
title: "Spark SQL Shuffle Join Improvement at eBay"
date: "2023-08-18T14:30:00" 
track: "datastorage"
presenters: "王玉明"
stype: "Chinese Session"
---
Join operation is one of the most important and widely used operations in data warehouse.
The Join operator in Apache Spark is one of the most expensive operators, especially Shuffle Join.

In this presentation, we will introduce a series of Shuffle Join optimizations recently added at eBay.

Specifically,
  - Unwrap join condition to use bucket join. 
  - Enhance shuffle exchange reuse to reduce table scans. 
  - Push down partial aggregation through Join.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230605/1650461080.jpg" width="200" /><br>Wang Yuming: eBay, Software engineer, Software Development Engineer, eBay SQL on Hadoop team, Apache Spark PMC Member and Committer, 2022 SIGMOD Systems Award winner. He has been involved in the development of Apache Spark since Spark 1.5.0 and has become one of the most active code contributors. Focus on SQL query performance optimization.
 <br><br>