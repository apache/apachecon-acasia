---
title: "Agentic 调试：用 LLM 自动诊断 Impala 查询 Profile"
date: ""
track: "agenticcoding"
presenters: "Surya Hebbar"
stype: "英文演讲"
---

大语言模型在代码生成方面展现出惊人的潜力，但调试分布式系统完全是另一回事。如果你把一份原始的 400MB 数据库查询 profile 喂给 LLM，它要么会被 token 上限噎住，要么会疯狂产生幻觉。要让 agent 在生产环境中成为可靠的协作者，我们必须先修好喂给它们的数据管道。

本次演讲分享来自 Apache Impala 的实战经验，讲述如何让"Agentic 调试"成为现实。我们将探讨从冗长的执行树（execution forest）转向聚合运行时 profile（Aggregated Runtime Profiles）如何解决 LLM 的上下文问题。通过对遥测数据进行高密度打包，并把缺失事件安全地结构化为节省 token 的 JSON 负载，我们让 AI agent 能够自主且准确地诊断执行瓶颈。听众将学到可复用的模式，用以弥合海量系统日志与严格的 LLM 上下文窗口之间的鸿沟。

### 讲师:


<img src="https://cdn.sessionize.com/image/6b92-400o400o1-sPSKNvSRCLEreK26PfKD7w.jpg" width="200" /><br/>

Surya Hebbar：Apache Impala 核心贡献者 | 东京大学硕士研究者

Surya Hebbar 是一名高性能计算工程师，也是 Apache Impala 项目的核心贡献者。作为 Cloudera 的软件工程师，他的工作主要集中在 Impala 的 C++ 后端与分布式系统优化。他主导设计了"Aggregated Runtime Profiles"项目，从根本上对 profile 结构进行了重新工程化——从稀疏的实例级计数器改为密集的、内存高效的数组，以消除高并发集群中的瓶颈。他还牵头对 Impala 的 WebUI 和可观测性工具进行了现代化改造，使其能够处理 PB 级的查询执行图而不会卡死浏览器。

Surya 目前正转入东京大学的地球与行星科学系攻读硕士学位。他将在 Masaki Satoh 教授指导下，借助 Fugaku、Miyabi 等百亿亿次（exascale）超级计算机运行高分辨率气候模型，把他在并行处理方面的专长应用到大气流体动力学领域。
