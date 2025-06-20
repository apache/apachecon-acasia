---
title: "Practice of Flink Memory Governance at ByteDance"
date: "2025-07-26T15:00:00"
room:  "YuanMing Hall"
track: "streaming"
presenters: "Yiheng Tang, Shaojun Wang"
stype: "Chinese Session"
---

As the demand for streaming tasks continues to grow within ByteDance, Flink has been widely adopted across various business domains at scale. Among the resource costs of these large-scale tasks, memory stands out as a significant contributor—especially heap memory. The total allocated memory for all tasks has reached tens of thousands of terabytes, yet the JVM heap utilization remains below 50%, and container-level memory usage is under 70%. Against the backdrop of company-wide cost reduction and efficiency improvement, we have carried out a series of memory optimizations focused on heap memory usage prediction, off-heap memory usage tracking, and simplifying Flink’s memory model. These efforts have been successfully rolled out across ByteDance, resulting in memory savings of over a thousand terabytes.
In this talk, we will present the key joint optimizations led by the Flink and JVM teams at ByteDance, and share the results we’ve achieved.

Agenda:
1.  Background
  - Current memory usage status of Flink at ByteDance
  - Key challenges we are facing
2. Heap memory usage prediction
3.  Off-heap memory usage tracking
4. Simplification of the Flink memory model: Unified memory pool
5. Implementation and benefits
6. Future plans
  - Exploration of further optimization directions


### Speakers:


<img src="https://sessionize.com/image/0408-400o400o1-Qugv97SCsud3LMz6G4ZKqV.jpg" width="200" /><br/>

Yiheng Tang: Bytedance Infrastructure Engineer

Flink Runtime Developer at Bytedance


<img src="https://sessionize.com/image/183a-400o400o1-4CYkeMZCjrpekwjGgjF934.jpg" width="200" /><br/>

Shaojun Wang: ByteDance, China, Programming Language Engineer

1. The PPMC of the Apache incubating project teaclave
2. A Gopher since 2017
3. A Programming Language Engineer @ByteDance