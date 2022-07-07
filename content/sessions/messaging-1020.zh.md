---
title: "朝着一个没有zookeeper的Pulsar前进"
date: "2022-07-30T14:10:00"
track: "messaging"
room: "A"
presenters: "David Kjerrumgaard"
stype: "英文演讲"
---
从2.10版本开始，Apache ZooKeeper的依赖已经被消除，取而代之的是一个可插拔的框架，它使您能够通过根据您的部署环境利用替代的元数据和协调系统来减少Apache Pulsar的基础设施占用。


在这次演讲中，我将带领您完成利用Kubernetes内部运行的现有etcd服务作为Pulsar元数据存储所需的步骤。因此完全不需要运行ZooKeeper，只留下一个没有ZooKeeper的Pulsar。
 ### Speakers: 
 <img src="images/speaker/1020.png" width="200" /><br>David Kjerrumgaard: StreamNative, 开发人员主, David是Apache Pulsar项目的提交人，也是《Pulsar in Action》的作者和《Practical Hive》的合著者。他目前担任StreamNative的开发人员倡导者，专注于通过教育和推广加强Apache Pulsar社区。在此之前，他是Splunk消息团队的首席软件工程师，以及两家大数据初创公司的解决方案总监;Streamlio Hortonworks。

 