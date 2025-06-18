---
title: "Apache Polaris（孵化中）和 Apache XTable：统一 Iceberg、Hudi 和其他表格式"
date: "2025-07-26T17:15:00"
room:  "万春厅"
track: "datalake"
presenters: "Eric Maynard"
stype: "英文演讲"
---

Apache Polaris（孵化中）实现了 Apache Iceberg REST 目录规范，并允许用户管理 Iceberg 表、视图和其他相关元数据。基于角色的访问控制控制哪些用户可以访问哪些数据，Polaris 支持将策略附加到表，以便对数据进行分类并配置表维护。

与 Apache XTable 的新集成有望将相同的功能扩展到非 Iceberg 表。Polaris 最近推出了“通用表”——允许用户在 Polaris 中管理他们的 Apache Hudi 表以及由 Apache Kafka 或其他系统支持的表。借助 XTable，客户现在可以连接到 Polaris 并读取最初用 Iceberg 编写的数据，就像它是用 Hudi 编写的一样，而无需考虑表格式。

本次演讲将概述 Polaris 中新的通用表和转换功能，如何配置 XTable 以增强转换，并简要回顾集成的设计和实现。

### 讲师:

<img src="https://sessionize.com/image/d65d-400o400o1-LvXU1jeMwf7eRJ4iZsGDwd.png" width="200" /><br/>

Eric Maynard: 数据互操作性 @ Snowflake

Eric Maynard 是 Snowflake 的一名工程师，致力于 Apache Iceberg、Apache Polaris（孵化）以及格式之间（元）数据的转换。