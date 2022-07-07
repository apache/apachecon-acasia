---
title: "Towards a ZooKeeper-less Pulsar"
date: "2022-07-30T14:10:00"
track: "messaging"
room: "A"
presenters: "David Kjerrumgaard"
stype: "English Session"
---
Starting with version 2.10, the Apache ZooKeeper dependency has been eliminated and been replaced with a pluggable framework that enables you to reduce the infrastructure footprint of Apache Pulsar by leveraging alternative metadata and coordination systems based upon your deployment environment.


In this talk, I will walk you through the steps required to utilize the existing etcd service running inside Kubernetes to act as Pulsar's metadata store. Thereby eliminating the need to run ZooKeeper entirely, leaving you with a Zookeeper-less Pulsar.
 ### Speakers: 
 <img src="images/speaker/1020.png" width="200" /><br>David Kjerrumgaard: StreamNative, Developer Advocate, David is a committer on the Apache Pulsar project, and also the author of "Pulsar in Action" and co-author of "Practical Hive". He currently serves as a Developer Advocate for StreamNative where he focuses on strengthening the Apache Pulsar community through education and evangelization. Prior to that he was a principal software engineer on the messaging team at Splunk, and Director of Solutions for two Big Data startups; Streamlio and Hortonworks.

 