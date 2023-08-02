---
title: "BanyanDB: A highly scalable distributed tracking database"
date: "2023-08-20T14:30:00" 
track: "cloudnative"
presenters: "高洪涛"
stype: "Chinese Session"
---
Trace data is an important data source for analyzing microservice system performance and failure. It records the call link and related metrics for each request in the system. As the size and complexity of microservice systems grow, the magnitude of tracking data also increases exponentially, which brings great challenges to the storage and query of tracking data. The traditional relational database or sequential database is often difficult to meet the requirements of efficient storage and flexible query of trace data.

BanyanDB is a distributed database designed for tracking data with high scalability, high performance, high availability and high flexibility. BanyanDB uses a time series-based sharding strategy that divides tracking data into multiple shards based on time ranges, each of which can be stored, replicated, and load balanced independently. BanyanDB also supports multi-dimensional indexing, which allows tracking data to be quickly filtered and aggregated according to different dimensions.

In this talk, we will introduce the design idea, architecture and implementation details of BanyanDB, as well as its application and effects in real scenarios. We will also show how BanyanDB compares and benefits to other databases, as well as its future direction and plans.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230522/0032233353684942.jpeg" width="200" /><br>Gao Hongtao: Tetrate, Founding engineer, Founding engineer of American servicemesh service provider tetrate. Former Huawei software development cloud technology expert, has rich experience in the design, development and implementation of cloud native products. In-depth knowledge of distributed database, container scheduling, microservices, ServicMesh and other technologies.
He is currently a core contributor to Apache ShardingSphere and Apache SkyWalking and is involved in the commercialization of the open source project in the software development cloud. Former Dangdang system architect, open source expert, has participated in Elastic-Job and other well-known open source projects. Rich experience in open source project management, promotion and community operation.
Actively participate in technology sharing, and have shared in a number of technology conferences, including DTCC, ArchSummit, Top100, Oracle Carnival, etc. He has published articles in various media, such as InfoQ, OSChina, etc
 <br><br>