---
title: "What's new in the recent and upcoming HBase releases"
date: "2023-08-18T13:30:00" 
track: "datastorage"
presenters: "张铎"
stype: "Chinese Session"
---
Apache HBase™ is the Hadoop database, a distributed, scalable, big data store.

The HBase community is preparing new major release 3.0.0 and new minor release 2.6.0, The hbase community is preparing new major release 3.0.0 and new minor release 2.6.0, with some brand new features. In this presentation, we will introduce these new features, about how they benefit our users and how we implement them in HBase. Like:

- OpenTelemetry Tracing: HBASE-22120, HBASE-26419
- The new region replication framework: HBASE-26233
- Move the logging framework from log4j to log4j2: HBASE-19577
- Cloud native supports
- Introduce StoreFileTracker for better object storage support: HBASE-26067, HBASE-26584
- K8s deployment support: HBASE-27827, in progress
- No persistent data on zookeeper
- Move meta location off zookeeper: HBASE-26193
- Table based replication queue storage: HBASE-27109
- File system based replication peer storage: HBASE-27110
- redeploy cluster with only root directory on object storage: HBASE-26245
- Future?
- HBase on Ozone
- WAL on Ozone: HBASE-27740
- Fully cloud native, no other self deployed services other than HBase itself
- New WAL implementation: BookKeeper? Embedded WAL service?
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230603/2240000820.jpg" width="200" /><br>Zhang Duo: Strategic data, Chief architect, Tsinghua University, Department of Computer Science and Technology bachelor's degree, long engaged in open source software development and maintenance. Since 2015, he has been a member and chairman of ApacheHBase project Committer, PMC. He will become a Member of the Apache Software Foundation in 2020. In 2018, it ranked third in the number of contributions among the nearly 7,000 committers of the Apache Software Foundation worldwide. He served as chairman of the Open Source Committee of Xiaomi and was responsible for the planning and promotion of the overall open source work of Xiaomi. He is currently the Chief Architect at Divine Data.
 <br><br>