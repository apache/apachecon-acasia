---
title: "Accelerate Spark Queries with Gluten and Velox Engine on Arm64"
date: "2025-07-25T14:30:00"
room:  "WanChun Hall"
track: "datalake"
presenters: "Yuqi Gu"
stype: "Chinese Session"
---

Apache Spark SQL provides a robust solution, enabling users to process massive datasets efficiently. Recently, Project Gluten was introduced as an Apache Arrow-based native SQL engine designed to enhance Spark SQL's capabilities. Concurrently, several vectorized SQL engines with vibrant open-source communities have gained traction. Among them, the Meta-led Velox project stands out as a promising vectorized database acceleration library.

The Gluten-Velox integration represents a significant leap forward, delivering an optimized Spark SQL accelerator tailored for the Arm platform. By leveraging Gluten-Velox, Spark SQL overcomes the limitations of its traditional row-based data processing and JVM constraints on Arm64 architectures. This is made possible through the vertical composability of Arm64 SIMD capabilities and advanced vectorized execution techniques.

In this talk, we will provide a brief introduction to the native engines Gluten and Velox and explore the enablement of Gluten and Velox on Arm64, presenting experimental results that demonstrate the potential of this approach on the Arm Neoverse N2 platform. Additionally, we will discuss an optimization case for Velox on Arm64, showcasing strategies to further enhance performance.


### Speakers:


<img src="https://sessionize.com/image/c0c6-400o400o1-ssHnQc9M2G2yMbua5opioP.jpg" width="200" /><br/>

Yuqi Gu: Apache Bigtop and Ambari PMC member (guyuqi@apache.org)

- Work at Arm China. Collaborate closely with Arm Infra LoB. The role involves promoting ARM infrastructure products (server and networking) from initial evaluation to final deployment. 
- Apache Bigtop PMC member, Apache Bigtop former Chair (2021~2023).
- Apache Ambari PMC member, Committer.
- guyuqi@apache.org