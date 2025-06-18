---
title: "弥合鸿沟：在生产环境中协调 Apache SkyWalking 和 OpenTelemetry"
date: "2025-07-27T14:30:00"
room:  "阳山会议室"
track: "observability"
presenters: "Cheng Chen"
stype: "中文演讲"
---

在当今动态的云生态系统中，许多企业由于架构迁移、团队偏好或语言支持限制等原因，在使用多个可观测性堆栈时面临着诸多复杂性。具体而言，Apache SkyWalking 和 OpenTelemetry 本身就功能强大，它们经常在同一个生产环境中共存。然而，这种共存经常会导致兼容性问题，例如跟踪中断、插件增强功能失败，严重的情况下还会导致业务调用错误和应用程序启动失败。
在 CommunityOverCode Asia 2025 的本次会议上，我将分享我们实现 Apache SkyWalking 和 OpenTelemetry 无缝集成的历程和方法。主要讨论要点包括：
● 多 JavaAgent 兼容性：探讨在 Java 应用程序中使用多个 Java Agent 解决类增强功能冲突和应用程序启动失败的策略。
● 多协议兼容性：解决在同一调用链中同时使用 sw8 和 W3C 跟踪上下文协议导致的跟踪中断问题。
● 可观测性堆栈迁移最佳实践：提供在 Apache SkyWalking 和 OpenTelemetry 堆栈之间有效迁移的见解和建议，包括关键注意事项和最佳实践。
本次演讲旨在为同时使用 Apache SkyWalking 和 OpenTelemetry 的企业提供实用指导，以应对兼容性挑战，从而提升系统稳定性和性能。欢迎加入我们，探索这些解决方案，并与社区互动，开展创新讨论。

### 讲师:

<img src="https://sessionize.com/image/b6e1-400o400o1-pQaQfhiHLxaGPmnakbBHWu.jpg" width="200" /><br/>

Cheng Chen: 一线工程师

阿里云高级开发工程师，在可观测性领域拥有多年丰富经验，对可观测数据的采集、计算、存储、分析和可视化有着深入的了解。