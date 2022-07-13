---
title: "存储与元数据双管齐下：深入探究 Apache Pulsar 双阶段删除协议的工作原理"
date: "2022-07-30T16:50:00"
track: "messaging"
room: "A"
presenters: "赵延"
stype: "中文演讲"
---
目前，Apache Pulsar 对于数据的删除存在两个步骤，即删除元数据与实际存储数据。
由于这两个步骤互相分开，我们无法保证实际存储数据一定能被删除，因此可能存在元数据已删除而实际存储数据依然存在的现象。现有 Pulsar 的用户在生产环境也遇到了该问题，存在大量的脏数据无法删除。
对此，我们可以引入两阶段删除协议来解决该问题。本次分享将详细介绍两段数据删除的工作原理，让 Apache Pulsar 用户和开发者更好地了解该功能背后的原理和工作机制。
 ### Speakers: 
 <img src="images/speaker/1189.png" width="200" /><br>赵延，StreamNative 软件工程师，Apache Dubbo Commiter，Alibaba Nacos commiter 以及 SOFAJRaft Commiter。
曾发表过同程旅行对于 SOFAJRaft 的探索：https://www.sofastack.tech/blog/sofajraft-in-practice-in-the-same-tour/.
 