---
title: "Embrace cloud native, based on Kubernetes ShardingSphere cloud transformation"
date: "" 
track: "middleware"
presenters: "李卓"
stype: "Chinese Session"
---
background
As Kubernetes matured and became more stable, SphereEx came to see it as an important milestone in the next phase of ShardingSphere as it explored its future prospects. In this context, the SphereEx Cloud team focuses on the cloud transformation of ShardingSphere as an important goal. In the actual process, the team encountered many problems and challenges. This speech will share the problems and solutions of the team in the cloud transformation of ShardingSphere.
What is the Kubernetes Operator mode
Kubernetes' Operator mode concept allows you to extend the capabilities of a cluster by associating a controller with one or more custom resources without modifying Kubernetes' own code.
Operator is a client of the Kubernetes API and acts as a controller for user-defined resources.
What is Kubernetes CRD
Custom Resources are extensions to the Kubernetes API. Users can extend Kubernetes using resource customization.
In Kubernetes, the following capabilities can be satisfied:
1. You can directly update resources using the client or CLI.
2. This resource can also be supported directly using the Kubectl command.
3. Using the automation mechanism of Kubernetes, the change of this resource can be sensed and the subsequent operation of the associated object of this object can be carried out.
4. Automatic processing using Kubernetes native capabilities.
Problems encountered
During the process of cloud on ShardingSphere-Proxy, the team encountered several problems. One is that there is no standard deployment process in the cloud environment. At the present stage, Shardingsphere-Proxy only supports Docker and binary deployment mode. Another is that Shardingsphere-Proxy relies on Zookeeper as the governance node. Stateful services such as Zookeeper are not well suited for processing in the cloud. Kubernetes is better suited for stateless applications due to its Pod lifecycle characteristics and powerful horizontal scaling capabilities. With the addition of Zookeeper, ShardingSphere-Proxy becomes less stateless. This is a tough nut to crack for the cloud team.
The solution
At this stage, ShardingSphere has never stopped exploring the Kubernetes environment. The SphereEx Cloud team combined the Kubernetes Operator model with ShardingSphere to cloud-transform ShardingSphere-Proxy in order to enhance its ability to adapt and operate in the Kuerbenets environment. Combined with the native capability of Kubernetes, ShardingSphere-Proxy can be separated from Zookeeper in Kuebrnetes environment, and keep the cluster mode to run separately.
Take ShardingSphere-Proxy, a database governance middleware, for example
By combining the Kubernetes Operator mode, shardingSphere-Proxy can enhance its performance in Kubernetes. This includes automatic o&M, automatic capacity expansion, and automatic node status monitoring. In terms of deployment structure and deployment difficulty, the Operator also makes this easier. Although at the present stage, ShardingSphere-Proxy has officially supported Helm for deployment. However, Helm can only implement rapid deployment and versioning management of a ShardingSphere-Proxy cluster environment, and the subsequent automatic operation and maintenance, including cluster status check and self-healing, are missing. The existence of ShardingSphere-operator fills this gap. By using declarative resource description, ShardingSphere-Operator can help users achieve the desired final state of ShardingSphere-Proxy deployment mode simply and quickly. Increased the stability and maintainability of ShardingSphere-Proxy cluster in the cloud environment.
In addition, the existence of custom resources, a Kubernetes extension, can also help ShardingSphere-Proxy store metadata dependent on the runtime cluster. Relying on the list/ Watch capability of CRD in Kubernetes, it can broadcast the changes of metadata to nodes in other clusters and update the runtime metadata of other nodes in real time.
DistSQL (Distributed SQL) is an operating language unique to Apache ShardingSphere. It is used exactly the same way as standard SQL and is used to provide SQL-level operational capabilities for incremental functionality. During the Zookeeper process, as the entry point for metadata changes became more diverse, support was provided for how to write DistSQL to the configuration and for users to directly modify the CRD, and the team provided its own ideas. Shardingsphere-proxy can support the two metadata change entries simultaneously by combining ShardingSphered with Shardingspherecar. Shardingsphere-sidecar may also support xDS protocol of Service Mesh in the future. This greatly increases the expansion capability of ShardingSphere-Proxy in the cloud environment.
 ### Speakers: 
 <img src="images/speaker/1089.png" width="200" /><br>Eunice li: SphereEx, Cloud R&D Engineer, SphereEx Cloud R&d, Cloud R&D Engineer, ShardingSphere-Operator core developer, Apache ShardingSphere Contributor
 