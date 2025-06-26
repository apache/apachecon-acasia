---
title: "A Small-file Sniffer System for Hadoop Clusters"
date: "2025-07-25T17:15:00"
track: "datastorage"
presenters: "Miao Wang"
stype: "English Session"
room: "Mtn WanShou Hall"
---

The HDFS (Hadoop Distributed File System) often encounters significant performance degradation when managing a large number of small files. Scanning all files to locate the small ones through the Namenode’s service becomes time-consuming and adds extra burdens to the Namenodes. There is a lack of research on how to identify the hotspots of small files in HDFS without querying the Namenode in a time-efficient manner. In this session, the speaker aims to introduce a big data system to identify small files in HDFS by parsing the File System Image (FSImage), which is generated periodically on the Namenode. This system allows Hadoop cluster administrators to monitor and identify small files in real time without impacting the normal operation of the Hadoop cluster. Additionally, it can serve as a tool to locate small-file hotspot tables in a Hive data warehouse.

### Speakers:


<img src="https://sessionize.com/image/aee1-400o400o1-JZ2CnJbAPD5PN5NLnF28Yk.jpg" width="200" /><br/>

Miao Wang: postal savings bank of china, data engineer

Miao obtained a Bachelor of Engineering degree from Beijing Institute of Technology and a Master degree in Eletrical and Computer Engineering from Concordia University. Currently, he serves as a Data Engineer at Postal Savings Bank of China. His interests span across distributed systems, data lakes, and big data. Additionally, he is a contributor to multiple open-source projects, including Apache Iceberg.