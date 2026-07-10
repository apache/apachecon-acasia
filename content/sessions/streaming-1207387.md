---
title: "Kafka Streams 4.2.0 Dead Letter Queue: From Manual Workarounds to Built-in Transaction Safety"
date: ""
track: "streaming"
presenters: "Eric Chang"
stype: "Chinese Session"
---

Handling bad records in Kafka Streams looks simple at first: catch the bad record, write it to another topic, and continue. In practice, it becomes more subtle once deserialization errors, custom exception handlers, and exactly-once processing are involved.

This session is a practical walkthrough of KIP-1034: Dead Letter Queue in Kafka Streams, a Kafka improvement proposal created by Damien Gasparina and coauthored by Damien Gasparina, Loic Greffier, and Sebastien Viale. I am not an author of the KIP; this talk is an engineer’s reading and hands-on exploration of the feature through runnable examples.

Before Kafka 4.2.0, adding a Dead Letter Queue often meant writing and maintaining custom exception handlers, a separate producer, producer lifecycle code, and manual header handling for source topic, partition, offset, exception type, message, and stack trace. Kafka Streams 4.2.0 introduces built-in Dead Letter Queue support that can be enabled with just a few configuration lines. Kafka Streams creates the default Dead Letter Queue record, adds the standard error headers automatically, and sends it through its internal producer path.

We will compare a pre-KIP-1034 manual Dead Letter Queue implementation with the Kafka 4.2.0 approach, then look at why this matters for transaction safety. With a manual Dead Letter Queue producer, the Dead Letter Queue write sits outside the Kafka Streams transaction boundary. If that write is committed and the Streams transaction later aborts, the same bad input record may be retried and written to the Dead Letter Queue again. KIP-1034 closes this gap by letting Dead Letter Queue writes follow the same Kafka Streams internal write path as normal output records.

Attendees will leave with a practical mental model for when KIP-1034 helps, what problems it solves, and how to migrate away from ad hoc Dead Letter Queue implementations in Kafka Streams.

References:

- [blog post about the content of this session](https://blog.unknowntpo.me/blog/kafka-kip-1034-dlq)
- [KIP-1034](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1034%3A+Dead+letter+queue+in+Kafka+Streams)
And here's the link to the KIP: 

### Speakers:


<img src="https://cdn.sessionize.com/image/66b0-400o400o1-UHasfsGgbmwaRvqqXqtoL1.png" width="200" /><br/>

Eric Chang: Apache Gravitino Committer, Apache Kafka contributor, and member of OpenSourceForYou, a vibrant Taiwan-based open-source community founded by Chia-Ping Tsai

Eric Chang is an Apache Gravitino Committer and Apache Kafka contributor based in Taiwan. He is also a member of OpenSourceForYou, a vibrant Taiwan-based open-source community founded by Chia-Ping Tsai. Eric is interested in backend systems, Kafka, and distributed data processing, and he writes technical articles with runnable examples to explain practical engineering problems. His recent work explores Kafka Streams KIP-1034 and how built-in Dead Letter Queue support changes the way applications handle bad records under exactly-once processing.

