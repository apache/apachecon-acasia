---
title: "使用Sharding Sphere来进一步扩展Amazon Aurora的读写能力"
date: "" 
track: "middleware"
presenters: "马丽丽"
stype: "中文演讲"
---
除性能、可用性以外，数据库的可扩展性也是用户在进行数据库选型时或者随着业务扩张数据量不停增长需要考虑的方面。以亚马逊云科技自研的关系数据库Amazon Aurora为例，它在存储扩展、读节点水平扩展、全球数据库扩展、以及单节点的纵向扩展方面都有良好的支持。在写节点的水平扩展上，Aurora现在支持最多4个写节点，在用户写的并发数比较多时，用户需要进行数据库中间件的选型。本次分享会介绍如何结合Apache ShardingSphere来进一步扩展Amazon Aurora的写扩展的能力，并会为听众在进行数据库中间件选型基于什么角度考虑提供一个参考。
本次演讲会涵盖：
1. Amazon Aurora和ShardingSphere基本介绍
2. ShardingSphereProxy对Amazon Aurora动态分片的支持
3. ShardingSphereProxy对Amazon Aurora读写分离的支持
4. ShardingSphereProxy对Amazon Aurora表Join的支持
5. ShardingSphereProxy对Amazon AuroraFailover对支持
6. ShardingSphereJDBC与Amazon Aurora的结合
 ### Speakers: 
 <img src="images/speaker/1200.png" width="200" /><br>马丽丽: 亚马逊云科技, 数据库专家架构师, 马丽丽，亚马逊云科技数据库专家架构师，十几年来一直在数据库领域进行研究和产品创新：从IBM DB2、到 MPP 并行数据仓库Greenplum、到计算和存储解耦的 Apache HAWQ、再到云上数据库 Amazon Aurora 和 ElastiCache。她在国际会议上发表多篇数据库方面学术论文（SIGMOD, GCC, SKG, PDCAT），并拥有多项国际专利。她是Apache HAWQ 项目PMC成员，也是Greenplum早期团队成员。她曾于2017年DTCC大会上分享过“Apache HAWQ 2.X最新技术解密”，在Greenplum社区分享过Greenplum的PL/Container实现，以及在亚马逊云科技的平台分享过Amazon Aurora Serverless以及MemoryDB等话题。
 