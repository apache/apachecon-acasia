---
title: "ServerlessX: A Kernel-Space Serverless System for RDMA-based Disaggregated Architectures"
date: "2026-08-09T16:15:00"
track: "microservice"
presenters: "Mingxuan Liu"
stype: "Chinese Session"
room: "Mtn Yang Hall"
---

This session explores a novel Linux kernel-space Serverless framework designed to bridge the gap between physically disaggregated hardware pools (e.g. disaggregated memory) and the instant execution semantics of modern Serverless functions. By building a three-layer architecture spanning a RDMA network foundation, distributed OS kernel primitives (RDMA Fork, Map, and mmap), and application-specific scaling strategies, we demonstrate how to achieve millisecond-level elasticity across disaggregated resources. Attendees will dive into three practical cases, including rapid GPU scale-out for LLM inference, dynamic memory scale-up for recommendation systems, and decoupled I/O capacity scaling for storage engines.

### Speakers:


<img src="https://cdn.sessionize.com/image/16a6-400o400o1-KNwE7WjxEY3ppBwwGySxky.jpg" width="200" /><br/>

Mingxuan Liu: Northwestern Polytechnical University

Mingxuan Liu is a graduating Ph.D. Candidate at Northwestern Polytechnical University. With over a decade of research experience, his focus spans OS kernels, RDMA networking, Serverless computing, and LLM infrastructure. His doctoral research centers on kernel-mode serverless resource elastic scaling methods for RDMA disaggregated architectures. He has published over ten first-author papers in top-tier (CCF-A/B) academic venues. Mingxuan will soon join the University of Macau as a postdoctoral fellow to continue advancing high-performance distributed systems.