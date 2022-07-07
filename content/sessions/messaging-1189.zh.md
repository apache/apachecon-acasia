---
title: "Deep Dive into Apache Pulsar: How Two-Phase Deletion Protocol works between Storage and Metadata"
date: "2022-07-30T16:50:00"
track: "messaging"
room: "A"
presenters: "赵延"
stype: "中文演讲"
---
目前 Apache Pulsar 对于数据的删除存在两个步骤，步骤一删除元数据，步骤二删除实际存储数据。
由于这两个步骤是分开的，我们无法保证步骤二操作一定成功，因此可能导致元数据被删除成功，但是实际存储数据依然存在。现有 Pulsar 的用户在生产环境也遇到了这个问题，存在大量的脏数据无法删除。
因此，我们引入两阶段删除协议来解决以上场景。本次分享将详细介绍两段数据删除的工作原理，让 Apache Pulsar 用户和开发者更加了解该功能背后的原理和工作机制。
 ### Speakers: 
 <img src="images/speaker/1189.png" width="200" /><br>赵延: StreamNative, Software Engineer, Apche dubbo commiter/Alibaba nacos commiter/SOFAJRaft commiter. 
发表过同程旅行对于 SOFAJRaft 的探索. https://www.sofastack.tech/blog/sofajraft-in-practice-in-the-same-tour/

 