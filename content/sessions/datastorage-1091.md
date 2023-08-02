---
title: "Bytedance 100 billion file HDFS clustering practice"
date: "2023-08-18T15:00:00" 
track: "datastorage"
presenters: "Xiong Mu"
stype: "Chinese Session"
---
With the further development of big data technology, the data scale and usage complexity are getting higher and higher, and Apache HDFS is facing new challenges. At ByteDance, HDFS is both the storage for traditional Hadoop warehouse services, the base of the storage separation architecture computing engine, and the storage base for machine learning model training.

Based on HDFS itself, the Bytedance big data storage team built a storage scheduling capability for large-scale computing resource scheduling across multiple regions to improve the stability of computing tasks. It also provides integrated user-side cache, regular triple copy, cold storage data identification and hot and cold scheduling capabilities.

This share describes how ByteDance understands the new requirements of traditional big data storage in emerging scenarios, and shares the evolution of technology and operation and maintenance systems to support different application scenarios.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230614/1208402570.png" width="200" /><br>Xiong Mu: ByteDance, Big Data Storage R&D Engineer at the Volcano Engine, mainly responsible for big data storage HDFS metadata service evolution and upper-layer computing ecosystem support.
 <br><br>