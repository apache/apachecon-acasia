---
title: "Observability Solution for Apache Http Server"
date: "2022-07-29T16:00:00"
track: "observability"
presenters: "Nagariya, Ajay,Das, Debajit,Pratyush, Kumar"
stype: "English Session"
---
The observability solution of Apache Http Server is based on OpenTelemetry (source code at https://github.com/open-telemetry/opentelemetry-cpp-contrib/tree/main/instrumentation/otel-webserver-module). It enables tracing of incoming requests to the server by injecting instrumentation into the Apache Http Server at runtime. It also has capabilities to capture the response time of many modules (including mod_proxy) involved in an incoming request, thereby including the hierarchical time consumption by each module.

Monitoring individual modules is crucial to the instrumentation of Apache Http Server. As the HTTP request flows through individual modules, delay in execution or errors might occur at any of the modules involved in the request. To identify the root cause of any delay or errors in request processing, module wise information (such as response time of individual modules) would enhance the debuggability of the Apache Http Server.

Some of the modules monitored by this solution are: mod_sso, mod_php, mod_dav, mod_proxy and mod_proxy_balancer. There is a list of excluded modules that are not monitored because these modules are responsible for internal working of Apache Http Server and are not directly involved in application request processing. This list of excluded modules can be found at https://github.com/open-telemetry/opentelemetry-cpp-contrib/blob/main/instrumentation/otel-webserver-module/src/apache/ExcludedModules.cpp. All other modules other than the excluded modules are monitored out of the box. In case the user wants to monitor any of these modules, one can easily remove them from the excluded list.

The observability solution is provided as a Module of Apache Http Server and should be loaded after all other modules are loaded, so that the module level details are captured. Since this solution is based on OpenTelemetry, it creates spans and traces as specified in the OpenTelemetry Specifications. The telemetry data can be viewed and analyzed in any backend such as zipkin, Jaeger, Appdynamics etc.

On every request received by Apache Http Server, Spans are created at the start of the request and ended at the end of the request. Apart from this, spans are also created and ended at the start and end of individual modules involved in request processing. The spans are then emitted periodically to the configured backend for processing and to derive valuable insights.

The observability solution is being actively managed by a team in Cisco(Appdynamics) based out of Bangalore, India.
 ### Speakers: 
 <img src="images/speaker/1150.png" width="200" /><br>Nagariya, Ajay: Cisco, Director Of Engineering at AppDynamics (Cisco), An accomplished Technology Professional & Leader with 21+ years of demonstrated experience and a proven track-record in building and leading world-class product teams. I have managed product portfolios across Development, Testing, DevOps & Engineering Support for the Full Stack/Enterprise Products in the areas of NMS, Storage, Systems Programing, Hardware Validations, ERP, Security Software & Web/Cloud offerings. 

A business enabler with proven business acumen competency, ability to think and act strategically. I have visible track-record of establishing engineering processes that result in improved product quality, predictable schedules, and product delivery. 

I have repeatedly built teams from the ground up through recruitment, training, and talent management. I have strong ability to attract and retain top talent.

At Cisco, I am leading a modern APM team in the domain of a Full Stack Observability to SaaS and Cloud-Native platforms.

Primarily responsible for building end to end APM and Observability solutions for latest technology stack based dynamic languages/frameworks, Open Telemetry compliant distributed tracers, and monitoring systems for big data technologies like Kafka, Spark and Hadoop, that entail developing world class collectors, big data pipelines, highly available storage, and visualization dashboards. The resulting products provide exploratory, predictive and prescriptive capabilities to our customers to stay on top of their production systems.

CORE COMPETENCIES
• Engineering Leadership 
• Hands-on Full Stack Software development 
• Escalation & People Management 
• Business Acumen
• Portfolio planning & DevOps Model

 <img src="images/speaker/1150_2.png" width="200" /><br>Das, Debajit: Cisco, Senior Software Engineer at AppDynamics (Cisco), Experienced Senior Software Engineer with a demonstrated history of working in the APM, telecommunications and consumer electronics industry. Skilled in Multithreaded Development, Software Design Patterns, C and C++. Strong engineering professional with a Bachelor of Technology (B.Tech.) focused in Electronics and Communication engineering from National Institute of Technology, Silchar.

 <img src="images/speaker/1150_3.png" width="200" /><br>Pratyush, Kumar: Cisco, Software Engineer at AppDynamics(Cisco), Working as a software engineer at Cisco AppDynamics product development team. I am Competitive programming enthusiast.

Creating OpenTelemetry Instrumentation for custom PHP application made using Laravel which made it possible to make a comparison with Appdynamics Instrumentation
· Analyzed the spans and traces generated by various instrumentation supports like Jaeger, Zipkin ,Opencensus etc on top of Appdynamics sensor.
· Made changes to manual instrumentation supported OpenTelemetry framework to include Auto instrumentation support.

 