---
title: "Large scale migration to Parquet in Uber"
date: "2022-07-31T14:10:00"
track: "bigdata"
room: "B"
presenters: "Huicheng Song"
stype: "English Session"
---
Parquet is the core file format in Uber's big data stack. It is a prerequisite for many key initiatives like column level encryption, column pruning etc. in Uber's data org.

However, there are nearly 20,000 existing Hive tables still using other formats. It is inefficient and error-prone to migrate them using the traditional SELECT-INSERT method.

We tackled the challenge with a 3-pillared solution:
  - High throughput rewriter
  - Mixed format partition support in Hive and Spark query engines
  - Reliable ETL pipeline conversion

The solution can be a reference for anyone needs to migrate massive amounts of Hive tables and data files to Parquet format
 ### Speakers: 
 <img src="images/speaker/1015.png" width="200" /><br>Huicheng Song: Uber, Senior Software Engineer, Uber software engineer, working in Big Data Security, file format unification

 