---
title: "When failure is not an option."
date: "" 
track: "messaging"
presenters: "David Kjerrumgaard"
stype: "English Session"
---
Developing a highly-available application requires more than just utilizing fault-tolerant services such as Apache Pulsar in your software stack. It also requires immediate failure detection and resolution including built-in failover when there are data center outages.

Up until now, Pulsar clients could only interact with a single Pulsar cluster and were unable to detect and respond to a cluster-level failure event. In the event of a complete cluster failure, these clients cannot reroute their messages to a secondary/standby cluster automatically.

With the release of Pulsar 2.10, this much-needed automated cluster failover capability has been added to the Pulsar client libraries. In this talk, I will walk you through the changes you need to make inside your application code to take advantage of this new capability.
 ### Speakers: 
 <img src="images/speaker/1019.png" width="200" /><br>David Kjerrumgaard: StreamNative, Developer Advocate, David is a committer on the Apache Pulsar project, and also the author of "Pulsar in Action" and co-author of "Practical Hive". He currently serves as a Developer Advocate for StreamNative where he focuses on strengthening the Apache Pulsar community through education and evangelization. Prior to that he was a principal software engineer on the messaging team at Splunk, and Director of Solutions for two Big Data startups; Streamlio and Hortonworks.

 