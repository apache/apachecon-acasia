---
title: "Apache Http服务器的可观察性解决方案"
date: "2022-07-29T16:00:00"
track: "observability"
presenters: "Ajay Nagariya, Debajit Das, Kumar Pratyush"
stype: "英文演讲"
---
Apache Http Server的可观察性解决方案基于OpenTelemetry(源代码在https://github.com/open-telemetry/opentelemetry-cpp-contrib/tree/main/instrumentation/otel-webserver-module)。它支持通过在运行时将检测注入Apache Http server来跟踪对服务器的传入请求。它还能够捕获传入请求中涉及的许多模块(包括mod_proxy)的响应时间，从而包括每个模块的分层时间消耗。

监视各个模块对于Apache Http Server的检测至关重要。当HTTP请求流经各个模块时，请求中涉及的任何模块都可能发生执行延迟或错误。为了确定请求处理中任何延迟或错误的根本原因，模块相关信息(例如各个模块的响应时间)将增强Apache Http服务器的可调试性。

这个解决方案监控的模块有:mod_sso, mod_php, mod_dav, mod_proxy和mod_proxy_balancer。有一个不受监控的排除模块列表，因为这些模块负责Apache Http Server的内部工作，不直接参与应用程序请求处理。这个被排除的模块列表可以在https://github.com/open-telemetry/opentelemetry-cpp-contrib/blob/main/instrumentation/otel-webserver-module/src/apache/ExcludedModules.cpp上找到。除被排除的模块外，所有其他模块都被开箱监控。如果用户希望监视这些模块中的任何一个，可以很容易地将它们从排除列表中删除。

可观察性解决方案作为Apache Http Server的模块提供，应该在所有其他模块加载后加载，以便捕获模块级别的详细信息。由于此解决方案基于OpenTelemetry，因此它按照OpenTelemetry规范中指定的方式创建跨度和跟踪。遥测数据可以在任何后端进行查看和分析，如zipkin, Jaeger, Appdynamics等。

在Apache Http Server接收到的每个请求中，span在请求开始时创建，在请求结束时结束。除此之外，还创建了span，并在请求处理中涉及的各个模块的开始和结束处结束。然后，这些跨度被周期性地发送到配置的后端进行处理，并获得有价值的见解。

位于印度班加罗尔的思科(Appdynamics)团队正在积极管理可观察性解决方案。
 ### Speakers: 
 <img src="images/speaker/1150.png" width="200" /><br>Ajay Nagariya: 思科, AppDynamics(思科)工程总监, 他是一位有成就的技术专业人士和领导者，拥有21年以上的经验，并在建立和领导世界级的产品团队方面有良好的记录。我曾管理过产品组合，包括开发、测试、DevOps和工程支持，涵盖NMS、存储、系统编程、硬件验证、ERP、安全软件和Web/云产品等领域的全栈/企业产品。

具有敏锐的商业能力，具有战略思考和行动的能力。我有建立工程过程的可见的跟踪记录，从而提高产品质量，可预测的时间表，和产品交付。

通过招聘、培训和人才管理，我不断地建立起团队。我有很强的吸引和留住顶尖人才的能力。

在思科，我领导着一个现代化的APM团队，在SaaS和云本地平台的全栈可观察性领域。

主要负责为基于动态语言/框架的最新技术栈构建端到端的APM和Observability解决方案，兼容Open Telemetry分布式跟踪器，以及大数据技术的监控系统，如Kafka, Spark和Hadoop，这需要开发世界级的收集器，大数据管道，高可用存储和可视化仪表板。由此产生的产品为我们的客户提供了探索性、预测性和规范性的能力，以保持他们的生产系统的顶部。

核心竞争力
•工程领导
•掌握全栈软件开发
•升级和人员管理
•商业智慧
•投资组合规划和DevOps模型

 <img src="images/speaker/1150_2.png" width="200" /><br>Kumar Pratyush: 思科, AppDynamics(思科)高级软件工程师, 经验丰富的高级软件工程师，在APM，电信和消费电子行业工作过。熟练掌握多线程开发，软件设计模式，C和c++。在Silchar国家理工学院获得电子与通信工程学士学位(B.Tech)。

 <img src="images/speaker/1150_3.png" width="200" /><br>Debajit Das: 思科, AppDynamics软件工程师(思科), 在思科AppDynamics产品开发团队担任软件工程师。我是一个有竞争力的编程爱好者。

为自定义PHP应用程序创建OpenTelemetry Instrumentation，使用Laravel可以与Appdynamics Instrumentation进行比较
·在Appdynamics传感器的基础上，分析了Jaeger、Zipkin、Opencensus等各种仪表支持产生的跨度和轨迹。
·对支持OpenTelemetry框架的手动仪表进行更改，包括自动仪表支持。

 