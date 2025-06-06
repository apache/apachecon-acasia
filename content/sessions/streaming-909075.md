---
title: "Scalable Join & Aggregation with External State and Dynamic Tables"
date: ""
track: "streaming"
presenters: "Feng Jin"
stype: "Chinese Session"
--- 

	1.	Background & Motivation
	•	Flink SQL challenges at scale: large state, long joins, complex maintenance
	•	Business use case: automotive data warehouse and alerting systems
	2.	State Externalization with Delta Join and Merge Engine
	•	Delta Join: external dimension tables with up-to-date snapshots
	•	Merge Engine: external upsert tables for aggregation results
	•	How we minimized internal state while ensuring correctness and latency
	3.	The Role of Dynamic Tables
	•	Intermediate table explosion: a hidden cost of state externalization
	•	How Dynamic Tables automate schema creation, lifecycle, and data lineage
	•	Empowering developers: write business logic, forget the plumbing
	4.	Enabling Batch-Stream Unification
	•	Lightweight Flink state: only track offsets
	•	Same SQL logic for both real-time and backfill workflows
	•	Practical benefits in backfills, audits, and reprocessing
	5.	Results & Lessons Learned
	•	Developer experience and productivity gains
	•	Improved job resilience and observability
	•	Where we’re going next: tighter integration with metadata and scheduling



### Speakers:

<img src="https://sessionize.com/image/849a-400o400o1-JY6LVQLecrGWcQHMZZkw7V.jpg" width="200" /><br/>

Feng Jin is currently a member of the Compute Platform team at Xiaomi, where he is responsible for maintaining the internal Flink framework and building the company’s real-time lakehouse architecture. He has extensive experience in large-scale stream processing, Flink SQL optimization, and state management. He is also an Apache Flink committer and actively contributes to the open-source community.