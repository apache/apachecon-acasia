---
title: "TableView简介：Pulsar的数据库表抽象"
date: "2022-07-31T13:30:00"
track: "messaging"
room: "A"
presenters: "David Kjerrumgaard"
stype: "英文演讲"
---
在许多场景中，应用程序使用Pulsar消费者或reader从主题中获取所有更新，并使用已接收消息的每个键的最新值构建映射。

新的TableView消费者可以直接在Pulsar客户端API中提供对这种访问模式的支持，并将手动构建这种本地缓存的复杂性做了封装。在这次演讲中，我们将演示如何通过一个简单的应用程序来使用新的TableView消费者，并讨论使用TableView消费者的最佳实践和模式。
 ### Speakers: 
 <img src="images/speaker/1021.png" width="200" /><br>David Kjerrumgaard：StreamNative，布道师，David是Apache Pulsar Committer，也是《Pulsar in Action》的作者和《Practical Hive》的合著者。他目前担任StreamNative布道师，专注于通过教育来建设Apache Pulsar社区。在此之前，他是Splunk消息团队的首席软件工程师，以及两家大数据初创公司Streamlio和Hortonworks的解决方案总监。

 