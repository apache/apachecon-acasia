---
title: "Apache Ozone: Auto File Expiration and Removing through S3 Lifecycle Configuration"
date: ""
track: "datastorage"
presenters: "Chen Xi, Sammi Chen"
stype: "中文演讲"
---

Apache Ozone is a distributed storage system in the Hadoop ecosystem. It supports both Hadoop Filesystem and AWS S3 compatible RESTFull API. In a distributed storage system in the big data ecosystem, normally some files are short lived temporary data, and some files are long lived permanent data, system administrators or users have to manually remove the temporary files when they are not used anymore. In this session, we will introduce the new feature S3 Lifecycle Configuration - Object Expiration, which will be released soon in the next Ozone 2.2.0 release, about how the S3 Lifecycle Configuration - Object Expiration feature is designed, how to use the feature to automatically expiration and removing temporary files by setting lifecycle configuration on target bucket, and share the experience of this feature in production environment.

### 讲师:


<img src="https://cdn.sessionize.com/image/219f-400o400o1-7Sfo2ovJpEL8bf4Ev34E9n.jpg" width="200" /><br/>

Chen Xi: Storage Expert Engineer, Data Infrastructure at Shopee

Experienced in the storage domain, with a strong focus on distributed storage systems and performance optimization. Currently working in Shopee’s Data Infrastructure team, responsible for storage product development.


<img src="https://cdn.sessionize.com/image/f062-400o400o1-JwG1ArqNeWcX7KNGJHGgSv.jpg" width="200" /><br/>

Sammi Chen: Cloudera Principal Storage Engineer 

Cloudera principal storage engineer,  focusing on Apache Hadoop and Apache Ozone kernel development, currently being the Chair of Ozone PMC and Hadoop PMC, former big data storage tech leader of Tencent and Intel. 

