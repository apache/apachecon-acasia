---
title: "Capturing per thread statistics for a job - Thread-level IOStatistics - HADOOP-17461"
date: "2022-07-30T13:30:00"
track: "bigdata"
room: "A"
presenters: "Mehakmeet Singh"
stype: "English Session"
---
For effective reporting of the IOtatistics of individual worker threads, we need a thread-level context that IO components update(HADOOP-17461).
 
IOStatistics is a statistics capturing API created by Steve Loughran which includes counters, max, mins, means, and gauges for a filesystem and streams to look at. These statistics give off better details for a job or operation than we had previously in the Hadoop world and could be used to figure out performance improvements needed in certain areas of a filesystem.
 
Implementation in S3A and ABFS streams includes the creation of an IOStatisticsSnapshot WeakReferenceTreeMap which would store a specific thread ID as the key and the Snapshot of an IOstatistics instance as the value. Only aggregating it once the stream closes and then setting the snapshot back. This would help in getting the IOStatistics of a particular thread’s work even after the streams are closed.
 
This would provide a better view into Hive and spark jobs in the big data space where the failure of a job doesn’t necessarily end up with a certain set of statistics to look at and debug the issue better. Having the statistics per thread level is also beneficial in getting a better look into such jobs dealing with big data and presenting us with a good way to understand the issue better on a thread level.
 ### Speakers: 
 <img src="images/speaker/1191.png" width="200" /><br>Mehakmeet Singh: Cloudera, Software Engineer II, My name is Mehakmeet Singh, have a bachelors in Technology in Computer Science, and landing an Internship + FTE at Cloudera was my first venture in this industry straight out of college. After being here for around 2 years I have contributed a lot to the OpenSource community mostly via the Cloud-Connectors projects which I am a part of in Cloudera. My work began with gathering simple Counters in Azure Blob Filesystem(ABFS) in Hadoop to Implementing Client-Side Encryption in AWS S3A, Providing a better way to buffer data in ABFS to not run into OOM errors, and then working on Thread-level gathering of IOStatistics. I'm still young in this field but have a ton of support in my company from my colleagues to reach out to the Apache community and contribute. This would be my first of many ApacheCon, and would be my biggest speaking platform until now, but you have to start from somewhere and grow with these experiences, and I'll gladly be a part of it and look forward to projects from others as well.

 