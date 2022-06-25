---
title: "Dubbo Mesh based on Dubbo-Go-Pixiu"
date: "" 
track: "webserverandtomcat"
presenters: "麻志辉"
stype: "Chinese Session"
---
This article mainly shares the exploration of Proxyless Service-mesh direction in the mesh field of Dubbo-Go.
Similar to sidecar mode, proxyLess directly interacts with Istiod control plane components through built-in xDS protocol support in Dubbo-Go framework, realizing functions such as service registration discovery and traffic management in Istio mesh environment. Proxyless Mesh scheme has obvious advantages in some scenarios such as resource efficiency and time-sensitive application agent layer delay effect in large-scale service grid.
In terms of external traffic access, Dubbo-Go-Pixiu serves as the Dubbo gateway to implement HTTP to Dubbo protocol conversion, and after connecting to Istioccess, it can serve as the Ingress gateway to realize the ability to access Dubbo services in the mesh environment from the outside.
 ### Speakers: 
 <img src="images/speaker/1104.png" width="200" /><br>Zhihui Ma: Dubbo - go - pixiu community, dubbo-go-pixiu committer, The lecturer is an important contributor to the Dubbo-Go-Pixiu community and is currently responsible for the task of connecting with ISTIO.

 