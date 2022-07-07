---
title: "TableView简介:Pulsar的数据库表抽象"
date: "2022-07-31T13:30:00"
track: "messaging"
room: "A"
presenters: "David Kjerrumgaard"
stype: "英文演讲"
---
在许多用例中，应用程序使用Pulsar消费者或读取器从主题中获取所有更新，并使用接收到的消息的每个键的最新值构建一个映射。

新的TableView消费者直接在Pulsar客户端API本身中提供了对这种访问模式的支持，并封装了手动构建这种本地缓存的复杂性。在这次演讲中，我们将演示如何使用一个简单的应用程序来使用新的TableView consumer，并讨论使用TableView consumer的最佳实践和模式。
 ### Speakers: 
 <img src="images/speaker/1021.png" width="200" /><br>David Kjerrumgaard: StreamNative, 开发人员主, David是Apache Pulsar项目的提交人，也是《Pulsar in Action》的作者和《Practical Hive》的合著者。他目前担任StreamNative的开发人员倡导者，专注于通过教育和推广加强Apache Pulsar社区。在此之前，他是Splunk消息团队的首席软件工程师，以及两家大数据初创公司的解决方案总监;Streamlio Hortonworks。

 