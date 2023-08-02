---
title: "Kafka without Zookeeper"
date: "2023-08-18T15:45:00" 
track: "messaging"
presenters: "Luke Chen,邓子明"
stype: "Chinese Session"
---
Currently, Kafka relies on ZooKeeper to store its metadata, ex: brokers info, topics, partitions...etc. KRaft is a new generation of Kafka that runs without Zookeeper. This talk will include:

1. Why Kafka needs to develop the new KRaft feature.
2. The architectures of the old (with Zookeeper) Kafka and new (without Zookeeper) Kafka
3. Benefit of adopting KRaft
4. How it works internally.
5. The monitoring metrics
6. Tools to help troubleshoot issues in KRaft
7. A demo to show what we've achieved so far.
8. The roadmap for the Kafka community to move toward KRaft.

After this talk, the audience can have better knowledge of what KRaft is, and how it works, and what's the difference with Zookeeper based Kafka, and most importantly, how to monitor it and troubleshoot it.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230526/1018099720.jpg" width="200" /><br>Luke Chen: RedHat, Senior Software Engineer, I'm a senior software engineer in RedHat working on products to run Apache Kafka on cloud. I'm also a committer and PMC member in Apache Kafka. I've been contributed in Apache Kafka for more than 3 years. 
 <br><br><img src="https://img.bagevent.com/resource/20230525/1008439060.jpg" width="200" /><br>Deng ziming: ByteDance, Data Development,  years of data development experience, Apache Kafka Committer.”
 <br><br>