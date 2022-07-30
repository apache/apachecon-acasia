---
title: "Make Apache Pulsar as Lakehouse: Introducing the Lakehouse Tiered Storage Integration for Pulsar"
date: "2022-07-31T14:10:00"
track: "messaging"
room: "A"
presenters: "Hang Chen"
stype: "Chinese Session"
---
Apache Pulsar is a message bus to cache data and decouples between different systems. To support long-term topic data storage, we introduced tiered storage to offload cold data into tiered storage such as GCS, S3, HDFS, etc. However, current offloaded data is organized by Pulsar and is not open-format, which is a raw data format; only Pulsar can access the data. It is hard to integrate with other significant data components, such as Presto, Flink SQL, and Spark SQL.

To solve the problems we faced, we introduced Lakehouse storage lib to manage offload data and integrate with the current topic cold data offload mechanism. With Lakehouse storage lib support, we can use all features provided by Lakehouse, such as transaction support, Schema enforcement, governance, and BI support.

We will read data from BookKeeper or tiered storage according to data location for streaming data reading. Due to Lakehouse's open storage format, we can support all kinds of ecosystems sustained by Lakehouse to read data.

To support streaming offload and make the offloading mechanism more scalable, we introduce an offload by reader mechanism to read data from the topic and write into tiered storage.

Moreover, we also can provide a compaction service backend by offloader and act the topic as a table. Each update operation for a key is transformed as an upsert action to the table.
 ### Speakers: 
 <img src="images/speaker/1188.png" width="200" /><br>Hang Chen: StreamNative, Engineer, Hang Chen is an engineer from StreamNative, and he is an Apache Pulsar PMC member. He focuses on storage modules for Pulsar, including BookKeeper, tiered storage, and lakehouse.

 