---
title: "Kafka 4.0 Highlights: Features, Removals, and Upgrades"
date: "2025-07-26T17:15:00"
room: "YuanMing Hall"
track: "streaming"
presenters: "Jiunn-Yang Huang, Chia-Ping Tsai, PoAn Yang, TengYao Chi, YiHuan LEE, Kuan Po Tseng"
stype: "Chinese Session"
---

While there’s already a lot of buzz around Kafka 4.0, most discussions focus on the headline features—like the removal of ZooKeeper or the introduction of new APIs. In this session, we want to highlight some of the lesser-known but equally important changes in Kafka 4.0. These updates might not grab the spotlight, but they can significantly impact how you configure, operate, and debug Kafka in real-world environments.

One of the major questions users face is how to approach the upgrade to Kafka 4.0. KIP-896 removes support for protocol versions 2.0 and below, and KIP-1124 offers official guidance for upgrading Kafka clients, Connect, and Streams. On the server side, users must ensure JDK compatibility and consider how to transition from ZooKeeper-based setups to the new architecture. This section will cover the most critical considerations to keep in mind during the upgrade process.

The Kafka test framework has also undergone a major evolution. Previously, tests were written using an inheritance-heavy design, where subclasses inherited cluster setup logic from parent classes. This made tests difficult to understand and debug, often introducing hidden dependencies and unnecessary configuration. The new test framework simplifies this by using JUnit annotations like @ClusterTest, making test logic clearer, more modular, and easier to maintain.

Kafka 4.1 will also introduces smarter behavior in how it handles rack-aware rebalancing. In earlier versions, storing rack information consumed a large portion of memory for group metadata—up to 80% in some cases. KIP-1101 introduces a caching mechanism that detects rack topology changes efficiently, reducing memory usage and avoiding unnecessary recalculations during group rebalances.

Finally, Kafka 4.0 completes a long-awaited logging upgrade with the delivery of KIP-653. Originally proposed in 2020, KIP-653 replaces reload4j with log4j2, finally resolving long-standing CVE concerns and modernizing the logging infrastructure. Alongside this, Kafka drops support for .properties log config files in favor of YAML. This section provides an overview of the migration and what users need to watch out for when adopting log4j2.

### Speakers:

<img src="https://sessionize.com/image/1452-400o400o1-JyMyZrzbPcSemqnPycYmag.jpg" width="200" /><br/>

Jiunn-Yang Huang: Backend Engineer

I’m a backend engineer who contributes to Apache Kafka. I love learning about distributed systems and event streaming—especially how they power real-time data platforms at scale. Contributed over 100 commits last year and worked on memory optimizations in Kafka.

<img src="https://sessionize.com/image/2d3c-400o400o1-S4UZTbkX3EfAsvqD57soTa.jpg" width="200" /><br/>

Chia-Ping Tsai: Apache Member, Apache HBase PMC member, Apache Kafka PMC member, Apache YuniKorn PMC member

Be a PhD by writing paper of distributed system. Be a PMC member by contributing code to distributed system. Be a valuable guy by enjoying distributed systems


<img src="https://sessionize.com/image/cdca-400o400o1-KCJ6DRaPTfEdWiiTQ4Zzxy.jpg" width="200" /><br/>

PoAn Yang: ASF, Apache YuniKorn committer

I am an open-source software enthusiast, primarily focusing on Apache Kafka. I am among the top 20 contributors, and my work involves enhancing the AsyncKafkaConsumer and developing the next-generation group coordinator.


<img src="https://sessionize.com/image/b096-400o400o1-4neD1RFWbr1BXxdKrF69st.jpg" width="200" /><br/>

TengYao Chi: Apache Kafka Committer

TengYao is a software engineer by day, an open source contributor by night.
In the past year, he has the most commits in Apache Kafka across all contributors in the last 12 months. Most of his contributions are for the async consumer, the next-generation group coordinator protocol, and the migration of log4j2.

He also loves penguins.


<img src="https://sessionize.com/image/c5ac-400o400o1-DuGnE5zsb5qfQTHAKajgzb.jpg" width="200" /><br/>

YiHuan LEE: Graduate student at National Cheng Kung University

My research focuses on "The Effect of Load Balancing on Kafka Performance"

<img src="https://sessionize.com/image/4f33-400o400o1-U8VTJGFMti2BRV8KsAi6VB.png" width="200" /><br/>

Kuan Po Tseng: ASF, Apache Kafka Contributor

My research focuses on "The Effect of Load Balancing on Kafka Performance"