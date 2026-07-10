---
title: "Agentic Debugging: Using LLMs to Auto-Diagnose Impala Query Profiles"
date: ""
track: "agenticcoding"
presenters: "Surya Hebbar"
stype: "English Session"
---

Large Language Models show incredible promise for code generation, but debugging distributed systems is a different beast. If you feed a raw 400MB database query profile to an LLM, it will either choke on the token limit or hallucinate wildly. To turn agents into dependable collaborators in production, we have to fix the data pipeline feeding them.

This session shares hands-on experience from Apache Impala on making "Agentic Debugging" a reality. We will explore how transitioning from verbose execution forests to Aggregated Runtime Profiles solves the LLM context problem. By dense-packing telemetry and safely structuring missing events into token-efficient JSON payloads, we empower AI agents to autonomously and accurately diagnose execution bottlenecks. Attendees will learn repeatable patterns for bridging the gap between massive system logs and strict LLM context windows.

### Speakers:


<img src="https://cdn.sessionize.com/image/6b92-400o400o1-sPSKNvSRCLEreK26PfKD7w.jpg" width="200" /><br/>

Surya Hebbar: Core Contributor to Apache Impala | MS Researcher at The University of Tokyo

Surya Hebbar is a High-Performance Computing Engineer and a Core Contributor to the Apache Impala project. Working as a Software Engineer at Cloudera, his work has focused heavily on Impala's C++ backend and distributed systems optimization. He architected the "Aggregated Runtime Profiles" initiative, which fundamentally re-engineered the profile structure from sparse instance-level counters into dense, memory-efficient arrays to eliminate bottlenecks in high-concurrency clusters. He also led the modernization of Impala's WebUI and observability tools to handle petabyte-scale query execution graphs without locking up the browser.

Surya is currently transitioning to pursue his MS in Earth and Planetary Science at The University of Tokyo. Working under Prof. Masaki Satoh, he will be leveraging exascale supercomputers like Fugaku and Miyabi to run high-resolution climate models, applying his expertise in parallel processing to the field of atmospheric fluid dynamics.

