---
title: "Apache Cloudberry: gathering statistics for queries executed by multiple PostgreSQL instances."
date: ""
track: "observability"
presenters: "Leonid Borchuk"
stype: "English Session"
---

Let's say you have Apache Cloudberry cluster that consists of several PostgreSQL instances. They all execute a single query, and you want to collect general statistics on how many resources were spent on executing this query. The built-in pg_stat_statements module is no longer suitable here, since it works within the same database. I will present a solution with a similar central idea — collecting data through query execution hooks, but instead of storing it in PostgreSQL shared memory, we send raw data to an external agent process. This process is responsible for aggregating metrics, providing a unified picture across all instances, as well as additional functions, such as the forced termination of problematic sessions, while not limited to PostgreSQL: the solution can collect data from other system components. I will talk about architecture, product tasks, and share links to the repositories (Apache 2.0 License) with the code.

### Speakers:


<img src="https://cdn.sessionize.com/image/429e-400o400o1-X15FYUcE9UQzxFpN9AkBKZ.png" width="200" /><br/>

Leonid Borchuk: Developer at Yandex Cloud, Moscow. Apache Cloudberry commiter

Team lead of the MPP postgres development team at Yandex.Cloud. He started his career with the administration of large commercial universal and analytical databases. But now he's finally writing his own. Apache Cloudberry commiter.

