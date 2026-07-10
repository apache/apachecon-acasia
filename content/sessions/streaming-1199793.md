---
title: "A New Consumer Offset Policy — 'From Now On, I Want Every Single Message'"
date: ""
track: "streaming"
presenters: "Jiunn-Yang Huang"
stype: "Chinese Session"
---

Kafka's auto.offset.reset offers only earliest, latest, and none, yet none satisfies the most common need: "start consuming from now, but don't miss a single message." latest silently drops data during partition expansion or log truncation; earliest forces reprocessing of massive history; and by_duration still risks data loss due to dynamic timestamp computation.
This talk introduces a new offset reset strategy: by_start_time. It uses the consumer group's creation timestamp as a single, stable anchor point to uniformly handle every scenario — existing partitions, newly added partitions, and offset-out-of-range — all through one ListOffsetsRequest with no hidden branches. We will walk through the KIP's design evolution, its trade-offs, and the practical impact on end users.
Target Audience:
Anyone with hands-on Kafka consumer experience who has hit offset reset issues in production. If you've debugged data loss from partition expansion late at night, or been confused by the semantic differences among auto.offset.reset options, this talk is for you.
Key Takeaways:
(1) Understand how existing strategies lose data under partition expansion and log truncation. 
(2) Grasp by_start_time's core design — one unified rule anchored to group creation timestamp covering all reset scenarios. 
(3) Learn the KIP's design evolution and known limitations.

### Speakers:


<img src="https://cdn.sessionize.com/image/1452-400o400o1-JyMyZrzbPcSemqnPycYmag.jpg" width="200" /><br/>

Jiunn-Yang Huang: Backend Engineer

I’m a backend engineer who contributes to Apache Kafka. I love learning about distributed systems and event streaming—especially how they power real-time data platforms at scale.

