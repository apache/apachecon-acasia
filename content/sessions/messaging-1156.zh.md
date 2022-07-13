---
title: "深入研究 Pulsar 中的消息分块"
date: "2022-07-30T16:10:00"
track: "messaging"
room: "A"
presenters: "杨子棵"
stype: "中文演讲"
---
Apache Pulsar 与所有消息系统一样，会对发送到 broker 的每条消息限制大小。这可以防止每条消息的负载超过 broker 中设置的 `maxMessageSize`。

然而，在诸如图像处理和音频处理等应用场景中，很多用户需要 Pulsar 客户端向 broker 发送大消息。因此，Pulsar 在发送大消息时，除了增加 `maxMessageSize` 的值外，也提供了消息分块功能来支持。通过消息分块，生产者可以根据 `maxMessageSize` 将大消息拆分为多个块，并将每个块作为普通消息发送给 broker。消费者之后会将这些块消息组合回原始消息。
在这篇演讲中，杨子棵将解释消息分块的概念，深入探讨其实现，并分享此功能的最佳实践.
 ### Speakers: 
 <img src="images/speaker/1156.png" width="200" /><br>Zike Yang：StreamNative 软件工程师，Apache Pulsar Committer。

 