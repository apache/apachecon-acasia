---
title: "GeaFlow｜Streaming Graph Computing Engine and AI Memory Practice"
date: "2026-08-09T13:30:00"
track: "incubator"
presenters: "Litao Lin, Yao Zhongqiang"
stype: "Chinese Session"
room: "Mtn YuQuan Hall"
---

GeaFlow is currently incubating at the Apache Software Foundation (ASF). As the industry's first open-source engine dedicated to streaming graph computing, it addresses the challenges that traditional static graph computing faces in dynamic scenarios amid the explosion of real-time data. Through unified semantic design and scheduling models for streaming-batch graph processing, GeaFlow enables efficient analysis and computation of trillion-scale graphs, redefining the technical boundaries of graph computing.
This talk will explore the intrinsic connection between streaming graph computing and real-time Agent memory. We will demonstrate how GeaFlow leverages the inherent capabilities of incremental computation and state management in streaming graphs to solve the real-time update and consistency challenges faced by Agent memory. We will elaborate on the design of GraphMemory, exploring how a hybrid storage architecture that combines vectors, text, and graph relationships can address the limitations of memory retrieval and enhance the long-term memory recall and reasoning capabilities of Agents.
In the technical practice section, we will analyze the application of Graph-GNN (such as SAGNN) in vertical domains like intelligent transportation. We will demonstrate how to construct dynamic road network graphs using GeaFlow and achieve real-time write-back and updates of graph states based on road segment impedance predictions. Additionally, we will outline the architectural roadmap for GeaFlow's integration with other open source engine systems to support trillion-scale graph computing.

### Speakers:


<img src="https://cdn.sessionize.com/image/942a-400o400o1-UTgxQ7mc7kgpLPSnYWcsvV.jpg" width="200" /><br/>

Litao Lin: Apache GeaFlow (Incubating) Committer

Apache GeaFlow (Incubating) Committer. As a core member of the project, he participated in the architecture design and development of the GeaFlow graph computing engine from scratch, with a particular focus on the design and implementation of the graph computing DSL and the evolution of data intelligence technologies. He is deeply involved in open source community activities and currently works at Ant Group.


<img src="https://cdn.sessionize.com/image/8e82-400o400o1-fiJe6bcjN6hvokxoSwtyfp.jpg" width="200" /><br/>

Yao Zhongqiang: Graph Computing Expert & Development Engineer at Ant Group

Deeply involved in the big data field, specializing in graph computing, real-time computing, and OLAP. Current team focus is on Agent Memory and MARL.