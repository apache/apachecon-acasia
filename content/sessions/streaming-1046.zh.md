---
title: "Flink流批一体在Shopee的落地"
date: "" 
track: "streaming"
presenters: "肖贵超"
stype: "中文演讲"
---
Apache Flink的批处理已经具有支持大规模生产的能力，流批一体对数据开发的带来的价值显而易见，正如我们从很多业务团队那里得到的反馈一样。在众多实践中，其主要的切入点是一类同时拥有流和批需求的业务场景，而在Shopee不止于此，Shopee Data Infra的Flink团队在大力发掘流批一体的潜在价值。我们一方面把flink与离线数据系统深度集成，包括账户及权限体系、元数据系统、调度及血缘管理等；另一方面努力增强flink批处理的生产能力，包括remote shuffle service、graph config 、resource profile等。这样，很多数据开发的同学在一个平台就可以用统一的代码完成所有数据处理需求的开发及运维。在这次演讲中，我们将对这些落地实践做详细介绍。
 ### Speakers: 
 <img src="images/speaker/1046.png" width="200" /><br>肖贵超: Shopee, 高级技术专家 (Senior Expert Engineer), Shopee数据架构（Data Infra）实时团队manager，长期从事大数据实时计算领域的引擎研发和大规模生产实践。曾是阿里jstorm和blink团队成员，在多个头部电商公司负责过flink的应用生产落地。
 