---
title: "Challenges of Implementing Iceberg Features in a C++ Query Engine"
date: ""
track: "datalake"
presenters: "Zoltán Borók-Nagy, Péter Rózsa"
stype: "英文演讲"
---

Apache Impala is a hybrid, massively parallel query engine: its query planning and metadata handling are implemented in Java, while its execution engine is written in C++. This architecture presents unique challenges when integrating Apache Iceberg, whose reference implementation and ecosystem are primarily Java-based. Attendees will gain insight into the practical challenges of bringing Iceberg to non-JVM query engines.

We will explore how Iceberg features are implemented in a distributed C++ query engine, and where Impala can reuse existing Iceberg libraries versus where custom implementations are required. We will dive into concrete examples, including metadata handling and row-level operations. The session will also highlight opportunities this model creates, such as rethinking how merge-on-read is implemented.

Finally, attendees will also learn about the current state of Iceberg support in Impala and how our progress is going toward adopting Iceberg V3.

### 讲师:


<img src="https://cdn.sessionize.com/image/84b3-400o400o1-7GoTobWcFvV4kLv5UvF1Mn.jpg" width="200" /><br/>

Zoltán Borók-Nagy: Cloudera, Principal Engineer

Zoltán is a software engineer at Cloudera, working on Apache Impala. He is also a PMC member on the project. Currently he is leading the Impala/Iceberg integration efforts. Before Cloudera, Zoltán worked on C++ static analysis tools. He is interested in distributed, massively parallel systems, databases, and performance engineering.


<img src="https://cdn.sessionize.com/image/0f03-400o400o1-VjFuA65v8Md5uQxrNPHre2.jpg" width="200" /><br/>

Péter Rózsa: Cloudera, Software Engineer

Péter Rózsa, a Software Engineer at Cloudera since 2020, started contributing to Apache Impala in 2022. He's been working on different parts of the Impala project, recently on Iceberg integrations

