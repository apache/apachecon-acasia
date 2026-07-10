---
title: "Scaling Apache Ozone at Didi: Operating 100PB+ Storage and Billions of Files in Production"
date: ""
track: "datastorage"
presenters: "Shilun Fan, Ming Wei, Hongbing Wang"
stype: "Chinese Session"
---

As Didi’s unstructured data grew rapidly, HDFS metadata pressure became a major scalability challenge. Apache Ozone was introduced as the next-generation storage engine to address these limitations, and it has now been running in production at Didi for more than two years, supporting over 100 PB of data and tens of billions of files.

This session gives an introductory overview of Didi’s Ozone journey, including why Ozone was chosen, how the platform evolved in production, and what engineering work was required to improve scalability, performance, and reliability. We will share practical experience in multi-cluster routing, follower-read optimization for S3 workloads, read performance tuning, erasure coding adoption, large-scale deletion and migration, observability, and availability improvements. The session will also summarize lessons learned from operating Ozone at scale and contributing improvements back to the Apache Ozone community.

### Speakers:


<img src="https://cdn.sessionize.com/image/06ea-400o400o1-Wwh5e6GkraWD5RMk1W3UK2.jpg" width="200" /><br/>

Shilun Fan: Storage Engineer at DiDi, Apache Ozone Contributor

Shilun Fan is an Apache Hadoop PMC Member, an Apache Auron Committer, and an Apache Ozone Contributor. He works on large-scale distributed storage systems and data infrastructure at DiDi. He has been deeply involved in the production deployment and optimization of Apache Ozone, with a focus on scalability, performance tuning, erasure coding, and reliability. His work focuses on building scalable, reliable, and cost-efficient storage platforms for massive data workloads.


<img src="https://cdn.sessionize.com/image/b659-400o400o1-3YG7S2Eu2hqjimXdLd2L7h.jpg" width="200" /><br/>

Ming Wei: Storage Engineer at DiDi

Apache Ozone Contributor


<img src="https://cdn.sessionize.com/image/fd26-400o400o1-LdRsa125u41W2EhLPzcXxk.jpg" width="200" /><br/>

Hongbing Wang: Storage Engineer at DiDi

Apache Ozone Committer

