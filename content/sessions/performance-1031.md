---
title: "Apache Arrow Optimization on Arm"
date: "2023-08-19T14:30:00" 
track: "performance"
presenters: "Yibo Cai"
stype: "Chinese Session"
---
This speech introduces our practices of optimizing Apache Arrow on Arm platform. Using upstream PRs as solid examples, we will present the techniques to profile and optimize complex workloads on Arm, including but not limited to Top-down methodology, Arm SPE (Statistical Profiling Extension), NEON, etc.

Apache Arrow is a multi-language toolbox for accelerated data interchange and in-memory processing. This speech focuses on Arrow C++ implementation. As an example, we will show how Arm SPE helps to identify a performance bottleneck from a mis-predicted branch in Arrow CSV writer benchmark, which leads to an optimization that achieves ~50% performance uplift with trivial code changes. 

Audience may learn general software profiling and optimization knowledge from this speech, as well as Arm specific techniques.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230523/1131180950.jpg" width="200" /><br>Yibo Cai: Arm, Principal Software Engineer, Yibo has been working in the IT industry for more than 20 years. He is principal software engineer from Arm, focusing on improving software ecosystem on Arm server. Including big data, storage, and database. 

Yibo has rich experience in software optimization, from libraries to complex workloads, from low level architecture specific optimization to high level algorithm improvement.

Yibo is an active open source contributor. He is Apache Arrow PMC member and SPDK maintainer for SPDK-CSI project.
 <br><br>