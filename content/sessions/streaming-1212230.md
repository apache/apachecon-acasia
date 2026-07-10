---
title: "The Evolution and Production Practices of Flink 2.x in Tencent"
date: ""
track: "streaming"
presenters: "Zihao Chen"
stype: "Chinese Session"
---

1. Business Context and Architectural Evolution
  a. Business Drivers: As Tencent's business demands for real-time Lakehouse solutions and data preprocessing for Large Language Models (LLMs) surged, the iteration of the legacy 1.x version faced challenges such as high labor costs and a growing disconnect from the open-source community. 
  b. Core Value of Flink 2.x: The enhancements and optimizations introduced in Flink 2.x—spanning compute-storage separation, materialized tables, batch processing optimizations, Lakehouse architectures, and AI workflows—align perfectly with Tencent's specific business scenarios.

2. Iterative Optimization of Engine Capabilities
  To foster closer integration with the open-source community, we have fully adapted a subset of our internal capabilities to the Flink 2.x framework and are gradually contributing them back to the community. 
  a. Compute Performance:
    - Asynchronous I/O Optimization: Supports batch asynchronous I/O, boosting throughput through batching and asynchronous processing techniques.
    - Lookup Join Optimization: Supports batch asynchronous Lookup Joins.
  b. AI on Flink: Supports integration with the Triton Inference Server.
  c. Enhanced WindowStagger Consistency: Resolves inconsistencies in window assignment behavior that previously arose when enabling the WindowStagger feature.
  d. Improved O&M and Observability Capabilities:
    - Native Data Sampling: Enables zero-intrusion data probing for production tasks, thereby reducing the cost of debugging and testing real-time applications. 
    - HistoryServer Optimization: Addresses archiving bottlenecks in large-scale production clusters, ensuring the reliable traceability of historical tasks.

3. Implementation Practices Across Diverse Business Scenarios
  a. Streaming-Batch Unification: Showcases the performance improvements achieved by upgrading streaming-batch unified scenarios to Flink 2.x. 
  b. Real-time Data Streams in the AI ​​Era:
    - AI Functions: Enables the direct integration of AI model calls within Flink SQL to construct low-latency AI data processing pipelines.
    - PyFlink Performance Optimization: Focusing on advertising feature engineering scenarios, we share how optimizing the Python UDF runtime can significantly boost feature computation efficiency.
  c. Governance of Ultra-Large-Scale State: Highlights how Delta Join and BiFang are utilized to resolve issues associated with excessive state size in dual-stream Join operations.

4. Future Outlook: From Stream Computing to Intelligent Stream Computing
  a. Balancing Performance and Cost: We aim to continuously deepen the integration of incremental computing and materialized views to achieve maximum compute reuse, thereby striking the optimal balance between performance and operational cost. 
  b. Event-Driven AI Agents: Explore Flink Agents, evolving Flink from a standalone data processing engine into an event-driven streaming agent framework.

### Speakers:


<img src="https://cdn.sessionize.com/image/c17d-400o400o1-3ksWtZ8Yz4P3kYR9cEC4tH.jpg" width="200" /><br/>

Zihao Chen: Tencent, Senior Software Development Engineer

Zihao has been engaged in R&D related to the Flink kernel for many years. In recent years, he has mainly focused on driving the evolution of Flink 2.x and developing Flink's autoscaling capabilities to maintain the Flink engine's technological edge and improve the stability and resource utilization of Flink jobs.

