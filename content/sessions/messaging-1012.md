---
title: "Deep Dive the replication protocol in Kafka"
date: "2023-08-18T16:30:00" 
track: "messaging"
presenters: "Luke Chen"
stype: "Chinese Session"
---
Being a messaging system, the data durability is very important. The replication ensures automatic failover to other replicas when a server in the cluster fails so messages remain available in the presence of failures. In Apache Kafka, the replication protocol is not only used to achieve durability, but also to achieve high throughput. In this talk, we'll deep dive how the replication protocol works internally in Kafka. We'll also explain what's the pros and cons of this kind of design. Furthermore, we'll also introduce the other kind of replication protocol in Kafka, which is used for KRaft controllers (i.e. quorum based way). 

After this talk, the audience can rethink these replication protocols, and maybe some of the ideas can be brought into some other distributed system projects. Hope it will also help audience know more about Apache Kafka.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230602/1539258830.jpg" width="200" /><br>Luke Chen: RedHat, Senior Software Engineer, I'm a senior software engineer in RedHat working on products to run Apache Kafka on cloud. I'm also a committer and PMC member in Apache Kafka. I've been contributed in Apache Kafka for more than 3 years. 
 <br><br>