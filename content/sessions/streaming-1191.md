---
title: "Real-Time Data Integration Practice Based on Flink CDC at Alibaba Cloud"
date: "2023-08-19T13:30:00" 
track: "streaming"
presenters: "Chen Zhengyu"
stype: "Chinese Session"
---
CDC (Change Data Capture) is a technology used to capture changes from databases. Flink CDC is an open-source representative of real-time data integration frameworks, with technical advantages such as full incremental integration, lock-free reading, concurrent reading, and distributed architecture, which are highly popular in the open-source community.

Flink CDC supports powerful data processing capabilities and can use SQL to perform real-time association, aggregation, flattening, and more on database data. With Flink's rich downstream ecosystem, processed data can be easily written to downstream systems such as Kafka, Hudi, Iceberg, and Doris, enabling real-time data lake and warehouse integration.

In this presentation, we will first introduce the core design and key implementation of Flink CDC technology, and explain in detail the new features of version 2.4.0. Then, based on specific business scenarios, we will share Alibaba Cloud's internal Flink CDC solutions for different business pain points, such as data lake and warehouse integration scenarios, and binlog expiration issues.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230616/1746465060.jpg" width="200" /><br>
Ruan Hang is a senior research and development engineer at Alibaba Cloud, Flink CDC Maintainer & Apache Flink Contributor
 <br><br>