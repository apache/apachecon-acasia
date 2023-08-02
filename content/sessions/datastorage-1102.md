---
title: "Xiaomi HDFS data governance practices and evolution"
date: "2023-08-19T15:00:00" 
track: "datastorage"
presenters: "王成伟"
stype: "Chinese Session"
---
Introduction: This sharing focuses on the background of HDFS data governance in Xiaomi, and the data governance practice and evolution based on the hierarchical storage of hot and cold data, as well as the subsequent data governance planning.
Outline:
1. Background
This section describes the current status of HDFS in Xiaomi, and the reasons and purposes for HDFS data governance.
1. Practice and evolution
- Definition and analysis of cold data
This section mainly introduces the definition of cold data in small meters, and the method of analyzing and locating cold data.
- Tiering v1 solution Description
This section describes the Tiering v1 solution that uses fuse to mount S3 storage as an Archive disk to store cold data based on the HDFS heterogeneous storage function. It includes the architecture and principle of the Tiering v1 scheme, as well as the advantages and problems.
- Tiering v2 solution Description
This section describes the Tiering v2 solution for accessing public cloud S3 by modifying HDFS. The principles and overall architecture of the Tiering v2 solution are included. HDFS modification; How to dump cold data to S3? How to read cold data in S3; How to GC cold data stored in S3; Advantages and existing problems.
1. Summary and outlook
This section describes the implementation results of HDFS data governance and future planning, such as supporting direct HDFS write to S3 and append cold data in S3.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230601/1422115780.png" width="200" /><br>Wang Chengwei: millet, Senior software development Engineer, Xiaomi senior software development engineer, HDFS Contributor, many years of HDFS optimization and maintenance experience. In Xiaomi, I was mainly responsible for HDFS optimization and maintenance.
 <br><br>