---
title: "避免失败：Pulsar 自动集群故障转移功能详解"
date: "2022-07-31T13:30:00"
track: "messaging"
room: "B"
presenters: "David Kjerrumgaard"
stype: "英文演讲"
---
开发高可用性的应用程序，需要的不仅仅是利用软件栈中的容错服务（如Apache Pulsar），还需要立即进行故障检测和解决，包括在数据中心发生故障时进行内置故障转移。

到目前为止，Pulsar客户端只能与单个Pulsar集群交互，无法检测到集群级故障事件并对其做出响应。在集群完全失败的情况下，这些客户端不能自动将其消息重新路由到辅助/备用集群。

随着Pulsar 2.10的发布，这种急需的自动化集群故障转移功能已被添加到Pulsar客户端库中。在本次演讲中，我将带你了解在应用代码中需要进行哪些更改才能利用这个新功能。
### Speakers: 
<img src="images/speaker/1019.png" width="200" /><br>David Kjerrumgaard：StreamNative，布道师，David是Apache Pulsar Committer，也是《Pulsar in Action》的作者和《Practical Hive》的合著者。他目前担任StreamNative布道师，专注于通过教育来建设Apache Pulsar社区。在此之前，他是Splunk消息团队的首席软件工程师，以及两家大数据初创公司Streamlio和Hortonworks的解决方案总监。

 