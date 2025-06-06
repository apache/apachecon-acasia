---
title: "How to handle your Star schema in the Streamhouse world"
date: ""
track: "streaming"
presenters: "Alexey Novakov"
stype: "English Session"
--- 

Almost every company who wants to build its own data platform for business analytics goes through a scenario of denormalizing their original data model from OLTP space in their data warehouse or lakehouse space. The end goal is to build some useful reports and power some real time business dashboard. While doing this, data teams may make many sub-optimal solutions and attempts in terms of data freshness, infrastructure cost and cost of maintenance. The challenge is to find proper solution and tools to join all the 10 or 20 tables (dimensions) with the single “fact” table. Taking into account that all data in tables, which is coming from OLTP system, is always in flux, as it is ingested as a data stream.

In this talk I will show you how you can tackle this typical use case which most of the companies during their data warehousing journey want to build. We will do that based on Ververica’s Streamhouse architecture using unified storage and compute components like Flink CDC and Apache Paimon.



### Speakers:

<img src="https://sessionize.com/image/a61c-400o400o1-HAF3PCbZfVSFWcBNV3JJu6.jpg" width="200" /><br/>

I am a Solution Architect working for last the last 6 years on data solutions and products. At Ververica I am focusing on supporting clients to solve their challenges in adopting data stream processing with Apache Flink. Among my previous project and companies I developed different systems such as Data Lakes, Data Integration and Data Virtualization Layers. In my spare time, I contribute to various open-source projects or start my own for fun. Apart from programming I have some hobbies like astronomy, playing music and gym.