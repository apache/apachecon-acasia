---
title: "基于 Apache Calcite 的多引擎虚拟列技术"
date: "2022-07-31T16:10:00"
track: "bigdata"
room: "B"
presenters: "谢佳君"
stype: "中文演讲"
---
在数据分析领域，同一个业务指标可能需要针对不同的引擎写不同的SQL，编写的人需要处理不同引擎的语法差异，学习和使用成本较高。当指标口径变更时，需要通知到所有使用该指标的业务方进行相应的变更，沟通成本较高。字节跳动基于Apache Calcite设计并实现了多引擎的虚拟列，来解决这一问题。
字节跳动基于 Apache Calcite进行了深度定制，项目名称为 ByteQuery。ByteQuery 基于 Calcite 设计并实现了 ANSI SQL 2011 标准语法，对外提供跨引擎的统一 OLAP 查询服务。ByteQuery 在 Calcite 的基础上扩展了虚拟列的 DDL 语法，比如add/drop virtual columns语法；ByteQuery 针对不同 OLAP 引擎，自动完成虚拟列的逻辑改写和引擎对接，降低用户使用成本。通过虚拟列技术，业务方只需要将常用的业务指标保存为虚拟列即可和普通列一样使用。这种方案有着如下的优点:
- 虚拟列不占用额外的存储空间，降低存储成本
- 无需用户了解不同引擎的语法差异，ByteQuery 自动适配多引擎，降低使用成本
- 无需周知指标的使用方，方便指标统一管理，降低指标维护成本
- 相比于 View，提供 Hive 实体Table 一致的使用体验
- 可以在数据加密/脱敏等多种应用场景落地，例如明文字段配置高权限级别，添加脱敏的虚拟列字段并配置低权限级别，提供灵活的使用方式
 ### Speakers: 
 <img src="images/speaker/1187.png" width="200" /><br>谢佳君: 字节跳动, 高级研发工程师, 字节跳动数据引擎部门高级研发工程师，专注于SQL的解析优化，热爱开源，是Apache Calcite的contributor之一。

 