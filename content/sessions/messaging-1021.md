---
title: "Introducing TableView: Pulsar's database table abstraction"
date: "2022-07-31T13:30:00"
track: "messaging"
room: "A"
presenters: "David Kjerrumgaard"
stype: "English Session"
---
In many use cases, applications are using Pulsar consumers or readers to fetch all the updates from a topic and construct a map with the latest value of each key for the messages that were received. 

The new TableView consumer offers support for this access pattern directly in the Pulsar client API itself, and encapsulates the complexities of manually constructing such local cache manually. In this talk, we will demonstrate how to use the new TableView consumer using a simple application and discuss best practices and patterns for using the TableView consumer.
 ### Speakers: 
 <img src="images/speaker/1021.png" width="200" /><br>David Kjerrumgaard: StreamNative, Developer Advocate, David is a committer on the Apache Pulsar project, and also the author of "Pulsar in Action" and co-author of "Practical Hive". He currently serves as a Developer Advocate for StreamNative where he focuses on strengthening the Apache Pulsar community through education and evangelization. Prior to that he was a principal software engineer on the messaging team at Splunk, and Director of Solutions for two Big Data startups; Streamlio and Hortonworks.

 