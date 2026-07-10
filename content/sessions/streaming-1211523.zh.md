---
title: "Exploring Real-Time AI Application Scenarios Based on Flink"
date: ""
track: "streaming"
presenters: "饶饶 熊"
stype: "中文演讲"
---

**1. Background**
- Typical real-time AI application scenarios: real-time ad features, recommendation prediction, fraud detection, content moderation, intelligent operations, etc.
- PyFlink's role in real-time AI: bridging Flink's stream processing capabilities with the Python AI ecosystem, lowering the barrier for algorithm engineers to build real-time AI Flink jobs

**2. PyFlink Practices at Tencent**
- Platform support: dependency management for PyFlink jobs, interpreter optimization, vectorized UDFs, async functions, library/table SDK, and other key technical infrastructure
- Real-time ad feature engineering: building a second-level real-time feature pipeline with PyFlink, addressing feature freshness and online-offline consistency challenges while connecting to the Python ecosystem
- AI Function scenarios: supporting remote inference (AsyncI/O calls to LLM/GPU model services) and local inference (embedded lightweight models), covering a wide range of real-time inference needs from large models to lightweight models

**3. AI Agent-Driven Development & Operations**
- Operations efficiency: building an intelligent diagnostic Agent based on LLM + RAG for anomaly pattern recognition, log analysis, root cause reasoning, and assisted remediation
- Development efficiency: natural language generation of Flink SQL/PyFlink code, schema-aware assistance, code review, and debugging support

**4. Future Outlook**
- Flink AI Agents: a natural language-driven, end-to-end Agent for job development, debugging, and deployment — closing the loop from requirement understanding → code generation → deployment → operations monitoring

### 讲师:


<img src="https://cdn.sessionize.com/image/541e-400o400o1-fRk5WkYAbfkxwYJD5QVohU.jpg" width="200" /><br/>

饶饶 熊: Tencent, Senior Backend Development Engineer

Senior Big Data Engineer at Tencent, focusing on Flink real-time computing and AI infrastructure. Core contributor to Tencent's Flink-based real-time computing platform (Oceanus), with extensive experience in PyFlink ecosystem development, Flink SQL/Runtime related work, and AI-integrated stream processing. Currently leading the exploration of AI Agent-driven development and operations for real-time data platforms. Passionate about bridging the gap between streaming data systems and the AI/ML ecosystem.

