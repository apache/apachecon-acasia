---
title: "深入了解Kafka中的复制协议"
date:  "2023-08-18T16:30:00" 
track: "messaging"
presenters: "Luke Chen"
stype: "中文演讲"
---
作为消息传递系统，数据持久性非常重要。当集群中的某个服务器发生故障时，复制确保自动故障转移到其他副本，因此在出现故障时消息仍然可用。在Apache Kafka中，复制协议不仅用于实现持久性，还用于实现高吞吐量。在这次演讲中，我们将深入探讨Kafka内部的复制协议是如何工作的。我们还将解释这种设计的优点和缺点。此外，我们还将介绍Kafka中的另一种复制协议，用于KRaft控制器(即基于仲裁的方式)。

通过这次演讲，听众可以重新思考这些复制协议，也许其中的一些想法可以带到其他分布式系统项目中。希望它也能帮助读者更多地了解Apache Kafka。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230602/1539258830.jpg" width="200" /><br>Luke Chen: RedHat, 高级软件工程师, 我是RedHat的一名高级软件工程师，致力于在云上运行Apache Kafka的产品。我也是Apache Kafka的提交者和PMC成员。我为Apache Kafka贡献了3年多的时间。
 <br><br>