---
title: "Build Once, Run on Any Linux: SynxDB CE for Apache Cloudberry (Incubating)"
date: "2026-08-09T15:45:00"
track: "incubator"
presenters: "Shine Zhang, Ed Espino"
stype: "English Session"
room: "Mtn YuQuan Hall"
---

Apache Cloudberry (Incubating) is a Postgres-compatible MPP analytical database with a fast-growing community. Like many Apache projects, its official releases are source tarballs — exactly right for ASF governance, but leaving a gap for the people who actually want to run it. Hobbyists, evaluators, and enterprise teams all expect an installable binary.

The obvious approach — "just build one package per distro" — is a trap. glibc symbol versions, compiler ABIs, bundled library versions (OpenSSL, Perl, Python), and RPM-vs-DEB packaging all multiply the matrix until you're maintaining a dozen variants of the same release.

For SynxDB CE, our Community Edition of Apache Cloudberry (Incubating), we took a different path: build once, run on any Linux where glibc is recent enough. The strategy:

Bundle the entire toolchain. A layered Docker build environment (toolchain → devel-base → devel-cbdb → runtime) ships our own GCC 12.2.1, binutils, Perl, Python, cmake, Conan, meson, and ninja — all built from source into /usr/local/toolchain/. The host OS contributes nothing to the compile. Every build, on every developer's laptop and every CI runner, uses the same bits.

Target glibc 2.17 as the ABI floor, using CentOS 7 as the build platform. glibc's backward-compatibility guarantee means a binary linked against 2.17 runs unchanged on Rocky 8 (glibc 2.28), Rocky 9 (2.34), Ubuntu 22.04 (2.35), Ubuntu 24.04 (2.39), and SUSE releases of similar vintage.

Make glibc the only runtime dependency. Everything else — OpenSSL, libhdfs3, ORC, Parquet, libgsasl, libftp, liboss2 — is vendored through a Conan 2.x dependency DAG and linked into the distribution. No external package-manager dependencies. No "install these 40 RPMs first."
Package from one binary tree into both RPM and DEB. Single build, two artifacts. No parallel pipelines.

Verify portability as a CI gate. ldd scans confirm no unexpected shared-library edges; smoke tests install the DEB on Ubuntu 24.04 and run SELECT version().

We'll walk through the Dockerfile hierarchy, show the Conan package DAG, and talk candidly about what didn't work on the way here — compiler ABI pitfalls, glibc symbol surprises, and the quiet cost of fpm.

### Speakers:


<img src="https://cdn.sessionize.com/image/400a-400o400o1-Kbirppzd7dTL7TeFZfHuCi.jpg" width="200" /><br/>

Shine Zhang: CTO and co-founder of Synx Data Labs

Xin Zhang (Shine) — CTO and co-founder of Synx Data Labs. Former Pivotal/VMware Greenplum engineer, PostgreSQL contributor, and long-time participant in the Greenplum / Cloudberry lineage. Leads Synx's upstream contributions to Apache Cloudberry (Incubating) and the SynxDB Community Edition release pipeline.


<img src="https://cdn.sessionize.com/image/f030-400o400o1-sEY99WaWKxwojYGUBVLoqZ.jpg" width="200" /><br/>

Ed Espino: CEO and co-founder of Synx Data Labs, Inc.

Ed Espino is co-founder of Synx Data Labs and creator of SynxDB, with over 30 years of experience in database engineering and analytics infrastructure. His career spans foundational work at Informix and Sybase, joining Greenplum in 2009, and contributing to successful IPOs at OnDisplay and Pivotal.
A member of the Apache Software Foundation and PPMC member for Apache Cloudberry (Incubating), Ed is an active contributor to the open-source analytics ecosystem. He currently leads infrastructure development at Synx Data Labs, including the cloudberry-image-factory and assembly-bom projects, and is building The Analytics Workshop — a Substack publication focused on analytics engineering through an infrastructure-first lens.
Ed brings a practitioner’s perspective shaped by decades at the intersection of database architecture, open-source community governance, and enterprise data platforms.