---
title: "When the Optimizer Lies: Debugging Cross-Slice Execution in Apache Cloudberry"
date: ""
track: "datastorage"
presenters: "Alena Rybakina"
stype: "English Session"
---

In Apache Cloudberry, the optimizer, planner, and executor operate with different abstractions of a query. When these abstractions diverge, even simple queries can trigger severe failures.
This talk presents a real bug involving Shared Scans over Common Table Expressions (CTEs) on replicated tables. When such CTEs were referenced multiple times as scalar subqueries, queries could hang indefinitely or fail with errors like "could not open existing temporary file".
The root cause was a mismatch between logical and physical execution: scalar SubPlans hid dependencies from the optimizer, leading to incorrect slice assignment and broken producer–consumer locality.
In this talk, I will walk through several alternative fixes and explain how each of them attempts to address the problem. We will dive into the optimizer internals to understand why the bug happens in the first place, how different fixes change the execution topology, and why some of them - despite working - cannot be accepted as a final solution.
Some fixes introduce subtle regressions, change plan shapes, or force fallback to the Postgres optimizer, highlighting the difficulty of making local improvements without breaking global behavior.
This talk shows how a seemingly simple query pattern can expose deep inconsistencies between optimizer and execution - and why fixing such issues often requires navigating trade-offs rather than finding a single “correct” solution.

### Speakers:


<img src="https://cdn.sessionize.com/image/62a6-400o400o1-LjXRcX4dAwc4VGESotUqiG.png" width="200" /><br/>

Alena Rybakina: Software developer, Yandex Cloud

Work Experience
Over 5 years of professional experience in database systems, including 5 years at Postgres Professional.
Main Interests
Query optimization, MVCC internals, and database statistics.
PostgreSQL Experience
More than 4 years of hands-on experience working on PostgreSQL internals, performance improvements, and optimizer-related features.
Main Projects and Contributions
Development of optimization-related extensions and features, including AQO (Adaptive Query Optimization) and Self-Join Elimination
Experimental and production-oriented improvements to the PostgreSQL query planner
Contributions to PostgreSQL core, including the OR-to-ANY and VALUES-to-ANY transformations in the optimizer

