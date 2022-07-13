---
title: "Apache Linkis 数据处理实践"
date: "2022-07-31T14:10:00"
track: "workflowdatagovernance"
presenters: "李孟"
stype: "中文演讲"
---
Linkis背景介绍
Linkis 在上层应用和底层引擎之间构建了一层计算中间件。通过使用Linkis 提供的REST/WebSocket/JDBC 等标准接口，上层应用可以方便地连接访问Spark, Presto, Flink 等底层引擎,同时实现跨引擎上下文共享、统一的计算任务和引擎治理与编排能力。
关于Linkis 数据处理实战，我主要分享两方面，一方面关于元数据，另一方面关于计算任务。
元数据
元数据划分为三类：数据字典、数据血缘和数据特征，Linkis基于Linkis DataSource和Apache Atlas 两种服务为数据资产提供元数据管理能力，DataSource 业务边界因为WeDataSphere社区很多开源工具（Scriptis\Visulalis\Exchangis\Streamis）都会用到数据源，缺乏统一管理能力，而且用户需要在不同的产品反复多次设定数据源，我们希望通过提供统一的数据源管理服务，一次设置可以多处使用。Atlas 是一组可扩展和可扩展的核心基础治理服务，Linkis EngineConn (引擎连接器) 基于Atlas Hook 做了整合，执行计算涉及到数据信息，特征，血缘采集到Atlas中，供上游数据资产使用。
计算任务
dolphinscheduler 拉起Linkis 计算任务，dolphinscheduler Shell 任务类型 通过LinkisDolphinSchedulerClient 配置相关参数，拉起相关任务。
小结
到此Linkis 数据处理的整体链路，涉及到元数据，调度任务，形成完整闭环。
 ### Speakers: 
 <img src="images/speaker/1132.png" width="200" /><br>李孟: 上海仙翁科技, 数据架构, 多年数据架构经验，CSDN博客专家，开源爱好者，Beam社区贡献者，WeDataSphere社区贡献者。

 