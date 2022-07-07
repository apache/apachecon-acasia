---
title: "Multi-engine virtual column technology based on Apache Calcite"
date: "2022-07-31T16:10:00"
track: "bigdata"
room: "B"
presenters: "谢佳君"
stype: "Chinese Session"
---
In the field of data analysis, the same business indicator may need to write different SQL for different engines, and the writer needs to deal with the syntax differences of different engines, which costs a lot to learn and use. When an indicator caliber is changed, it is necessary to notify all the service providers using the indicator to make the change. Therefore, the communication cost is high. Bytedance solves this problem by designing and implementing multi-engine virtual columns based on Apache Calcite.
Bytedance is deeply customized based on Apache Calcite, and the project name is ByteQuery. ByteQuery designs and implements the ANSI SQL 2011 standard syntax based on Calcite to provide unified OLAP query services across engines. ByteQuery extends Calcite's DDL syntax for virtual columns, such as add/drop Virtual columns. ByteQuery automatically completes logical rewriting of virtual columns and engine interconnection for different OLAP engines, reducing user costs. With the virtual column technology, the business side only needs to save common service indicators as virtual columns to be used in the same way as ordinary columns. This scheme has the following advantages:
- Virtual columns do not occupy extra storage space, reducing storage costs
- ByteQuery automatically ADAPTS to multiple engines without requiring users to understand syntax differences between different engines
- No need to know the user of indicators, convenient unified management of indicators, reduce the maintenance cost of indicators
- Provides consistent use experience of Hive entity tables compared with View
- The system can be implemented in various application scenarios such as data encryption and desensitization. For example, a high permission level can be set for plaintext fields, and a low permission level can be set for desensitized virtual column fields, providing flexible usage modes
 ### Speakers: 
 <img src="images/speaker/1187.png" width="200" /><br>Jiajun Xie: Bytes Dance, Senior R&d Engineer, Senior R&D engineer of Bytedance Data Engine Department, focusing on SQL parsing and optimization, loving open source, and being one of Contributor for Apache Calcite.

 