---
title: "Deep Dive into Apache Pulsar Transaction - How it works and notes for it."
date: "" 
track: "messaging"
presenters: "孟祥迎"
stype: "Chinese Session"
---
Apache Pulsar Transaction is an important feature supported by Apache Pulsar 2.9.0. After several iterations, Pulsar Transaction is now stable and has been adopted and put into production by many companies. In order to enable more people to understand and use Pulsar Transaction, the author will briefly introduce the basic concept and implementation principle of Transaction in this lecture, and introduce how to use Pulsar Transaction in detail. And what you need to be aware of when using Transaction.
After introducing the basic concepts and implementation principles of Transaction, the audience should have a general understanding of transaction. After that, the author describes how to start and configure transaction, and details the role of each configuration item associated with transaction. I then describe how to use Transaction to send and acknowledge messages, and what to be aware of when using Transaction. Some optimizations that may be added in the future will be introduced later to give you a clear idea of where transaction is going.
Finally, the author describes how to use operations tools to view the status information related to a transaction and how to test the performance of a transaction.
 ### Speakers: 
 <img src="images/speaker/1204.png" width="200" /><br>Xiangying Meng: StreamNative, Platform Engineer, Xiangying Meng, Apache Pulsar Committer, StreamNative Platform Engineer, loves open source, currently focusing on Apache Pulsar Transaction.

 