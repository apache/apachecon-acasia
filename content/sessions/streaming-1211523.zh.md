---
title: "基于 Flink 探索实时 AI 应用场景"
date: ""
track: "streaming"
presenters: "饶饶 熊"
stype: "中文演讲"
---

**1. 背景**
- 典型的实时 AI 应用场景：实时广告特征、推荐预测、欺诈检测、内容审核、智能运维等。
- PyFlink 在实时 AI 中的角色：把 Flink 的流处理能力与 Python AI 生态连接起来，降低算法工程师构建实时 AI Flink 作业的门槛。

**2. PyFlink 在腾讯的实践**
- 平台支持：PyFlink 作业的依赖管理、解释器优化、向量化 UDF、异步函数、库/表 SDK 等关键技术基础设施。
- 实时广告特征工程：用 PyFlink 构建秒级实时特征管道，在接入 Python 生态的同时，解决特征新鲜度与线上线下一致性的挑战。
- AI Function 场景：支持远程推理（通过 Async I/O 调用 LLM/GPU 模型服务）和本地推理（内嵌轻量级模型），覆盖从大模型到轻量级模型的广泛实时推理需求。

**3. AI Agent 驱动的开发与运维**
- 运维效率：基于 LLM + RAG 构建智能诊断 Agent，用于异常模式识别、日志分析、根因推理和辅助修复。
- 开发效率：用自然语言生成 Flink SQL/PyFlink 代码，提供 schema 感知的辅助、代码评审与调试支持。

**4. 未来展望**
- Flink AI Agents：一个由自然语言驱动、端到端的 Agent，用于作业开发、调试和部署——打通"需求理解 → 代码生成 → 部署 → 运维监控"的闭环。

### 讲师:


<img src="https://cdn.sessionize.com/image/541e-400o400o1-fRk5WkYAbfkxwYJD5QVohU.jpg" width="200" /><br/>

饶饶 熊：腾讯，资深后端开发工程师

腾讯资深大数据工程师，专注于 Flink 实时计算与 AI 基础设施。腾讯基于 Flink 的实时计算平台（Oceanus）的核心贡献者，在 PyFlink 生态开发、Flink SQL/Runtime 相关工作以及 AI 与流处理结合方面经验丰富。目前牵头实时数据平台 AI Agent 驱动的开发与运维方向的探索。热衷于弥合流式数据系统与 AI/ML 生态之间的鸿沟。
