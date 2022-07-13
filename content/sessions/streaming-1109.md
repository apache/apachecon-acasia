---
title: "Efficient construction of real-time data lakes based on Flink CDC and Hudi"
date: "2022-07-30T13:30:00"
track: "streaming"
presenters: "徐榜江"
stype: "Chinese Session"
---
Business data in a database is one of the most valuable data, and how to effectively and efficiently synchronize this data into the data lake is a very valuable topic.
CDC (Change Data Capture) is a technology used to Capture changes from the database. Flink CDC is the open source representative of real-time Data integration framework, with full incremental integration, lockless read, concurrent read, distributed architecture and other technical advantages, which is very popular in the open source community. In addition to real-time lake and warehouse access, Flink CDC also supports robust data processing capabilities, Real-time association, aggregation and widening of database data can be done through SQL, and the processed data can be conveniently written into downstream Kafka, Hudi, Iceberg and Doris with the rich downstream ecology of Flink.

In this sharing, Professor Xu Bangjiang will first share the core design and implementation of Flink CDC, such as lock-free algorithm, parallel reading, breakpoint continuation and distributed architecture, and share the application of Flink CDC in different scenarios based on specific business scenarios. Then the demo will explain how to efficiently build a real-time data lake based on Flink CDC and Hudi.
 ### Speakers: 
 <img src="images/speaker/1109.png" width="200" /><br>Bangjiang Xu: Ali cloud, Senior R&d Engineer, Apache Flink Committer & Flink CDC Maintainer, specializes in Flink SQL, Flink CDC, data integration, has spoken and shared Apache Flink, Flink CDC Maintainer many times.
https://github.com/apache/flink
https://github.com/ververica/flink-cdc-connectors

 