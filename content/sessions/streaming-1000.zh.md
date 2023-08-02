---
title: "Apache Flink中Scala API的状态"
date: "2023-08-19T15:45:00" 
track: "streaming"
presenters: "alexey"
stype: "英文演讲"
---
作为编写Flink新作业的Scala开发人员，您希望使用最新的Scala 3版本，而不是Flink编译时使用的版本。对Scala 2.13和Scala 3的支持直到Flink 1.15出来才真正成为可能。在这次演讲中，我们将回顾在1.15版本之前，Scala API是如何在Apache Flink中实现的，以及该版本中有哪些变化。Apache Flink选择了完全相反的方式，使Scala开发人员能够使用任何Scala版本，而不是Apache Spark项目，这本身就是一个有趣的讨论。

在这次演讲中，我们将通过SBT示例项目来使用Scala 3构建Flink作业。我们将了解当前Flink Java API的Scala包装器的社区选项以及与之相关的挑战。结果，我们将看到在Flink作业中使用Scala比用Java API编写流作业要方便得多。Scala CLI的介绍使Scala作业的整个打包体验成为一种纯粹的乐趣。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230607/1640066470.jpg" width="200" /><br>阿列克谢: Ververica, 解决方案架构师, 我是一名解决方案架构师，在过去的6年里一直致力于数据解决方案和产品。在Ververica，我专注于支持客户解决他们在使用Apache Flink采用数据流处理时遇到的挑战。在我之前的项目和公司中，我开发了不同的系统，如数据湖、数据集成和数据虚拟化层。我还花了多年时间为投资银行开发数据服务，包括货币交易软件。在我的业余时间，我也为各种开源项目做出贡献，或者自己开始做一些有趣的事情。我的爱好是天文、音乐和体育。
 <br><br>