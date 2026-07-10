---
title: "Optimizing Apache YARN Clusters Using Intelligent Overcommitment"
date: ""
track: "datastorage"
presenters: "Sumit Puri, Wasif Khan"
stype: "English Session"
---

Apache YARN clusters running compute frameworks such as Apache Spark, Apache Tez, and MapReduce often face major inefficiencies due to static, user-defined resource allocations. This leads to over-provisioning, low utilization, and increased infrastructure costs, while requiring continuous manual tuning to maintain performance.
This talk introduces a method to Optimize Yarn, which improves cluster efficiency through a real-time, intelligent approach to resource management. By understanding workload behavior over time and combining it with live cluster conditions, the solution can make dynamic decisions that improve how resources are utilized across nodes without requiring application changes.
The solution is designed with planned safeguards to ensure stability and reliability in production environments, enabling organizations to adopt it without risking application performance or service-level objectives.
This talk shares a result-driven approach that delivered substantial improvements. Container throughput increased from under by 100%, while application throughput improved from approximately 28.5%. At the same time, the number of active YARN nodes required was reduced by 33%, directly resulting in a reduction of the infrastructure footprint. These gains were driven by significantly improved CPU and Memory utilization across the cluster.
By enabling smarter, real-time resource allocation, this methodology can help organizations increase throughput, reduce infrastructure costs, and simplify cluster operations.

Refer to this Blog for a detailed explanation along with a video demo : https://engineering.acceldata.io/how-we-optimized-yarn-clusters-using-intelligent-overcommitment/


### Speakers:


<img src="https://cdn.sessionize.com/image/5502-400o400o1-Xudbf8rTBpCFNcw8zQnqsN.jpg" width="200" /><br/>

Sumit Puri: Senior Software Engineer, Acceldata Inc.

Sumit Puri is a Senior Software Engineer at Acceldata, working on large-scale data infrastructure and resource optimization systems. His work focuses on improving cluster efficiency across YARN and Kubernetes environments through intelligent resource management, real-time telemetry, and predictive modeling.

He has hands-on experience building distributed systems using Go, Kubernetes, and big data frameworks such as Spark and Tez. His recent work explores node-level optimization strategies, workload fingerprinting, and adaptive overcommitment techniques to maximize infrastructure utilization while maintaining stability.


<img src="https://cdn.sessionize.com/image/0c3f-400o400o1-K7zab49Sy9ANFPEDSgMzt6.jpg" width="200" /><br/>

Wasif Khan: Principal Engineer, Acceldata

Principal Engineer at Acceldata, working on big data observability solutions

