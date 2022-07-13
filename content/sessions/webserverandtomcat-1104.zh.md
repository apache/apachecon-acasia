---
title: "基于 dubbo-go-pixiu 的 dubbo mesh"
date: "2022-07-31T14:40:00"
track: "webserverandtomcat"
presenters: "麻志辉"
stype: "中文演讲"
---
主要分享 Dubbo-go在mesh 领域中 proxyless service-mesh 方向的探索。
类似与sidecar模式，proxyless通过在dubbo-go框架内置xDS协议的支持，直接与Istiod控制面组件交互，实现在istio mesh环境下，服务注册发现、流量治理等方面功能。proxyless mesh方案在考虑大规模服务网格中的资源效率、时间敏感应用代理层时延影响等一些场景中，具有明显的优越性。
在外部流量接入方面，Dubbo-go-pixiu 做为dubbo gateway实现http to dubbo的协议转换，接入istio 后可做为Ingress gateway，实现从外部访问mesh环境中dubbo服务的能力。
 ### Speakers: 
 <img src="images/speaker/1104.png" width="200" /><br>麻志辉: dubbo-go-pixiu社区, dubbo-go-pixiu committer, 讲师是dubbo-go-pixiu社区重要的贡献者，目前负责对接istio的任务。

 