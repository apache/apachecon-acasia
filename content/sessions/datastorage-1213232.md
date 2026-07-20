---
title: "Everything boil down to SQL: Shift DataFusion Optimizations to Another Non-Generic Computing System"
date: "2026-08-07T14:30:00"
track: "datastorage"
presenters: "Ruihang Xia"
stype: "Chinese Session"
room: "Mtn WanShou Hall"
---

On the way to re-implement PromQL (the query language behind Prometheus) on top of Apache DataFusion, we found many similar optimization patterns between these two totally different languages. Some share a similar idea, some can be mixed together, and some are fed back to DataFusion. We further confirmed that almost all different-looking computing systems, no matter what their user interface looks like, are composed of several generic primitives. In this session, we'll first discuss those primitives and their optimizations. Then talk about high-level philosophies of how to keep things simple and unified while making optimizations for different systems and purposes, with lots of famous systems as examples.

### Speakers:


<img src="https://cdn.sessionize.com/image/17ae-400o400o1-PGTz6fMBHyvwhcgyuLCThc.png" width="200" /><br/>

Ruihang Xia: Software Architect at Greptime Inc.

Software Architect at Greptime
Apache DataFusion PMC, Apache Arrow Committer, Apache HoraeDB PPMC
https://github.com/waynexia