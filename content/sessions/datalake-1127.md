---
title: "Bytedance based on the Parquet format of cost reduction and efficiency practice"
date: "2023-08-18T16:15:00" 
track: "datalake"
presenters: "徐庆,王恩策"
stype: "Chinese Session"
---
Bytedance offline data warehouse uses Parquet format for data storage by default, but in the process of business use, we have encountered problems related to too many small files and high data storage cost.
To solve the problem of too many small files, the existing technical solution is generally to read multiple Parquet small files through Spark, and then re-output these data and merge them into one or more large files. For the storage cost problem, only the partition level row TTL is available for offline stores. If you need to delete the large number of detail field data that is no longer used in the partition (column level TTL), you need to use Spark to read the data and set the field to NULL overwrite mode. 
Whether it is small file merging or column level TTL, there is a lot of overwriting of Parquet data files. Because Parquet format has special coding rules, it needs to go through a series of operations such as (de-serialization), (decompression), (de-encoding), etc., in order to achieve the read and write of the data in Parquet. In this process, operations such as codec and decompression are CPU-intensive and consume a lot of computing resources. In order to improve the efficiency of file overwriting in Parquet format, we studied the definition of Parquet file format in depth and adopted the binary copy method to optimize data overwriting operations, skipping redundant operations such as codec in common overwriting, which greatly improved file overwriting efficiency compared with traditional methods. Performance is 10+ times that of normal overwrite.
To improve ease of use, we also provide new SQL syntax to enable users to easily complete small file merging and column level TTL.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230616/1450066050.jpg" width="200" /><br>Xu Qing: bytedance, Senior R&D Engineer of Volcano Engine LAS platform. He has been engaged in the research and development of Hive Metastore, SparkSQL, Hudi and other big data-related components for many years.
 <br><br><img src="https://img.bagevent.com/resource/20230616/1521102550.jpeg" width="200" /><br>Wang Ence: bytedance, Senior R&D Engineer of Volcano Engine LAS platform, responsible for the design and development of Bytedance big data distributed computing engine, helping the company to mine high-value information from massive data
 <br><br>