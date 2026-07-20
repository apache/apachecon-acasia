---
title: "一次构建，任意 Linux 运行：面向 Apache Cloudberry（孵化中）的 SynxDB CE"
date: "2026-08-09T15:45:00"
track: "incubator"
presenters: "Shine Zhang, Ed Espino"
stype: "英文演讲"
room: "玉泉山会议室"
---

Apache Cloudberry（孵化中）是一个兼容 Postgres 的 MPP 分析型数据库，社区增长迅速。与许多 Apache 项目一样，它的官方发布物是源码 tarball——这完全符合 ASF 的治理要求，却给真正想运行它的人留下了一段空白。爱好者、评估者以及企业团队，都期望能有一个可直接安装的二进制包。

最显而易见的做法——"每个发行版各打一个包"——其实是个陷阱。glibc 符号版本、编译器 ABI、内置库版本（OpenSSL、Perl、Python），再加上 RPM 与 DEB 打包方式的差异，会让构建矩阵不断膨胀，直到你为同一个版本维护十几种变体。

对于 SynxDB CE——我们的 Apache Cloudberry（孵化中）社区版——我们走了一条不同的路：一次构建，在任何 glibc 版本足够新的 Linux 上运行。策略如下：

打包整套工具链。一个分层的 Docker 构建环境（toolchain → devel-base → devel-cbdb → runtime）搭载了我们自带的 GCC 12.2.1、binutils、Perl、Python、cmake、Conan、meson 和 ninja——全部从源码构建进 /usr/local/toolchain/。宿主 OS 对编译过程不贡献任何东西。每一次构建，无论在哪个开发者的笔记本上、哪一台 CI runner 上，用的都是同一套二进制。

以 glibc 2.17 作为 ABI 下限，并使用 CentOS 7 作为构建平台。glibc 向后兼容的承诺意味着：链接于 2.17 的二进制，可以原封不动地运行在 Rocky 8（glibc 2.28）、Rocky 9（2.34）、Ubuntu 22.04（2.35）、Ubuntu 24.04（2.39），以及年代相近的 SUSE 发行版上。

让 glibc 成为唯一的运行时依赖。其余一切——OpenSSL、libhdfs3、ORC、Parquet、libgsasl、libftp、liboss2——都通过 Conan 2.x 的依赖 DAG 内嵌进来并链接进发行包。没有对包管理器的外部依赖。再也不需要"先装这 40 个 RPM"。

从同一棵二进制树打包出 RPM 和 DEB。一次构建，两份产物。无需并行流水线。

把可移植性校验作为一道 CI 关卡。ldd 扫描确认没有意外的共享库依赖边；冒烟测试在 Ubuntu 24.04 上安装 DEB 并运行 SELECT version()。

我们将走查这套 Dockerfile 层级结构，展示 Conan 包的 DAG，并坦诚地聊聊一路上没走通的方案——编译器 ABI 的坑、glibc 符号的意外，以及 fpm 悄悄带来的代价。

### 讲师:


<img src="https://cdn.sessionize.com/image/400a-400o400o1-Kbirppzd7dTL7TeFZfHuCi.jpg" width="200" /><br/>

Shine Zhang：Synx Data Labs 联合创始人兼 CTO

Xin Zhang（Shine）——Synx Data Labs 联合创始人兼 CTO。前 Pivotal/VMware Greenplum 工程师、PostgreSQL 贡献者，长期参与 Greenplum / Cloudberry 这一技术脉络。负责 Synx 对 Apache Cloudberry（孵化中）的上游贡献，以及 SynxDB 社区版的发布流水线。


<img src="https://cdn.sessionize.com/image/f030-400o400o1-sEY99WaWKxwojYGUBVLoqZ.jpg" width="200" /><br/>

Ed Espino：Synx Data Labs, Inc. 联合创始人兼 CEO

Ed Espino 是 Synx Data Labs 的联合创始人、SynxDB 的缔造者，在数据库工程与分析基础设施领域拥有 30 余年经验。他的职业经历涵盖在 Informix 与 Sybase 的奠基性工作、2009 年加入 Greenplum，并参与了 OnDisplay 和 Pivotal 的成功上市。

作为 Apache 软件基金会成员、Apache Cloudberry（孵化中）的 PPMC 成员，Ed 是开源分析生态的活跃贡献者。他目前在 Synx Data Labs 领导基础设施建设，包括 cloudberry-image-factory 与 assembly-bom 项目，并正在打造 The Analytics Workshop——一个以"基础设施优先"视角探讨分析工程的 Substack 出版物。

Ed 带来的是实干家的视角，这种视角来自他数十年来身处数据库架构、开源社区治理与企业数据平台交汇处的经历。