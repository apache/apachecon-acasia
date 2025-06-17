---
title: "Reshaping OpenTelemetry with Apache Arrow"
date: ""
track: "webserver"
presenters: "Lei Huang"
stype: "English Session"
---

OpenTelemetry is a widely adopted open-source standard for building observability frameworks, offering tools, APIs, and SDKs to generate, collect, and export telemetry data like metrics, logs, and traces. However, its transport protocol relies on Protocol Buffer messages that are stateless and easy to interpret but have a row-based structure that complicates compression. This limitation becomes more significant when transferring large volumes of data across network boundaries.

In my session, I will present a proposal to address this issue by enhancing the OpenTelemetry protocol with Apache Arrow, referred to as OTel-Arrow. This initiative aims to utilize Apache Arrow for bulk data compression and transfer in OpenTelemetry pipelines. We will discuss the OTel-Arrow data model, existing infrastructures that have implemented it, benchmark results comparing OTel-Arrow with the original implementation, and our integration of OTel-Arrow into modern time-series databases using the Apache Parquet format to facilitate fast analytics through a real-time query engine built on Apache DataFusion.

### Speakers:


<img src="https://sessionize.com/image/4df2-400o400o1-EVUc7f9M53frxPdweN8rwZ.jpg" width="200" /><br/>

Lei Huang: Database Developer at Greptime, Hangzhou, China

Lei is a passionate open-source database developer from China. After obtaining his master's degree in Computer Science from Peking University, he joined Alipay to work on infrastructure and middleware development, leading the development of a massive-scale message queue used for transaction processing. Later, he joined Greptime as a founding member, primarily responsible for the development of the storage engine. His main interests are distributed systems and database storage subsystems.
