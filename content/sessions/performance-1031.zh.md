---
title: "在Arm上优化Apache Arrows" 
date: "2023-08-19T14:30:00" 
track: "performance"
presenters: "蔡亦波"
stype: "中文演讲"
---
本演讲介绍了我们在Arm平台上优化Apache Arrow的实践。以上游pr为例，我们将介绍在Arm上分析和优化复杂工作负载的技术，包括但不限于自顶向下的方法、Arm SPE(统计分析扩展)、NEON等。

Apache Arrow是一个多语言工具箱，用于加速数据交换和内存处理。这次演讲的重点是Arrow的c++实现。作为一个例子，我们将展示Arm SPE如何帮助从Arrow CSV编写器基准测试中错误预测的分支中识别性能瓶颈，从而通过简单的代码更改实现约50%的性能提升。

听众可以从这个演讲中学习到一般的软件分析和优化知识，以及Arm特定的技术。
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230523/1131180950.jpg" width="200" /><br>蔡亦波: ARM, 首席软件工程师, 易博从事IT行业已有20多年。他是Arm的首席软件工程师，专注于改进Arm服务器上的软件生态系统。包括大数据、存储、数据库。

易博在软件优化方面拥有丰富的经验，从库到复杂的工作负载，从底层架构特定的优化到高层算法改进。

蔡亦波是一个活跃的开源贡献者。他是Apache Arrow PMC成员和SPDK- csi项目的SPDK维护者。
 <br><br>