---
title: "BIGO is based on the performance optimization practices of Pulsar in high throughput catch-up read scenarios"
date: "" 
track: "messaging"
presenters: "吴展鹏"
stype: "Chinese Session"
---
BIGO currently has two major video products and services, BIGO Live and Likee short videos. BIGO Live has covered more than 150 countries and regions, and Likee short videos have more than 100 million users. The products are widely popular among Generation Z. BIGO uses the open-source Kafka cluster to support real-time data analysis and short video recommendations. However, as the business continued to grow rapidly, the past structure encountered great challenges. Apache Pulsar's layered architecture and features such as low latency, persistent storage, and horizontal scalability help us solve many of the problems we face in production systems.

In this paper, we will introduce the performance optimization of BIGO based on Pulsar in a high-throughput read/write environment for a catch-up read scenario. The main contents of this paper include: In this article, we will discuss the performance loss caused by the catch-up read, the main time phase of message disk read, the new asynchronous prefetch optimization proposed by BIGO, and the actual performance of the new strategy in the production environment. We will share the thoughts and experiences of BIGO when optimizing the catch-up read scenario in the most realistic way.
 ### Speakers: 
 <img src="images/speaker/1133.png" width="200" /><br>Zhanpeng Wu: BIGO, Staff Engineer, He is a senior big data r&d engineer for BIGO Computing platform. He is currently a contributor for Apache Pulsar, PulSAR-Flink and maintainer of Kafka-on-Pulsar. In the past, I have been invited to give technical speeches at Pulsar Meetup and Pulsar Submit.

 