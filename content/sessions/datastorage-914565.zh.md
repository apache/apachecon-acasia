---
title: "适用于 Hadoop 集群的小型文件嗅探系统"
date: "2025-07-25T17:15:00"
track: "datastorage"
presenters: "Miao Wang"
stype: "英文演讲"
room: "万寿山会议室"
---

HDFS（Hadoop 分布式文件系统）在管理大量小文件时经常会遇到性能严重下降的问题。通过 Namenode 服务扫描所有文件以查找小文件会变得非常耗时，并给 Namenodes 增加额外负担。关于如何在不查询Namenode的情况下以省时高效的方式识别HDFS中的小文件热点，目前还缺乏研究。在本环节中，演讲者旨在介绍一种大数据系统，通过解析在Namenode上定期生成的文件系统映像（FSImage）来识别HDFS中的小文件。该系统允许 Hadoop 集群管理员在不影响 Hadoop 集群正常运行的情况下实时监控和识别小文件。此外，它还可用作 Hive 数据仓库中定位小文件热点表的工具。

### 讲师:


<img src="https://sessionize.com/image/aee1-400o400o1-JZ2CnJbAPD5PN5NLnF28Yk.jpg" width="200" /><br/>

Miao Wang: 中国邮政储蓄银行，数据工程师

Miao 拥有北京理工大学工程学士学位和康考迪亚大学电子与计算机工程硕士学位。目前，他在中国邮政储蓄银行担任数据工程师。他的兴趣横跨分布式系统、数据湖和大数据。此外，他还是 Apache Iceberg 等多个开源项目的贡献者。