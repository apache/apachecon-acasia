---
title: "Lakehouse to AI Data Lake: Xiaomi AI scene data storage and computing architecture evolution"
date: ""
track: "datalake"
presenters: "Kainan Bao"
stype: "Chinese Session"
---

While the lakehouse architecture has become the de facto standard for business intelligence (BI) workloads, it faces two fundamental bottlenecks when extended to large-scale foundation model training pipelines. Unlike traditional BI which centers on structured tabular data, AI training processes massive volumes of unstructured data (text, images, audio, video), exposing critical gaps in unified unstructured data governance and architectural silos between Hadoop-based data processing and cloud-native model training infrastructure.

This session presents Xiaomi's production-proven two-phase architecture evolution to address these challenges. Phase 1 integrates unstructured data into a unified metadata governance layer using Gravitino and Fileset, and enables seamless interoperability between cloud object storage and the Hadoop ecosystem via GVFS. Phase 2 adopts a Ray-Lance stack that transcends the limitations of the traditional Hadoop stack, leveraging Ray as the cloud-native distributed computing engine and Lance as the AI-optimized storage format. Attendees will learn practical implementation details and real-world performance gains from production use cases including incremental data deduplication and multimodal data management.

### Speakers:


<img src="https://cdn.sessionize.com/image/a5e2-400o400o1-GdvaUKeFWkpXjmo5rWQVTC.jpg" width="200" /><br/>

Kainan Bao: Software Engineer at Xiaomi | Core Contributor of Xiaomi Mimo Models | Contributor of Iceberg, Paimon & Gravitino

Software Engineer at Xiaomi and a Core Contributor of Xiaomi Mimo Models, responsible for PB-scale data processing for Xiaomi Mimo foundation model training. Specializes in solving the unique challenges of processing massive volumes of multimodal unstructured data including text, images and video.

Has extensive experience in data lake governance, with contributions to the Iceberg, Paimon & Gravitino open source communities. In this session, will share how Xiaomi evolved its traditional data lake to unify structured and unstructured data governance with Gravitino, and built AI-native data processing systems using Ray and Lance.

