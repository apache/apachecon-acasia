---
title: "The practice and optimization of data Lake Iceberg in Xiaomi"
date: "2023-08-18T15:45:00" 
track: "datalake"
presenters: "肖杰宝"
stype: "Chinese Session"
---
Introduction: This sharing focuses on introducing the reasons and current situation of Xiaomi's internal introduction of Iceberg, as well as the practice of using Iceberg to upgrade its business architecture, including the optimization of Iceberg Parquet file filtering capability, and the evolution and landing of managed table optimization service architecture.
Outline:
- Why Iceberg is introduced and its current situation
This paper introduces the reason why Iceberg is introduced in Xiaomi and the current production state of Iceberg in Xiaomi
- Lakehouse architecture upgrade practice
It is divided into two parts: table upgrade practice and business architecture upgrade practice. The table upgrading practice mainly describes how to upgrade Hive tables into Iceberg tables and how to make them into products. The service architecture upgrade practice mainly brings practical services to obtain greater benefits by upgrading links to the lake architecture
- Function Optimization
This paper mainly introduces the reading principle of Iceberg and the development of the Parquet Page Index feature, further enhancing Iceberg's Data Skipping capability. It also discusses the integration of Parquet encryption capability in Iceberg to achieve column-level data encryption
- Construction and evolution of managed table optimization services
This paper mainly introduces the issues encountered and the system architecture before the launch of the managed table optimization service, as well as the supported optimization task types, table monitoring, and other related content
- Future Planning
This paper mainly introduces the work that Xiaomi will carry out based on Iceberg in the future, such as index construction, hybrid cloud architecture for storage, intelligent data lake warehouse, and cache acceleration, etc
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230601/1439170843694195.png" width="200" /><br>Xiao Jiebao: Xiaomi, Software development engineer, Xiaomi software research and development engineer, currently mainly responsible for the research and development of Xiaomi's internal data lake Iceberg core and table optimization services.
 <br><br>