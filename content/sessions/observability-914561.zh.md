---
title: "eBPF + MCP：DeepFlow 全栈可观测性与智能体实践案例"
date: "2025-07-27T16:45:00"
room: "阳山会议室"
track: "observability"
presenters: "Yang Xiang"
stype: "中文演讲"
---

Apache APISIX、Kafka、RocketMQ 和 Pulsar 都是优秀的中间件软件，应用广泛。然而这些中间件的可观测性通常仅限于粗粒度的指标暴露，缺乏与分布式追踪的关联。因此当面临长尾性能问题时，中间件运维人员往往只能通过 tcpdump 或日志分析等基础工具进行排障和根因定位，效率低下。eBPF 的零侵入特性有效解决了这些痛点。DeepFlow（开源项目）利用 eBPF 实现了对各类 Apache 中间件服务"代码函数、系统调用、文件 I/O、网络转发"的全栈可观测性，无需任何配置变更或进程重启。同时基于通过 MCP 协议暴露的全栈可观测性数据，DeepFlow 智能体能够快速自主识别性能瓶颈并提供优化建议。本次演讲将介绍 DeepFlow 基于 eBPF 的全栈可观测性能力和基于 MCP 的智能体使用场景。

### 讲师:

<img src="https://sessionize.com/image/b9fe-400o400o1-7eiz9d5NPVegnn7SkHVGzm.jpg" width="200" /><br/>

Yang Xiang: 云杉网络，总裁

清华大学博士，现任云杉网络总裁兼 DeepFlow 开源社区负责人。他曾在 ACM SIGCOMM 和 ACM IMC 等国际顶级学术会议上发表过关于应用可观测性和网络测量等主题的学术论文。