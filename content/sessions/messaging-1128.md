---
title: "Luban RocketMQ platform message grayscale scheme"
date: "" 
track: "messaging"
presenters: "区二立"
stype: "Chinese Session"
---
RocketMQ (MQ) is widely used as messaging middleware in transaction management, asynchronous decoupling, peak load balancing, and data synchronization applications. When the business system publishes grayscale, the call of Dubbo and HTTP can be realized in Vivo's microservice governance and gateway platform based on the general grayscale method in the industry. However, none of the known grayscale schemes of MQ can completely solve the problem of message isolation and switch connection. Therefore, Vivo technical architecture team added extended implementation of MQ grayscale function in Luban MQ platform (including root cause analysis, resource management, subscription relationship verification, delay optimization, etc.). This scheme is mainly based on the target usage mode of split queue for deep extended encapsulation.
 ### Speakers: 
 <img src="images/speaker/1128.png" width="200" /><br>Erli Qu: vivo, Technical director, 1. Former Technical architect of Ali Middleware and native solution architect of Ali Cloud, shared different middleware in principle and practice on different occasions.
1. Currently serving as the central director of Vivo platform, leading the construction of Luban MQ platform from 0 to 1, sub-database and sub-table platform (supporting complex statements and customized strategies), including the shared development platform of Dubbo/MQ/HTTP /xxlJob, and global ID service in full format (considering open source); The extension encapsulates redisson, Dubbo, Sentinel, Seata and other general middleware.

 