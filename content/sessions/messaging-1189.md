---
title: "Deep Dive into Apache Pulsar: How Two-Phase Deletion Protocol works between Storage and Metadata"
date: "" 
track: "messaging"
presenters: "赵延"
stype: "Chinese Session"
---
At present, Apache Pulsar has two steps to delete data: step 1 delete metadata and Step 2 delete actual stored data.
Because the two steps are separated, the success of step 2 cannot be guaranteed. As a result, the metadata may be deleted successfully, but the actual stored data still exists. Existing users of Pulsar also encountered this problem in production, where there was a large amount of dirty data that could not be deleted.
Therefore, we introduce the two-phase deletion protocol to solve the above scenarios. In this post, you will learn more about how two sections of data removal work, so that Users and developers of Apache Pulsar can better understand how this feature works.
 ### Speakers: 
 <img src="images/speaker/1189.png" width="200" /><br>Yan Zhao: StreamNative, Software Engineer, Apche dubbo commiter/Alibaba nacos commiter/SOFAJRaft commiter.
Made with trip for SOFAJRaft exploration. https://www.sofastack.tech/blog/sofajraft-in-practice-in-the-same-tour/

 