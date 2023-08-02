---
title: "Optimizing HDFS Performance: Achieving Balanced Utilization of Hardware Accelerators and Arm64 Multi-Core Capabilities on Kunpeng920"
date: "2023-08-19T16:15:00" 
track: "performance"
presenters: "Guodong Xu"
stype: "Chinese Session"
---
In today's rapidly evolving technological landscape, the utilization of hardware accelerators to alleviate computational-centric tasks from the CPU has become commonplace. Tasks such as compression and cryptography have traditionally been offloaded to these accelerators. However, as we continue to enhance various components of the entire system, including memory, disk I/O, and network capabilities, we are encountering a shift in the bottleneck, once again placing emphasis on computation-centric tasks in certain scenarios.

While upgrading hardware accelerators may not always be a feasible solution, we can still harness the inherent power and versatility of the multi-core nature of the Arm64 server architecture to extract additional bandwidth.

The purpose of this speech is to present a sophisticated software approach that effectively identifies such bottlenecks and provides insights on how we can reintegrate more CPU cores into computation-centric tasks. The ultimate objective is to achieve efficient and intelligent task distribution between hardware accelerators and the multiple CPU cores.

At the conclusion of this presentation, a standardized benchmark will be showcased to demonstrate the notable enhancements achieved through the implementation of this method. Furthermore, we will outline our future plans and eagerly welcome collaboration from the community in any capacity.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230617/2215411950.jpg" width="200" /><br>Guodong Xu: Linaro Ltd., Senior Tech Lead, 2012-2023 Linaro Ltd. 
 - Arm SVE/SVE2 optimization, senior tech lead
 - Kernel development tech lead
2008-2011 Flextronics Ltd, Software development lead
2002-2007 Motorola Mobile, Linux kernel device driver development

 <br><br>