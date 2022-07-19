---
title: "In-depth practice of Apache Oozie"
date: "2022-07-29T14:10:00"
track: "workflowdatagovernance"
presenters: "张俊帆"
stype: "Chinese Session"
---
In recent years, the field of offline processing of big data is gradually mature and perfect, and in the field of offline task scheduling, that is, workflow, a variety of project tools are emerging in an endless stream. Apache's first workflow scheduler Oozie has been around for more than 10 years, while dolphinScheduler and Airflow have attracted a lot of interest, demonstrating that there is still plenty of life in the workflow scheduler space.

This presentation will bring in-depth practice of Apache Oozie as a very old project in iQiyi. It introduces Oozie functions and architecture, scale and application in IQiyi, support and transformation of Oozie task plug-ins, implementation of Roadmap for unified deployment of multiple Oozie clusters, and community contribution

This section describes Oozie functions and architecture
Oozie architecture is stateless unlike airflow and DolphinScheduler in that it has no complex master/ Slaves architecture. Each node is a master and uses the ZK coordinator to claim its own actions (i.e., jobs).

The worker design is also different from that of the well-known Dolphinscheduler. Oozie workers are not a work resource pool composed of workers, but are hosted to Hadoop Yarn cluster. Each Spark/Hive/MR/Flink(except SSH Action) is started with an Oozie Launcher.

Oozie scalability depends on Hadoop Yarn capacity and reduces Oozie management cost.
However, each Oozie launcher occupies 1core/1 gb. Oozie version 5.0 is 2core/2 gb (a MR task, and Oozie internal launcher AM implemented on Yarn after 5.x).

Oozie provides various types of Actions (similar to DolphinScheduler task types) and exposes common underlying interfaces for user extension. Oozie native supports common big data actions such as Hive, Spark, Mr, distcp, and flink Batch/Tony.

Oozie provides scheduled startup, triggering startup, SLA alarm, and node restart functions, meeting the requirements for offline scheduling of big data.
However, due to its difficult interface and complex XML configuration, Oozie is only used as the underlying scheduling engine in IQiyi, and a data development platform is built in the upper layer to provide visual drag and drop pages to enhance ease of use. However, Oozie's stateless architecture supports the development of iQiyi big data offline tasks.

Application in iQiyi
Since 2018, Oozie has supported more than 10 offline Hadoop clusters (total number of nodes + 2w) with an average of 20+ workflow offline tasks per day. Oozie not only covers offline data development such as recommendation and advertisement, but also takes part of machine learning workflow orchestration scenarios.

The initial deployment of Oozie follows Oozie design, that is, each Hadoop cluster has one Oozie cluster (usually 2 to 4 physical machines in Oozie HA mode). In this deployment mode, the underlying physical isolation is implemented. This limits the scheduling capacity of a single Oozie cluster and improves stability.

However, as services develop and Hadoop clusters are deployed in multi-machine rooms, Oozie is bound to Hadoop, which imposes heavy O&M burdens. It takes about one week to release Oozie changes online. As a result, Oozie deployment mode has been changed in depth.
In addition, the submission entry of internal offline tasks is contracted to Oozie scheduling engine, resulting in numerous requirements and extended action types, such as Flink Batch Action.


Support and modification of Oozie Action plug-in
Compatibility problems occur when the Spark task submission portal is migrated from the portal machine to Oozie in the early stage of Oozie application. Oozie's native Spark submission mode uses Hadoop distributed Cache to download the Spark JAR to the launcher task directory when the user starts the Launcher. However, if spark JAR contains some incompatible YARN dependencies in the cluster, the Spark task fails. This problem is solved completely by postponing the download of the Spark JAR until the launcher is started.

In addition, when migrating crontab tasks from the enterprise portal to the platform in the early stage, a large number of SSH actions were implemented (remote login to the Oozie portal is used to perform tasks). Therefore, several bugs and issues have been fixed for SSH Action, all of which have been reported back to the community. Some hidden bugs were also found, such as occasional scheduling deadlocks [Oozie-3646] Possible dead-lock in SignalXCommand -

In the process of oozie-based scheduling services becoming mature, we have made some new attempts and explorations, including supporting Flink Batch on Oozie and using Oozie to schedule machine learning training tasks.

Flink Batch Action is an Oozie action implemented to promote a batch stream. However, during the implementation process, it was discovered that Oozie's Hadoop Delegation Token mechanism was not yet implemented in Flink, thus contributing multiple PR to Apache Flink, such as
1. https://issues.apache.org/jira/browse/FLINK-21700
2. https://issues.apache.org/jira/browse/FLINK-21768
3. https://issues.apache.org/jira/browse/FLINK-22294
4. https://issues.apache.org/jira/browse/FLINK-22329
5. https://issues.apache.org/jira/browse/FLINK-22534

TonY (TensorFlow/PyTorch on Yarn) is also introduced in Oozie to support machine learning workflow choreography. TonY Action is implemented to connect data processing and sample generation to machine learning training

A single Oozie cluster schedules tasks in multiple Hadoop clusters
Many Hadoop clusters, including self-built and cloud clusters, and Hadoop versions vary, resulting in high O&M costs when using Oozie deployment mode. Each Hadoop cluster requires an Oozie cluster.

At the same time, we also hope to ensure HA at the cluster scheduling level for high-priority tasks. In order to achieve this goal, we developed a three-step implementation plan, from having the ability of cross-cluster scheduling, to realizing fine-grained scheduling isolation, to realizing intelligent scheduling.

In terms of the ability of cross-cluster scheduling, Oozie is also reformed with the in-depth understanding of Oozie. By separating the scheduling cluster configuration from the task cluster configuration, A single Oozie cluster schedules multiple public cloud and self-built Hadoop2.x and 3.x clusters at the same time. After modification, Oozie supports a new Hadoop cluster, which takes only a few minutes.

If tasks of multiple clusters are scheduled by a single Oozie cluster, interference between clusters may occur. Therefore, different Oozie servers can implement cluster scheduling attribution policies to isolate scheduling loads and ensure task stability (figure)

At present, iQiyi is exploring the combination of internal QBFS(a virtual file system based on Hadoop HCFS interface) to perform intelligent task scheduling, shielding the underlying physical cluster for users, and providing a unified logical resource cluster

Roadmap
1. Combined with QBFS, continue to explore the intelligent scheduling of tasks
2. Provides Oozie code version release capability with fine gray-scale precision to specify workflow and user, improving release stability

Community contribution to Oozie and related projects
1. https://issues.apache.org/jira/browse/OOZIE-3646
2. https://issues.apache.org/jira/browse/OOZIE-3379
3. https://issues.apache.org/jira/browse/OOZIE-3594
4. https://issues.apache.org/jira/browse/OOZIE-3393
5. https://issues.apache.org/jira/browse/OOZIE-3569
6. https://issues.apache.org/jira/browse/OOZIE-3574
7. https://issues.apache.org/jira/browse/OOZIE-3589
Added Flink Batch Action, Flink side compatibility
8. https://issues.apache.org/jira/browse/FLINK-21700
9. https://issues.apache.org/jira/browse/FLINK-21768
10. https://issues.apache.org/jira/browse/FLINK-22294
11. https://issues.apache.org/jira/browse/FLINK-22329
12. https://issues.apache.org/jira/browse/FLINK-22534
 ### Speakers: 
 <img src="images/speaker/1251.png" width="200" /><br>Junfan Zhang: iQIYI, Big data Engineer, The open source project
Personally participate in big data projects such as Flink/Oozie/Hadoop and maintain github.com/tony-framework/tony
Open source address: github.com/zuston

No record of past speeches

 