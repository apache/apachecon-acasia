---
title: "Modern ETL for Text Vector Data Using Apache SeaTunnel and Amazon Bedrock"
date: ""
track: "dataops"
presenters: "Xin Zhang"
stype: "Chinese Session"
--- 

In the wave of enterprise intelligence upgrades, information retrieval is shifting from “keyword matching” to “semantic understanding.” Traditional search engines based on inverted indexes rely on string-level matching, which makes it difficult to capture the true intent behind user queries. This limits the effectiveness of search experiences, recommendation accuracy, customer service responses, and the intelligence of knowledge-based Q&A systems.

For example, on an e-commerce platform, when a user searches for “white dress suitable for summer,” a system that only matches keywords in product titles or categories is unlikely to understand the full semantic meaning of “suitable for summer,” which may involve fabric, style, and other dimensions. Similar challenges exist in financial document search, intelligent customer service, knowledge graph associations, and more.

To address this, we aim to build a semantic search system powered by vector retrieval. The core goal is to transform text fields in business data into semantic vectors in real time, write them to a database that supports approximate nearest neighbor (ANN) vector search, and enable semantic-level information retrieval.

Using SeaTunnel’s OpenSearch Sink plugin, we can call the embedding service during the Transform stage in SeaTunnel to convert raw text fields into high-dimensional dense vectors while retaining associated IDs, tags, and metadata for downstream storage.

### Speakers:

<img src="https://sessionize.com/image/2a81-400o400o1-Jsau5kyb24ZgXpGbt5aVrk.png" width="200" /><br/>

Xin Zhang is an AWS Solutions Architect, responsible for solution consulting and design based on the AWS Cloud platform. He has a rich experience in R&D and architecture practice in the fields of system architecture, data warehousing, and real-time computing.