---
title: "GeaFlow | Streaming Memory: Building a Real-time Stateful Backend to Empower AI+Graph Scenarios"
date: "2026-08-08T16:15:00"
track: "streaming"
presenters: "Litao Lin, Yao Zhongqiang"
stype: "Chinese Session"
room: "YuanMing Hall"
---

In 2026, AI Agent memory architecture is undergoing a paradigm shift. Traditional AI Agent memory systems largely adopt a batch processing mode characterized by "append-only writes + asynchronous indexing." This results in significant latency in memory updates, making it difficult to support contextual evolution in real-time interaction scenarios. The essence of memory is not a static dataset, but an unbounded data stream composed of dialogue, perception, and decision-making. How to perform low-latency state management and incremental computation on this stream represents a new challenge for stream computing technology in the AI era.
This session will focus on how stream computing technology addresses the memory challenge. Apache GeaFlow (Incubating), an open-source streaming graph computation engine, is positioned as a real-time incremental graph computation layer, serving as the real-time stateful backend for Agents. Unlike traditional graph databases and stream computing engines that lack native relationship modeling capabilities, GeaFlow processes incoming data as continuous graph updates via incremental computation—where each event triggers only necessary subgraph changes, thereby avoiding expensive full recomputations.
Specifically, GeaFlow replaces full computation with incremental streaming computation to enable real-time updates of local subgraphs the instant a dialogue occurs. Through dynamic graph state management, it maintains temporal memory as stream state, resolving state consistency issues in long-running dialogues. Furthermore, it leverages a distributed snapshot mechanism to ensure state fault tolerance and recovery for enterprise-level multi-Agent collaboration.
In the technical practice segment, we will demonstrate how to build a knowledge assistant capable of millisecond-level memory updates. We will also showcase how GeaFlow provides foundational support for AI systems operating on continuously evolving knowledge graphs.

### Speakers:


<img src="https://cdn.sessionize.com/image/942a-400o400o1-UTgxQ7mc7kgpLPSnYWcsvV.jpg" width="200" /><br/>

Litao Lin: Apache GeaFlow (Incubating) Committer

Apache GeaFlow (Incubating) Committer. As a core member of the project, he participated in the architecture design and development of the GeaFlow graph computing engine from scratch, with a particular focus on the design and implementation of the graph computing DSL and the evolution of data intelligence technologies. He is deeply involved in open source community activities and currently works at Ant Group.


<img src="https://cdn.sessionize.com/image/8e82-400o400o1-fiJe6bcjN6hvokxoSwtyfp.jpg" width="200" /><br/>

Yao Zhongqiang: Graph Computing Expert & Development Engineer at Ant Group

Deeply involved in the big data field, specializing in graph computing, real-time computing, and OLAP. Current team focus is on Agent Memory and MARL.