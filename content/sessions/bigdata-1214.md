---
title: "An off-line data discovery method based on consanguinity"
date: "2022-07-29T16:50:00"
track: "bigdata"
room: "B"
presenters: "韩帅,孙科"
stype: "Chinese Session"
---
In the context of data center, users in the field of offline data warehouse often need to solve the following problems:
- Which Hive tables contain service A's data
- Whether permissions of core fields in the Hive table are enlarged due to dump
- Whether the Hive table contains confidential data that needs to be cleared
These problems can be uniformly classified as data discovery problems. Bytedance conducts SQL analysis for offline data warehouse tasks, builds blood relationships of Hive tables, and solves data discovery problems in an automated and engineering way based on tag propagation algorithm, avoiding problems such as long cycle, high cost, low accuracy and inflexibility of manual annotation.
Data discovery includes but is not limited to: Service classification and classification of Hive tables and columns and identification of confidential fields.
Application scenarios:
1. Which Hive tables contain buried data of service A
By analyzing ETL SQL execution logic and various Filter conditions, determine whether the downstream table will contain app='a' data
2. An ODS table stores some confidential data in a complex structure. Through SQL analysis of the downstream table, it can identify whether the downstream table contains part of the data in the complex structure, and then identify the permission enlargement problem. For example, whether to contain the data of a key in the map
3. Whether a confidential field has been desensitized
 ### Speakers: 
 <img src="images/speaker/1214.png" width="200" /><br>Shuai Han: Bytedance - Senior R&D engineer of Big Data Computing Engine Group, with years of big data r&d experience. Familiar with SparkSQL, Hive, Calcite, Druid and other big data components.

 <img src="images/speaker/1214_2.png" width="200" /><br>Ke Sun: Bytedance - Senior R&D engineer of Big Data Computing Engine Group, responsible for unified SQL query service, Hive metadata, permission service and big data security compliance, with years of experience in big data research and development. Familiar with various big data components such as SparkSQL, Hive, Hudi, Parquet and Calcite.

 