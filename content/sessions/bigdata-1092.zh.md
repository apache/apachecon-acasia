---
title: "使用Apache Kafka、Apache Pinot和Streamlit构建实时分析仪表板"
date: "" 
track: "bigdata"
presenters: "Dunith Dhanushka, Karin Wolok"
stype: "英文演讲"
---
当你听到“决策者”，你会很自然地想到“C-suite”或“executive”。

但如今，我们都是决策者。餐馆老板、博客作者、大卖场购物者和就餐者都需要做出重要的决定，需要立即采取行动的见解。企业需要获得快速、新鲜的分析，为像我们这样的终端用户提供这些见解。

在这个会话中，我们将学习如何使用Apache Kafka, Apache Pinot和Streamlit在流数据源之上构建我们自己的实时分析应用程序。Kafka是一个用于实时工作负载的分布式、开源的发布-订阅消息和流媒体平台，Pinot是一个用于超低延迟分析的OLAP数据库，Streamlit是一个基于python的工具，可以轻松构建数据驱动的应用程序。

在介绍了这些工具之后，我们将使用Kafka的Python客户端将数据流传输到Kafka中，将数据吸收到一个Pinot实时表中，并使用Pinot的Python SDK编写基本查询。完成之后，我们将使用自动刷新的Streamlit仪表板将所有内容结合在一起，以便在发生数据更改时查看数据更改。将有许多图表和其他可视化!

这个会话是针对想要快速理解流数据的应用程序开发人员和数据工程师的。
 ### Speakers: 
 <img src="images/speaker/1092.png" width="200" /><br>Dunith Dhanushka: StarTree, 开发人员主, Dunith Dhanushka是一位经验丰富的IT专业人士，在大型事件驱动系统的架构、构建和咨询方面拥有超过十年的经验。他对探索企业数据管理领域的创新尤其感兴趣，包括流媒体平台、实时分析和分布式数据库。Dunith目前是StarTree的一名开发者。

 <img src="images/speaker/1092_2.png" width="200" /><br>Karin Wolok: StarTree, 开发者社区和营销主管, Karin目前是StarTree开发者关系团队的开发者社区编程负责人，StarTree是Apache Pinot的创始人创立的初创公司。Karin最初的职业生涯是在娱乐营销领域，与艾米纳姆和Live Nation等公司合作。她还在美国的两个主要城市成功地建立了一个职业女性网络，为当地的数据科学聚会组织了活动，并帮助领导了一场正在进行的黑客马拉松，将机器学习交到癌症生物学家手中。她的数据工作之旅最终让她成为了世界领先的图形数据库Neo4j的社区开发项目经理。最近，她加入了StarTree，以改善整个开发者社区的采用和成功。

 