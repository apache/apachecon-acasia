---
title: "Interactive data engineering workload execution using Livy session on Kubernetes cluster"
date: "2022-07-30T16:50:00"
track: "bigdata"
room: "B"
presenters: "Anmol Chaturvedi, Haripriya Bendapudi, Praneet Sharma"
stype: "English Session"
---
In recent times, the demand for time-critical short-lived interactive spark workloads has grown tremendously. One common use case is that of data preparation wherein a pipeline of data integration steps is built through spark driven interactions with subset of data (data worksheet) and visualizing the transforming data responses in real time. This recipe of interactive spark queries is then published to be applied on petabytes of data at hyperscale.

Informatica supports these use cases through deep integration with Apache Livy on a managed Kubernetes cluster. This session will cover in detail the enhancements made to Apache Livy SDK for supporting concurrent asynchronous submission of spark code snippets (statements). Deep dive of the framework will cover the lazy deployment of Livy server as a Kubernetes service, the optimizations made in the client agent application to achieve sub second queries dispatch, and a new Java’s *CompletableFuture* based listener for asynchronous queries monitoring and results retrieval. In this talk, we will also discuss how the framework prioritizes and supports fail-fast quick dispatch mode over traditional batch workflow demands like job recovery, cluster state correctness, and lazy job resources availability to describe a few. Finally, we will summarize observed performance gains regarding job runtime achieved by this framework over a regular Spark job.
 ### Speakers: 
 <img src="images/speaker/1244.png" width="200" /><br>Anmol Chaturvedi: Informatica Corporation, Director of Engineering, Anmol Chaturvedi heads up the stack that integrates the Cloud MDM, Cloud Data Engineering engine, Cloud Profiling, and the Cloud Data Quality suites in the Elastic Serverless Cloud Data Engine platform at Informatica. He has been responsible for the Data Virtualization suite, and a native distributed data processing engine engineered in house at Informatica. He has over 15 years of experience in Enterprise Software Development relating to data management, distributed computing, and databases.

<img src="images/speaker/1244_2.png" width="200" /><br>Haripriya Bendapudi:
Senior Software Engineer, Informatica. Has been working on Cloud Data Integration Elastic product for the past 3+ years contributing towards projects that help users run real-time data integration pipelines in a time and cost-effective manner by leveraging Spark on Kubernetes. She holds a master's degree from Cornell University. Outside work she enjoys hiking and putting her culinary skills to the test.

 

<img src="images/speaker/1244_3.png" width="200" /><br>Praneet Sharma:
Principal Software Engineer at Informatica with 8 years of experience in data integration domain. Responsible for designing and implementing features in Informatica’s cloud data integration elastic and advanced serverless products by utilizing open source technologies such as Spark, Kubernetes and Livy.

 