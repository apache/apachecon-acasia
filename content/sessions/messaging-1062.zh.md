---
title: "移动云MQTT-RocketMQ消息队列的海量数据流转实践"
date: "2023-08-20T17:15:00" 
track: "messaging"
presenters: "庄兴旺"
stype: "中文演讲"
---
5G时代，万物互联，越来越多的企业期望通过已有的数据分析业务中台对物联网数据做进一步计算处理。目前，大量的企业的业务中台架构都通过引入消息队列RocketMQ来进行削峰、解耦和消息通知。那么能否通过复用RocketMQ完成数据从海量的物联网设备端流转到数据分析业务中台（即消息队列RocketMQ）呢？因此，我将从以下几个方面介绍一下MQTT-RocketMQ Connect架构，可以实现MQTT和RocketMQ消息队列之间的海量数据流转：
1、背景
2、MQTT-RocketMQ Connect架构设计
3、MQTT-RocketMQ Connect的容器化实践
4、MQTT-RocketMQ Connect在移动云上的海量数据流转实践
5、总结与展望
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230605/1641346040.jpg" width="200" /><br>庄兴旺: 中移（苏州）软件技术有限公司, 助理软件开发工程师, 中国移动云能力中心Iaas产品部rpc产品组助理研发工程师，主要负责移动云消息队列RocketMQ和MQTT的设计与研发工作
 <br><br>