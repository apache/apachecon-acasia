---
title: "Impala on Iceberg with Puffins"
date: "2025-07-26T15:00:00"
room:  "WanChun Hall"
track: "datalake"
presenters: "Daniel Becker"
stype: "English Session"
---

The Apache Iceberg table format has become a de-facto standard in the Big Data world. Its numerous advantages over traditional file system based table formats - like row level modifications, transactions, partition transforms and time travelling - have made it a natural first choice for many projects.

Statistics about the data can be of immense help to database engines in creating efficient query plans. As a leading table format, Iceberg aims to provide a standardised way of storing these statistics: in addition to file level attributes already present in the core specification (like min and max values), it has introduced the Puffin file format for storing statistics over the whole table. By using the Puffin format, various database engines can share statistics instead of each having to compute and store its own version, making multi-engine workflows simpler and more efficient.

This talk will show you how we introduced support for Puffin stats in Apache Impala, an open-source, distributed, massively parallel database engine. We will go through all the stages of implementation, from only reading statistics that were computed for the latest snapshot, through optimising read performance, to also taking into account stats for older snapshots where they are missing for more recent ones. A particularly interesting point we will discuss is how we choose the most relevant stats when they are available from multiple sources: both from Puffin files and Impala’s traditional source of statistics, the Hive Metastore.

### Speakers:


<img src="https://sessionize.com/image/6933-400o400o1-72rRP3UXJeo1bZhvM4bFDm.jpg" width="200" /><br/>

Daniel Becker: Senior Software Engineer

Daniel Becker started working on Apache Impala in 2019 at Cloudera. His Impala contributions encompass various topics, including LLVM code generation, complex types, Parquet and Iceberg. He is a member of the Apache Impala PMC and has a degree from Pázmány Péter Catholic University.