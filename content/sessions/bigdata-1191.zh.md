---
title: "捕获作业的每个线程统计信息——线程级IOStatistics——HADOOP-17461"
date: "2022-07-30T13:30:00"
track: "bigdata"
room: "A"
presenters: "Mehakmeet Singh"
stype: "英文演讲"
---
为了有效地报告各个工作线程的iotstatistics，我们需要IO组件更新的线程级上下文(HADOOP-17461)。

IOStatistics是一个统计捕获API，由Steve Loughran创建，包括计数器，最大，分钟，平均值，和测量文件系统和流查看。这些统计数据比我们以前在Hadoop世界中获得的更详细的作业或操作信息，可以用于确定文件系统某些区域所需的性能改进。

在S3A和ABFS流中的实现包括创建一个IOStatisticsSnapshot WeakReferenceTreeMap，它将存储一个特定的线程ID作为键，并将IOstatistics实例的快照作为值。只在流关闭后聚合它，然后设置回快照。这将有助于在流关闭后获得特定线程工作的IOStatistics。

这将提供一个更好的视图来了解Hive，并在大数据空间中触发任务，在这个空间中，任务的失败并不一定会以一组特定的统计数据来更好地查看和调试问题。拥有每个线程级别的统计数据还有助于更好地了解处理大数据的此类作业，并为我们提供了一种在线程级别更好地理解问题的好方法。
 ### Speakers: 
 <img src="images/speaker/1191.png" width="200" /><br>Mehakmeet Singh: Cloudera, 软件工程师2, 我的名字叫Mehakmeet Singh，拥有计算机科学技术学士学位，并在Cloudera获得实习+ FTE，这是我大学毕业后在这个行业的第一次创业。在这里工作两年后，我为开源社区做出了很多贡献，主要是通过Cloud-Connectors项目，我也是Cloudera的一部分。我的工作开始于在Hadoop的Azure Blob文件系统(ABFS)中收集简单的计数器，在AWS S3A中实现客户端加密，在ABFS中提供一种更好的方式来缓冲数据，以避免出现OOM错误，然后进行IOStatistics的线程级收集。我在这个领域还很年轻，但是我的公司有很多同事的支持，帮助我接触Apache社区并做出贡献。这将是我众多ApacheCon中的第一个，也是到目前为止我最大的演讲平台，但你必须从某处开始，并随着这些经验的增长而成长，我很高兴成为其中的一员，并期待其他人的项目。

 