---
title: "Securing the Lakehouse: Identity-Aware Governance for Iceberg REST with Apache Gravitino"
date: ""
track: "datalake"
presenters: "Rory Qi"
stype: "English Session"
---

Apache Iceberg has become the de facto standard for open table formats, and the Iceberg REST Catalog is the key to decoupling compute from storage. However, while the REST specification defines how to exchange metadata, it leaves the security—authentication, authorization, and audit—as an exercise for the user. For organizations transitioning from experimental projects to production lakehouses, this "security gap" presents a significant hurdle.
In this talk, we introduce Apache REST, an open-source federated metadata lake that provides a production-ready implementation of the Iceberg REST service. We will walk through the technical architecture of how REST acts as a secure catalog proxy.
Key takeaways include:
Identity & Authentication: A deep dive into Gravitino’s support for OAuth2, Basic, Kerberos, and HTTPS to ensure only verified clients can access the catalog.
Unified Access Control: How to manage fine-grained permissions (RBAC) at the catalog, namespace, and table levels, even when using legacy backends like Hive Metastore or JDBC.
Credential Vending: How Gravitino securely provides short-lived storage credentials (S3/GCS/Azure) to clients, ensuring data-layer security is as strong as the metadata layer.
Real-world Integration: A demonstration of how Spark, Trino, and Flink can interact with a secured Gravitino Iceberg REST endpoint without custom engine forks or patches.
Whether you are a platform engineer building a multi-tenant data lake or a security architect concerned about open-source governance, this session will provide a blueprint for a secure, vendor-neutral Iceberg infrastructure


### Speakers:


<img src="https://cdn.sessionize.com/image/3df9-400o400o1-4yoKkoqsJnbKwTammtx8VP.jpg" width="200" /><br/>

Rory Qi: Apache Gravitino committer, Apache Uniffle PMC Chair

Apache Gravitino PMC member, Apache Uniffle PMC chair, ASF member, Datastrato engineer, ever worked at Tencent, Baidu

