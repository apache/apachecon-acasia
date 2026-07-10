---
title: "Lean Metadata, Big Data: Keep the Query Fast in Apache Iceberg"
date: ""
track: "datalake"
presenters: "Hongyue Zhang"
stype: "English Session"
---

Apache Iceberg's metadata layer is what makes schema evolution, partition evolution, and predicate pushdown possible . But at petabyte scale, that metadata itself can balloon to hundreds of gigabytes or more. When planning slows down the execution, something has to give.

This talk explores how Iceberg's metadata is structured through manifests, partition summaries, and column-level metrics, and why each layer exists to enable fast analytical queries. We'll then walk through Iceberg's native APIs, procedures and practical strategies for applying them to keep metadata size in check at scale. Finally, we'll preview proposals in the Iceberg v4 spec that aim to make metadata more compact and scalable by default.

You'll walk away with a clear picture of where all those gigabytes of metadata actually come from, a playbook for keeping them in check in an iceberg's own way, and enough context on the v4 spec to start contributing and where the format heads next.


### Speakers:


<img src="https://cdn.sessionize.com/image/1050-400o400o1-3JfnogDnkgNnwSMLv7LeQm.jpg" width="200" /><br/>

Hongyue Zhang: Software Engineer at Snowflake

Hongyue started to contribute to apache iceberg project since 2022 while work on Apple data platform. Now at Snowflake, he is building tools and systems around Apache Iceberg to help make data-driven decisions.

