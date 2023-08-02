---
title: "APACHE LINKIS data processing practice in lake-silo architecture"
date: "2023-08-18T15:00:00" 
track: "datalake"
presenters: "王华磊"
stype: "Chinese Session"
---
It mainly shares how Postal Savings Bank, as a large state-owned bank, solves practical problems with Linkis under the integrated framework of lake and warehouse, and its future development prospects. The outline of the agenda is as follows:
1. Big Data Lake warehouse integrated structure of PSBC
2. Problems faced in implementation
2.1 There are many technical components and complex maintenance of the basic environment
2.2 Technology is difficult, and the technical threshold of data development is high
2.3 In the streaming and Batch integrated architecture, component versions are upgraded quickly
2.4 Metadata communication between different computing engines fails

1. Specific practice of Apache Linkis
3.1 Implements the underlying interconnection of computing components and provides unified interface invocation
3.2 Pure sql development is preferred
3.3 Support multiple versions of the same component
3.4 Using the Hive Catalog in a Unified Manner to provide a unified Metadata interface

1. Participate in Apache linkis community construction
4.1 Data Access Layer Added Postgresql support
4.2 File Storage S3 support
4.3 Containerized Deployment Practices

1. Future technology planning
5.1 Strengthen the management function of Iceberg and other data lake technologies based on Linkis
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230522/1522539410.jpg" width="200" /><br>Wang Hualei: Postal Savings Bank of China, Deputy chief engineer, Years of experience in data architecture in banking big data field, open source enthusiast, Linkis community contributor.
 <br><br>