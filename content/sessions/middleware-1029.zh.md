---
title: "为Java项目创建跨平台、可复制的二进制构建"
date: "2022-07-30T17:30:00"
track: "middleware"
presenters: "Mark Thomas"
stype: "英文演讲"
---
随着对供应链安全的关注越来越多，对可复制的二进制构建的需求也越来越大。这为开放源码项目提供了机会，因为与封闭源码项目不同，可复制的二进制构建使开放源码项目能够明确地证明，它们所提供的方便的二进制文件是由终端用户能够审计的标记过的、未修改的源树构建的。

在过去的一年中，Apache Tomcat项目一直致力于跨平台可复制的二进制构建。Tomcat现在所处的位置是，根据给定的项目标签，可以在Windows或Linux上生成相同的发布发行版，包括源文件、二进制文件和为Windows签名的authenticode安装程序。本节将讨论Apache Tomcat项目在转向可复制构建时所面临的挑战，用于调试构建之间差异的技术以及用于解决这些差异的不同解决方案。
 ### Speakers: 
 <img src="images/speaker/1029.png" width="200" /><br>Mark Thomas: VMware, 主管工程师, Mark自2003年11月以来一直是Apache Tomcat提交者。他最初是在空闲时间研究Tomcat，但从2008年8月开始，他被SpringSource(现在是VMware的一部分)雇用，从事Apache Tomcat的工作。他的大部分时间都花在Tomcat上，但他也在tc Server上工作，这是VMware基于Apache Tomcat的Servlet & JSP容器。

Mark是Apache Tomcat 10.0和10.1的发布经理，他试图每个月左右发布一个新版本。他目前专注于Tomcat 10.1的开发，该开发将支持Jakarta EE 10。他是Eclipse Servlet、服务器页面、表达式语言和WebSocket的提交者。

在ASF的其他地方，Mark是ASF安全和基础设施团队的一员，他还在Commons PMC工作，专注于Commons Pool和DBCP。

Mark是ASF的会员，并于2016年至2019年担任董事。他自2018年2月起担任品牌管理副总裁。

 