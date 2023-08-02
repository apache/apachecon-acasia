---
title: "流式Apache Kudu在Apache Flink"
date: "2023-08-18T15:45:00" 
track: "streaming"
presenters: "Wei Chen"
stype: "英文演讲"
---
到目前为止，Apache Kudu不支持CDC，因此在与Apache Flink集成时，无法像其他支持CDC的数据源那样以流方式从它读取数据。为了克服这个问题，Apache Flink源连接器已经构建，以释放Apache Kudu以连续和增量的方式流式传输数据的能力。在本次演讲中，我们将讨论和分享该解决方案的详细设计和实现。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230610/1630271000.jpg" width="200" /><br>魏陈: 易趣, 软件工程师, Wei专注于通过利用大数据和流处理技术来增强eBay的通知平台。他也是一名技术博客作者，并积极参与开源社区。他在上海交通大学获得学士和硕士学位。
 <br><br>