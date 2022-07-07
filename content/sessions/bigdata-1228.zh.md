---
title: "Apache Ozone:高效地处理文件和对象的多协议感知系统"
date: "2022-07-29T14:10:00"
track: "bigdata"
room: "B"
presenters: "Rakesh Radhakrishnan, Mukul Kumar Singh"
stype: "英文演讲"
---
Apache Ozone是一个分布式、可伸缩的高性能对象存储，可以扩展到数十亿个不同大小的对象。Apache Ozone对象存储最近实现了一个多协议感知桶特性，其中一个Apache Ozone集群同时具备Hadoop核心文件系统(“HCFS”)和对象存储(如Amazon S3)功能。在这次演讲中，我们将深入探讨Ozone中统一和可扩展的架构设计，它表示目录、文件、对象和桶，允许分层文件系统和对象存储协议之间的互操作性。基本上，这种多协议能力对主要面向文件系统类工作负载的系统很有吸引力，但希望添加一些对象存储特性支持。例如，用户可以使用文件系统API将数据摄取到Ozone中，同样的数据也可以通过Ozone S3 API(Amazon S3实现)访问。这可能会提高自带对象存储的用户平台的效率。此外，存储在Ozone中的数据可用于不同的用例共享，消除了数据重复的需要，从而降低了风险，优化了资源的利用。
最后，我们还将讨论利用这种新设计引入基于散列的锁机制的路线图，通过替换全局桶级锁，允许更多并发元数据名称空间操作(混合写和读)。
 ### Speakers: 
 <img src="images/speaker/1228.png" width="200" /><br>Rakesh Radhakrishnan: Cloudera, 资深软件工程师，Apache Ozone, Hadoop, ZooKeeper项目的提交者和PMC，主要专注于开源大数据技术。Rakesh目前在Cloudera工作，并积极为Apache Ozone项目做出贡献。他拥有超过15年的大型分布式软件平台设计和开发经验。在加入Cloudera之前，他曾担任Intel Corporation的大数据软件工程师。

 <img src="images/speaker/1228_2.png" width="200" /><br>Mukul Kumar Singh: Cloudera, 高级工程经理, 目前在Cloudera工作，领导着Apache Ozone和Apache HDFS的存储团队。他还从事存储系统和文件系统工作13年，担任过各种角色，包括开源贡献者、PMC成员、研究员和软件开发人员。他还曾与Nimble Storage和NetApp合作，分别开发了WAFL和CASL文件系统。他毕业于卡耐基梅隆大学，在那里他的论文是关于一个文件系统的叠瓦式磁记录（SMR）盘。

 