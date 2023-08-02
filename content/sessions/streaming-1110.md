---
title: "FlinkSQL's field parentage and data permission solution"
date: "2023-08-18T15:00:00" 
track: "streaming"
presenters: "白松"
stype: "Chinese Session"
---
Data lineage and data security are indispensable capabilities for building an enterprise-level data warehouse. In recent years, with the increasing demand for real-time big data processing in all walks of life, real-time data warehouses (represented by those using Flink) have emerged rapidly. However, due to the relatively short development time, although the field of offline data warehouses based on Apache Ranger and Apache Atlas is relatively mature, those solutions do not yet support Flink SQL, and relying on Ranger and Atlas will lead to excessive system deployment and operation maintenance. Therefore, it is particularly important to design and implement the field lineage and data authority management of FlinkSQL under the premise of zero intrusion into the source code of Flink and Calcite. This sharing will introduce relevant solutions in detail to help the audience build Atlas+Ranger in the field of Flink real-time data warehouse.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230517/0910148400.jpg" width="200" /><br>White pine: Hangzhou Sulan Technology Co., LTD, Deputy general manager of R&D center, Co-founder of Sulan Technology Co., LTD., Deputy general manager of R & D Center, has 9 years of big data platform research experience, focusing on big data, real-time computing, data rights and other fields of research. Responsible for the company's core products digital platform and digital EMR product research and development, digital products have become hundreds of domestic and foreign companies to build data center infrastructure tools, such as CITIC Group, Foxconn, Vanke, BMW, Zhejiang Trading Group and so on.
 <br><br>
