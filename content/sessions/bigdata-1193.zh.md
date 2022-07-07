---
title: "大数据Python生态在传智教育的实践和思考"
date: "2022-07-31T16:50:00"
track: "bigdata"
room: "B"
presenters: "张敬存,赵晨杰"
stype: "中文演讲"
---

在大数据和人工智能领域，Python占比越来越高，其中Spark3.0的版本升级中曾经提到Python语言现在是Spark使用最广泛的语言之一，Python语法的简洁易学，为企业快速解决大数据生态问题提供了强有力支持。大数据的Python生态主要目标亮点：①将大数据的计算能力输出给Python用户，通过为大数据组件提供一系列的Python API，方便Python语言比较熟悉的用户开发大数据作业，如PySpark，PyFlink等 ②将Python生态基于大数据存储和计算进行分布式化，使用Python库的API，但是底层计算引擎使用大数据计算引擎，如TensorFlow On Flink，SparkTorch，Flink-onnx-Pytorch。
在这个讲座中，我们将讨论传智教育在大数据Python生态针对实时推荐业务线的最佳实践和思考，项目从Pulsar中实时读取数据，由于需要用到Alink机器学习库构建离线特征、在线状态训练与更新模型及通过对应推荐算法提供召回和排序服务，该包更好支持Python语言，故也选择了基于流批一体架构的PyFlink进行数据处理与统计分析，构建用户画像平台；此外我们还将讨论实时推荐业务模块根据线上反馈数据进行在线学习，实时快速进行模型调整，形成闭环系统。最后，我们将讨论一个大数据Python生态完整推荐系统最优解决方案，以将上述的内容都呈现在实践中。
 ### Speakers: 
 <img src="images/speaker/1193.png" width="200" /><br>张敬存: 江苏传智教育科技有限公司, 资深研究员, 张敬存，传智教育资深研究员；15年Java/大数据开发经验；专注于实时计算，为PyFlink贡献超过10个PR。

 <img src="images/speaker/1193_2.png" width="200" /><br>赵晨杰: 江苏传智教育科技有限公司, 资深研究员, 传智教育资深研究员，专注ML/DL/PR/KG领域相关算法的应用。

 