---
title: "模拟和人工智能行业背后的Apache Ozone"
date: "2022-07-30T13:30:00"
track: "bigdata"
room: "B"
presenters: "Kota Uenishi"
stype: "英文演讲"
---
这篇演讲介绍了在Preferred Networks的自托管超级计算机系统中，Apache Ozone上的两种工作负载。它们是我们努力将AI和HPC生态系统(PyTorch, GPU)与大数据生态系统(JVM，商用硬件)连接起来的成果。
一种是深度学习模型的分布式训练。从本质上讲，这是一个反复随机读取的工作量，单轮训练大约需要数百万张图像。由于工作负载的随机读取特性，预取数据无法充分隐藏延迟，从而优化吞吐量。我们将介绍如何通过引入客户端缓存系统来缓解这个问题。
另一个是科学模拟的数据集生成(第一线原理计算)，以及3D模型的图像渲染。数据量与计算资源(例如gpu)成正比不断增长。我们在Apache Ozone中引入了一种新的小文件问题——单个对象的元数据开销不能为零。我们还讨论了如何在当前客户端的约束条件下，将多个(数亿到数百万)文件聚合为一个数据集文件;例如boto、zip等库和理想的存档格式。
 ### Speakers: 
 <img src="images/speaker/1151.png" width="200" /><br>Kota Uenishi: Preferred Networks的软件工程师，最近为Apache Ozone贡献了一些补丁。他的团队使用Apache Ozone来提升Preferred Networks拥有的超级计算机的潜力。他曾在Chainer项目工作，该项目是历史上支持大规模分布式培训的深度学习框架之一，熟悉大规模深度学习工作负载。

 