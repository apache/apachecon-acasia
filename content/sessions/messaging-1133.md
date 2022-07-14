---
title: "BIGO’s Pulsar Performance Optimization Practices in High Throughput Catch-up Read Scenarios"
date: "2022-07-29T16:10:00"
track: "messaging"
room: "B"
presenters: "Zhanpeng Wu"
stype: "Chinese Session"
---
Powered by Artificial Intelligence technology, BIGO's video-based products and services have gained immense popularity, with users in more than 150 countries. The products include BIGO Live (live streaming) and Likee (short-form video). BIGO Live is available in more than 150 countries or regions and Likee has more than 100 million users and is popular among Generation Z. 

BIGO is used to run Kafka clusters to support real-time data analysis and short video recommendations. However, the previous infrastructure encountered great challenges as the business develops. Apache Pulsar architecture and features such as low latency, persistent storage, and horizontal scalability saved us from the situation.

In this talk, we will discuss the performance optimization of BIGO based on Apache Pulsar in a high-throughput read/write environment for a catch-up read scenario. Key takeaways: 
1. a). Discussion on performance loss caused by the catch-up read
2. b). Analysis of the main time-consuming stage of message disk read
3. c). The asynchronous prefetch optimization proposed by BIGO
4. d). Performance of the new strategy in production
5. e). Insights and experiences from optimizing the catch-up read use case.
 ### Speakers: 
 <img src="images/speaker/1133.png" width="200" /><br>Zhanpeng Wu: BIGO Staff Engineer, Senior Big Data R&D Engineer of BIGO Computing Platform. Zhanpeng is an Apache Pulsar contributor, Pulsar Flink Connector contributor, and maintainer of Kafka-on-Pulsar. Zhanpeng Wu is also an active speaker at Pulsar Meetup and Pulsar Summit.

 