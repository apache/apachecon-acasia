---
title: "Making Flink K8S works as your wish"
date: "" 
track: "streaming"
presenters: "赵波"
stype: "Chinese Session"
---
Let Flink run better in K8S. Now K8S has slowly entered online deployment service. In the whole process of big data technology evolution, we have higher demand for Flink job running on K8S.
1. In the case of resource shortage, we need Flink jobs to run in sequence according to certain rules.
2. The cluster resources can be configured. You do not need to manually calculate and configure Flink job resources to ensure that Flink job resources are preoccupied.
The broader needs are:
The diversity of scheduling algorithms, high efficiency of scheduling performance, seamless connection with mainstream computing frameworks, support for heterogeneous devices and so on
Volcano is responding to those needs. Meanwhile, Volcano inherits the design style and core concepts of the Kubernetes interface. Volcano is the first and only kubernetes-based container batch computing platform under CNCF, which is mainly used in high-performance computing scenarios. It provides a set of scheduling mechanisms that Kubernetes currently lacks, typically required for a variety of high-performance workloads such as machine learning big data applications, scientific computing, and special effects rendering.

Let's expand on the CNCF PodGroup concept and see how Flink on K8S and Volcano make The Flink Job work the way we want it to.
 ### Speakers: 
 <img src="images/speaker/1198.png" width="200" /><br>Bo Zhao: huawei, Engaged in the research of Flink computing framework

 