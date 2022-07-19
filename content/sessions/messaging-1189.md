---
title: "Deep Dive into Apache Pulsar: How the Two-Phase Deletion Protocol Works between Storage and Metadata"
date: "2022-07-30T16:50:00"
track: "messaging"
room: "A"
presenters: "Yan Zhao"
stype: "Chinese Session"
---
There are two steps to delete data in Apache Pulsar: delete metadata and actual stored data.
As these two steps are separated, we may not know precisely whether the second step is successful. This means the metadata may be deleted successfully, but the actual stored data could still exist. This issue has also occurred in production as reported by existing Apache Pulsar users, resulting in a large amount of dirty data that could not be deleted.
To solve this problem, we can introduce a two-phase deletion protocol. This session will deeply examine how the deletion protocol works, so that Pulsar users and developers can better understand it.
 ### Speakers: 
 <img src="images/speaker/1189.png" width="200" /><br>Yan Zhao, StreamNative Software Engineer, Apache Dubbo Committer, Alibaba Nacos Committer, and SOFAJRaft Committer. He wrote an article about how LY.COM explored SOFAJRaft: https://www.sofastack.tech/blog/sofajraft-in-practice-in-the-same-tour/.

 