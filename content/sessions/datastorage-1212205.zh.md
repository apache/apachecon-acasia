---
title: "滴滴 Apache Ozone 规模化实践：生产环境运营 100PB+ 存储与数十亿文件"
date: "2026-08-07T17:15:00"
track: "datastorage"
presenters: "Shilun Fan, Ming Wei, Hongbing Wang"
stype: "中文演讲"
room: "万寿山会议室"
---

随着滴滴非结构化数据快速增长，HDFS 元数据压力成为主要的可扩展性挑战。滴滴引入 Apache Ozone 作为下一代存储引擎来突破这些瓶颈，目前 Ozone 已在滴滴稳定运行两年多，支撑超过 100 PB 数据和数百亿文件。

本次演讲将对滴滴的 Ozone 历程做入门级概览，包括当初为何选择 Ozone、平台在生产环境中的演进，以及为提升可扩展性、性能和可靠性所做的工程工作。我们将分享在多集群路由、面向 S3 工作负载的 follower-read 优化、读性能调优、纠删码应用、大规模删除与迁移、可观测性以及可用性提升等方面的实践经验。演讲还会总结大规模运营 Ozone 的经验教训，以及把改进回馈给 Apache Ozone 社区的过程。

### 讲师:


<img src="https://cdn.sessionize.com/image/06ea-400o400o1-Wwh5e6GkraWD5RMk1W3UK2.jpg" width="200" /><br/>

Shilun Fan：滴滴存储工程师，Apache Ozone 贡献者

Shilun Fan 是 Apache Hadoop PMC 成员、Apache Auron Committer，以及 Apache Ozone 贡献者。他在滴滴从事大规模分布式存储系统与数据基础设施的工作。他深度参与了 Apache Ozone 的生产部署与优化，重点关注可扩展性、性能调优、纠删码与可靠性。他的工作重心是为海量数据工作负载构建可扩展、可靠且高性价比的存储平台。


<img src="https://cdn.sessionize.com/image/b659-400o400o1-3YG7S2Eu2hqjimXdLd2L7h.jpg" width="200" /><br/>

Ming Wei：滴滴存储工程师

Apache Ozone 贡献者


<img src="https://cdn.sessionize.com/image/fd26-400o400o1-LdRsa125u41W2EhLPzcXxk.jpg" width="200" /><br/>

Hongbing Wang：滴滴存储工程师

Apache Ozone Committer