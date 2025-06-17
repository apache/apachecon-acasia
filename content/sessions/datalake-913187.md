---
title: "Xiaomi's Efficient Data & AI Optimization with Apache Paimon"
date: ""
track: "datalake"
presenters: "Houliang Qi"
stype: "Chinese Session"
---

This session will primarily focus on how Xiaomi leverages Apache Paimon to enhance efficiency and reduce costs in its information-based data warehouse, AI data warehouse, and LLM data processing. Additionally, we will discuss how we utilize JuiceFS to support Paimon's multi-cloud storage capabilities. Finally, we'll introduce the application of Apache Gravitino in managing Paimon's metadata.
Outline:
1. Application Practice of Apache Paimon in the Information-based Data Warehouse
  - We will elaborate on how we employ Paimon as a dimension table to replace Iceberg and HBase. By doing so, we not only meet the business's timeliness requirements but also achieve a 31% cost reduction. Moreover, we'll explain how we use custom lookup shuffle and remote storage as a lookup cache to accelerate the lookup join process, resulting in a remarkable 60x performance improvement for lookup joins.
2. Application Practice of Apache Paimon in the AI Data Warehouse
  - In the advertising algorithm model, the quantity and timeliness of sample data play a crucial role. Before the introduction of Paimon, our offline and real-time sample data were processed through separate pipelines. The offline samples were joined using Spark Join, which led to low timeliness in overall data output and incurred substantial computational costs. Additionally, the offline and real-time sample architectures were two distinct systems, resulting in low development efficiency. By introducing Paimon's partial update function, we enabled real-time sample joining, reducing the time required to generate model training samples from days to hours.
3. Practice of Apache Paimon in LLM Data Preprocessing
  - In LLM data preprocessing, data deduplication is a vital step. We will introduce how to take advantage of Paimon's primary key table and the aggregation merge engine features to simplify the LLM data preprocessing workflow.
4. Construction and Practice of Apache Paimon's Multi-cloud Storage Capabilities
  - The cloud-native lakehouse architecture is the emerging trend. At Xiaomi, we have built multi-cloud storage capabilities based on JuiceFS. This approach can mask the differences in underlying storage (such as OSS/Blob/KS3/S3) for our business applications. Not only does it address issues like high costs of self-built HDFS storage and occasional slow nodes, but it also harnesses the benefits of cloud storage, including low cost, high scalability, and high reliability, to meet the business's needs for storing massive amounts of data.
5. Unified Practice of Metadata Lake Based on Gravitino
  - We will introduce how to use Gravitino to manage Paimon's metadata. We'll explore how Gravitino can be used to unify metadata across data lakes and discuss the advantages that unified metadata brings to our data management processes.

Through this sharing, users will learn how Xiaomi leverages Apache Paimon to optimize data/AI warehousing and LLM preprocessing for efficiency and cost savings, enables multi-cloud flexibility with Paimon, and unifies metadata management using Apache Gravitino.

### Speakers:


<img src="https://sessionize.com/image/8968-400o400o1-XFskLG5iSQjayU8GPBBL9V.jpg" width="200" /><br/>

Houliang Qi: Xiaomi

PMC member of Apache IoTDB and Apache TsFile. Software R&D Engineer at Xiaomi, specializing in the development and implementation of Xiaomi's datalake platform.

