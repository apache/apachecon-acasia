---
title: "万法归 SQL：把 DataFusion 的优化迁移到另一个非通用计算系统"
date: "2026-08-07T14:30:00"
track: "datastorage"
presenters: "Ruihang Xia"
stype: "中文演讲"
room: "万寿山会议室"
---

在基于 Apache DataFusion 重新实现 PromQL（Prometheus 背后的查询语言）的过程中，我们在这两种截然不同的语言之间发现了许多相似的优化模式。有些思路相近，有些可以融合在一起，还有一些被反哺回了 DataFusion。我们进一步确信：几乎所有看起来各不相同的计算系统，无论其用户界面长什么样，本质上都由若干通用的原语（primitive）组合而成。在本次演讲中，我们会先讨论这些原语及其优化，随后谈谈如何在为不同系统和不同目的做优化时，保持简洁与统一的高层哲学，并以大量知名系统作为案例。

### 讲师:


<img src="https://cdn.sessionize.com/image/17ae-400o400o1-PGTz6fMBHyvwhcgyuLCThc.png" width="200" /><br/>

Ruihang Xia：Greptime 软件架构师

Greptime 软件架构师
Apache DataFusion PMC、Apache Arrow Committer、Apache HoraeDB PPMC
https://github.com/waynexia