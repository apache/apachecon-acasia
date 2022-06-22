---
title: "深入研究脉冲星信息分块"
date: "" 
track: "messaging"
presenters: "Zike Yang"
stype: "中文演讲"
---
与所有消息系统一样，Apache Pulsar对发送给代理的每条消息都施加了大小限制。它防止每个消息的有效负载超过pulsar代理中设置的最大消息大小。然而，许多用户需要Pulsar客户端向代理发送大型消息，用于图像处理和音频处理等用例。

因此，Pulsar没有增加最大消息大小的配置，而是提供了消息分块特性，以支持发送大消息。使用消息分块，生产者可以根据最大消息大小配置将一个大消息分成多个块，并将每个块作为普通消息发送给代理。然后，使用者将这些块合并回原始消息。

在这次演讲中，杨子科将解释消息分块的概念，深入研究它的实现，并分享这一特性的最佳实践。
 ### Speakers: 
 <img src="images/speaker/1156.png" width="200" /><br>Zike Yang: StreamNative, 软件工程师, Zike Yang是Streamnative的软件工程师。他也是阿帕奇脉冲星的提交者。

 