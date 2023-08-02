---
title: "字节跳动 MapReduce -> Spark 平滑迁移实践"
date: "2023-08-19T14:00:00" 
track: "datastorage"
presenters: "魏中佳"
stype: "中文演讲"
---

随着业务发展，字节跳动内部每天线上约运行 120万 个  Spark 作业，与之相对比的是，线上每天依然约有两万到三万个 MapReduce 任务。作为一个历史悠久的批处理框架，从大数据研发的角度来看，MapReduce 引擎的运维面临了一系列问题。例如，框架更新迭代的的 ROI 较低，对于新的计算调度框架适配性较差等等。而从用户的角度来看， MapReduce 引擎的使用也存在一系列的问题。例如，计算性能不佳，需要额外的 Pipeline 工具管理串行运行的 Job，希望迁移 Spark 但是存量作业数量多且大量作业使用了 Spark 本身不支持的各种脚本。在此背景下，字节跳动 Batch 团队设计并实现了一套 MapReduce 任务平滑迁移 Spark 的方案，该方案使用户仅需对存量作业增加少量的参数或环境变量即可完成从 MapReduce 到 Spark 的平缓迁移，大大降低了迁移成本，并且取得了不错的成本收益。

 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230609/1631399580.png" width="200" /><br>魏中佳: 字节跳动基础架构工程师 2018 年加入字节跳动，现任字节跳动基础架构大数据开发工程师，专注大数据分布式计算领域，主要负责 Spark 内核开发、字节自研 Shuffle Service 开发。
 <br><br>