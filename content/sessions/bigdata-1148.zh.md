---
title: "Hadoop矢量IO:你的数据变快了!"
date: "" 
track: "bigdata"
presenters: "Mukund Thakur"
stype: "英文演讲"
---
自2006年以来，大数据的世界已经从tb级转移到数百pb级，从本地集群转移到远程云存储，然而最初的基于Apache Hadoop posix的文件api几乎没有改变。

这些api工作得很好，这很好，但是通过提供更适合远程对象存储的新操作(针对ORC和Spark等柱状数据库)，我们可以在远程对象存储方面做得更好。只有少数库需要迁移到这些api来显著加快所有大数据应用程序的速度。

本次演讲将介绍Hadoop 3.4中新的Hadoop文件系统API，称为“矢量读取”。经典FSDataInputStream的扩展，它由所有文件系统客户端自动提供。
S3A连接器是第一个提供自定义实现的对象存储，可以并行读取不同的数据块。在修改ORC库的Apache Hive基准测试中，我们发现与通过Posix api使用经典的s3a连接器相比，速度提高了2倍。

我们将介绍API规范、S3A实现和基准，并展示如何在您自己的应用程序中使用它。我们还将介绍我们正在进行的工作，在其他对象存储中提供类似的加速，以及在其他应用程序中使用API。
 ### Speakers: 
 <img src="images/speaker/1148.png" width="200" /><br>Mukund Thakur: Apache APISIX, Cloudera, 我是Apache Hadoop项目的活跃提交者，目前在Cloudera工作，专注于云存储连接器(aws、azure和gcs)和Ranger Authorization。
我有8年的大型分布式系统设计和开发经验。除了软件开发，我还喜欢做瑜伽和在喜马拉雅山徒步旅行。

 