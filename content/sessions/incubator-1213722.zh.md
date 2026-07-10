---
title: "AI 辅助的 Apache 孵化器监督"
date: ""
track: "incubator"
presenters: "Justin Mclean"
stype: "英文演讲"
---

在 Apache 孵化器中同时管理多个 Podling，需要整合来自多个互不相连来源的数据：Confluence 报告、GitHub 活动、邮件列表、Whimsy，却没有任何一个地方能呈现完整全貌。本次演讲将介绍一组为改变这一现状而构建的模型上下文协议（MCP）服务器。

这套工具横跨多个相互连接的服务器：一个直接从 podlings.xml 读取生命周期数据的 podlings 服务器，一个暴露提交与社区指标的 apache-health 服务器，一个提供 general@incubator.apache.org 可检索访问的 incubator-mail 服务器，以及一个 IPMC 综合层——它把三者合并成关注列表、毕业就绪度评估、Podling 简报和停滞检测。

演讲将演示真实的工作流：每月一次的 IPMC 监督通查、针对特定 Podling 的 mentor 跟进、识别长期停滞的项目，以及把报告叙述与健康指标交叉比对，找出两者说法不一致之处。它还会探讨这套工具引出的一个更大问题——AI 辅助的监督，是否会改变 Podling 报告本身的需求、频率或形式？

### 讲师:


<img src="https://cdn.sessionize.com/image/abea-400o400o1-G3ffQGzCrw1XXcqnfNEzrB.jpg" width="200" /><br/>

Justin Mclean：ASF 董事、ASF 孵化器 VP、Datastrato 社区经理

Justin Mclean 是 Apache 软件基金会（ASF）的长期贡献者，目前担任 ASF 孵化器 VP 及 ASF 董事会成员。多年来，他致力于推动孵化器的治理、政策与培训项目的演进，包括把项目实际运作方式整理成文，以及对孵化器历史进行分析。通过这些工作，他已帮助数以百计的开源项目构建起可持续、独立的社区。

在引导项目从早期孵化走向成功毕业方面，他经验丰富，审阅过的开源发布物已逾千个。他的工作聚焦于开源治理、社区健康，以及支撑大规模协作的系统设计。

Justin 经常在国际会议上就开源治理、许可证与社区建设等主题发表演讲，分享来自各类 ASF 项目与社区真实实践的鲜活经验。

