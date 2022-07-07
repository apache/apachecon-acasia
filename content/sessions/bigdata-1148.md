---
title: "Hadoop Vectored IO: your data just got faster!"
date: "2022-07-30T16:10:00"
track: "bigdata"
room: "A"
presenters: "Mukund Thakur"
stype: "English Session"
---
Since 2006 the world of big data has moved from terabytes to hundreds of petabytes, from local clusters to remote cloud storage, yet the original Apache Hadoop posix-based file APIs have barely changed.

It is wonderful that these APIs have worked so well, but we can do a lot better with remote object stores, by providing new operations which suit them better, targeted at columnar data libraries such as ORC and Spark. Only a few libraries need to migrate to these APIs for significant speedups of all big data applications.

This talk introduces a new Hadoop Filesystem API called "vectored read", coming in Hadoop 3.4. An extension of the classic FSDataInputStream it is automatically offered by all filesystem clients.
The S3A connector is the first object store to provide a custom implementation, reading different blocks of data in parallel. In Apache Hive benchmarks with a modified ORC library, we saw a 2x speedup compared to using the classic s3a connector through the Posix APIs.

We will introduce the API spec, the S3A implementation and the benchmarks, and show how to use it in your own applications. We will also cover our ongoing work on providing similar speedups with other object stores, and use of the API in other applications.
 ### Speakers: 
 <img src="images/speaker/1148.png" width="200" /><br>Mukund Thakur: Apache APISIX, Cloudera, I am an active committer of Apache Hadoop project currently working at Cloudera focusing on Cloud Storage Connectors (aws, azure and gcs) and Ranger Authorization. 
I have total experience of 8 years designing and developing large scale distributed systems. Apart from software development, I love doing yoga and hiking in the Himalayas.

 