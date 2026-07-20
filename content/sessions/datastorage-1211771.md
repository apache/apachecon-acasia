---
title: "HBase Function Iteration and Architecture Evolution Practice at Xiaomi"
date: "2026-08-07T15:45:00"
track: "datastorage"
presenters: "Yuting sun, Yiming Gong"
stype: "Chinese Session"
room: "Mtn WanShou Hall"
---

2. Description：
This session will introduce the function iteration and deployment architecture evolution of HBase system at Xiaomi Group, as well as the work done in stability, performance and cost optimization, including dictionary compression, data structuring, SQL engine capabilities, containerization, and storage-compute separation.
3. Presentation Outline
3.1 Data Compression and Storage Optimization
Dictionary Compression Technology
- Core Principle: Build auxiliary compression structure based on high-frequency byte sequences
- Technical Features: Compression/decompression using the same dictionary, particularly suitable for structured data with repetitive patterns
- Practical Results: Significantly reduce storage costs and improve I/O efficiency
3.2 Observability and Governance Capabilities
Table Lineage Feature
- Functionality: Implement lightweight table lineage collection capability
- Collected Information: Client version, IP address, Kerberos account, and other key metadata
- Application Value: Support one-click lineage query for data governance and issue troubleshooting
3.3 Consistency and Availability Trade-offs
HBase AP Practice Exploration
- Positioning Shift: Exploration from CP (consistency priority) to AP (availability priority)
- Tiered Strategy: Set consistency priority levels for tables
- Degradation Mechanism: Prioritize service recovery for tables with lower consistency requirements, rather than waiting for complete data recovery
3.4 Version Upgrade Practice
3.x Version Implementation
- Validation Strategy: Build independent test clusters for functionality and stability verification
- Gradual Rollout: Progressively deploy community 3.x version in production environment
- Lessons Learned: Challenges and best practices during version upgrade
3.5 Data Structuring Transformation
HBase Table Schema Definition
- Pain Points: Address the issue that native HBase only has column family-level constraints, lacking column-level type definitions
- Solution Design: Define field types and field-to-column-family/column mapping relationships
- Benefits:
  - Unified table structure management for business teams
  - Automatic serialization/deserialization
  - Foundation for SQL engine capabilities
3.6 SQL Engine Capabilities
SQL Semantics Implementation Based on Structuring
- Technical Foundation: Built upon data structuring achievements
- Core Capabilities: Implement standard SQL query semantics
- Usability Improvements:
  - More convenient console queries
  - Friendlier offline job data access
  - Lower barrier to entry and improved readability
3.7 HBase Containerization
- Deployment Method: Deploy containerized Master and RegionServer processes based on Kubernetes
- Capability Enhancements:
  - Improved elastic scaling
  - Higher resource utilization
  - Enhanced operation automation
3.8 HBase Storage-Compute Separation Architecture
- Technical Solution: Implement storage-compute separation based on JuiceFS + Object Storage
- Cost Reduction Impact: Significantly reduce storage costs
- Key Technologies:
  - Smooth file system migration solution
  - Interface adaptation and performance tuning
  - Ensure seamless migration for business services

---
4. Summary
Through the above series of technical evolution, Xiaomi HBase system has achieved dual goals of performance improvement and cost optimization while ensuring business stability, providing practical reference for the evolution of large-scale distributed storage systems.

### Speakers:


<img src="https://cdn.sessionize.com/image/f58e-400o400o1-94JMLSeRT14HWn8mTYNdUm.png" width="200" /><br/>

Yuting sun: Storage R&D Engineer

Xiaomi software R&D engineer, mainly responsible for HBase development


<img src="https://cdn.sessionize.com/image/c543-400o400o1-PaMvtfz6PJnDHzzhvx71Me.jpg" width="200" /><br/>

Yiming Gong: Xiaomi, SDE

HBase developer at xiaomi