---
title: "Deep Dive into Message Chunking in Pulsar"
date: "2022-07-30T16:10:00"
track: "messaging"
room: "A"
presenters: "Zike Yang"
stype: "Chinese Session"
---
Like all messaging systems, Apache Pulsar imposes a size limit on each message sent to the broker. It prevents the payload of each message from exceeding the max message size set in the pulsar broker. However, many users need the Pulsar client to send large messages to the broker for use cases such as image and audio processing. 

Therefore, instead of increasing the configuration of max message size, Pulsar provides a message chunking feature to enable sending large messages. With message chunking, the producer can split a large message into multiple chunks based on the max message size configuration and send each chunk to the broker as an ordinary message. The consumer then combines the chunks back to the original message.

In this talk, Zike Yang will explain the concept of message chunking, deep dive into its implementation, and share best practices for this feature.
 ### Speakers: 
 <img src="images/speaker/1156.png" width="200" /><br>Zike Yang: StreamNative, Software Engineer, Zike Yang is a software engineer at Streamnative. He is also an Apache Pulsar committer.

 