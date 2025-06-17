---
title: "Apache Polaris (Incubating) & Apache XTable: Unifying Iceberg, Hudi, and other Table Formats"
date: ""
track: "datalake"
presenters: "Eric Maynard"
stype: "English Session"
---

Apache Polaris (Incubating) implements the Apache Iceberg REST catalog specification and allows users to manage Iceberg tables, views, and other related metadata. Role-based access control governs which users have access to what data, and Polaris supports attaching policies to tables in order to categorize data and to configure table maintenance.

A new integration with Apache XTable promises to extend this same functionality to non-Iceberg tables. Polaris recently introduced "generic tables" -- allowing users to manage their Apache Hudi tables within Polaris alongside tables backed by Apache Kafka or other systems. With XTable, clients can now connect to Polaris and read data originally written in Iceberg as if it were written in Hudi without ever needing to think about table formats.

This talk will outline the new generic tables and conversion features in Polaris, how to configure XTable to power conversion, and will briefly review the design and implementation of the integration.


### Speakers:


<img src="https://sessionize.com/image/d65d-400o400o1-LvXU1jeMwf7eRJ4iZsGDwd.png" width="200" /><br/>

Eric Maynard: Data Interoperability @ Snowflake

Eric Maynard is an engineer at Snowflake working on Apache Iceberg, Apache Polaris (Incubating), and the translation of (meta)data between formats.

