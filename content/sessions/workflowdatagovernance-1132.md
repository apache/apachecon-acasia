---
title: "Apache Linkis data processing practices"
date: "2022-07-31T14:10:00"
track: "workflowdatagovernance"
presenters: "李孟"
stype: "Chinese Session"
---
Linkis background
Linkis builds a layer of computing middleware between the upper application and the lower engine. By using standard interfaces such as REST, WebSocket, and JDBC provided by Linkis, upper-layer applications can easily access low-level engines such as Spark, Presto, and Flink, and realize cross-engine context sharing, unified computing tasks, and engine governance and choreography capabilities.
As for Linkis data processing practice, I mainly share two aspects, one is about metadata, the other is about computing tasks.
metadata
Metadata is divided into three categories: Linkis provides metadata management capabilities for data assets based on Linkis DataSource and Apache Atlas services. DataSource service boundary Because many of the open source tools in the WeDataSphere community (Scriptis\Visulalis\Exchangis\Streamis) use data sources, lack unified management capabilities and require users to set up data sources multiple times in different products, We want to provide a unified data source management service so that a single setup can be used in multiple places. Atlas is a set of extensible and extensible core basic governance services. Linkis EngineConn (Engine Connector) is integrated based on Atlas Hook. Data information, features and blood relationships involved in the execution of calculation are collected in Atlas for use by upstream data assets.
Computing tasks
Dolphinscheduler pull Linkis computing tasks, dolphinscheduler Shell task type Through LinkisDolphinSchedulerClient configuration parameters, pull up relevant tasks.
summary
To this Linkis data processing of the overall link, involving metadata, scheduling tasks, forming a complete closed loop.
 ### Speakers: 
 <img src="images/speaker/1132.png" width="200" /><br>Meng Li: Shanghai Xianweng Technology co, The data architecture, Years of experience in data architecture, CSDN blogger, open source enthusiast, Beam community contributor, WeDataSphere community contributor.

 