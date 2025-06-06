---
title: "货拉拉生产环境中的Apache Amoro与Iceberg实践"
date: ""
track: "datalake"
presenters: "Zheng Yu Chen"
stype: "中文演讲"
--- 

在货拉拉，我们利用Apache Amoro构建了以Apache Iceberg为核心的新一代湖仓平台。在管理PB级日处理数据量的过程中，我们解决了关键的稳定性挑战，包括：

生产环境稳定性挑战：

- 生产环境中的小文件压缩与快照过期处理
- 使用对象存储（如S3、OSS）进行大规模数据迁移
- 实时监控与告警，针对合并任务和元数据操作
- 优化表设计，以最小化小文件和压缩开销

架构创新：

- 针对物流数据定制的Iceberg模式与分区策略
- 预防性文件管理，以减少合并压力
- 自动化维护，确保长期稳定性

在本次会议中，我们将分享：

- 在高流量物流平台中扩展Iceberg的经验教训
- 性能与可靠性的关键优化
- 我们的湖仓之旅——从货拉拉的PoC到生产环境

本次演讲将为数据工程师和架构师提供在大型、真实环境中实施Iceberg的可操作见解。

### 讲师:

<img src="https://sessionize.com/image/8dab-400o400o1-wspZVa98jevB6AB6cPZU8m.jpg" width="200" /><br/>

陈正宇（ConradJam），Apache Flink中文社区志愿者，Apache Amoro项目管理委员会成员（PPMC），长期从事大数据数据开发工作。目前，他负责从0到1设计并构建Flink公有云多云数据解决方案、数据同步和大数据运维流水线平台。