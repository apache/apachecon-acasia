---
title: "Apache Ozone: Multi-Protocol aware system handles both Files and Objects efficiently"
date: "2022-07-29T14:10:00"
track: "bigdata"
room: "B"
presenters: "Rakesh Radhakrishnan, Mukul Kumar Singh"
stype: "English Session"
---
Apache Ozone is a distributed, scalable and a high performance object store that can scale to billions of objects of varying sizes. Apache Ozone object store recently implemented a multi-protocol aware bucket feature, where a single Ozone cluster with the capabilities of both Hadoop Core File System (“HCFS”) and Object Store (like Amazon S3) features. In this talk we will deep dive into the unified and extensible architectural design in Ozone representing directories, files, objects and buckets that allows interoperability between hierarchical file system and object store protocol. Basically, this multi-protocol capability will be attractive to systems that are primarily oriented towards File System - like workloads, but would like to add some Object Store feature support. For example, a user can ingest data into Ozone using FileSystem API, and the same data can be accessed via Ozone S3 API(Amazon S3 implementation). This would potentially improve the efficiency of the user platform with on-prem Object Store. Furthermore, data stored in Ozone can be shared for various use cases, eliminating the need for data duplication, which in turn reduces risk and optimises resource utilisation. 
Finally, we will also talk about the roadmap to leverage this new design to introduce a hash based locking mechanism to allow more concurrent metadata namespace operations(mixture of write and read) by replacing the global bucket level lock.
 ### Speakers: 
 <img src="images/speaker/1228.png" width="200" /><br>Rakesh Radhakrishnan: Cloudera Private Limited, Staff Software Engineer, Rakesh Radhakrishnan is a committer and a PMC in Apache Ozone, Hadoop, ZooKeeper projects and primarily focusing on open source big data technologies. Rakesh is currently working at Cloudera and actively contributing on the Apache Ozone project. He has more than 15 years of experience in large scale Distributed Software Platforms design and development. Prior to joining Cloudera, he worked as a Big Data Software Engineer in Intel Corporation.

 <img src="images/speaker/1228_2.png" width="200" /><br>Mukul Kumar Singh: Cloudera Private Limited, Senior Engineering Manager, Mukul is currently working with Cloudera where he is leading the Storage team working on both Apache Ozone and Apache HDFS. He has also been working on Storage Systems and File Systems for 13 years and has played various roles as open source contributor, PMC member, researcher and a software developer. He also has worked with Nimble Storage and NetApp and worked on WAFL and CASL file systems respectively. He graduated from Carnegie Mellon University, where his thesis was on a file system for Shingled Magnetic recording disks.

 