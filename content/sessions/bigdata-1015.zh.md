---
title: "大规模迁移到Uber的Parquet"
date: "2022-07-31T14:10:00"
track: "bigdata"
room: "B"
presenters: "Huicheng Song"
stype: "英文演讲"
---
Parquet是Uber大数据栈的核心文件格式。在Uber的数据组织中，这是许多关键举措的先决条件，比如列级加密、列修剪等。

然而，有将近2万个现有的Hive表仍然使用其他格式。使用传统的SELECT-INSERT方法迁移它们效率低下，而且容易出错。

我们通过三个方面的解决方案来应对这一挑战:
—高吞吐量重写器
—Hive、Spark查询引擎支持混合格式分区
-可靠的ETL管道转换

该解决方案可以作为任何需要将大量Hive表和数据文件迁移到Parquet格式的人的参考
 ### Speakers: 
 <img src="images/speaker/1015.png" width="200" /><br>Huicheng Song:  高级软件工程师, 优步软件工程师，大数据安全，文件格式统一

 