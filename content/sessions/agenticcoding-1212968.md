---
title: "Core Design Gets Harder: Lessons from Rewriting Bub"
date: ""
track: "agenticcoding"
presenters: "卓燃 尚"
stype: "Chinese Session"
---

Agentic coding makes it easier than ever to generate features. But that is exactly why extensibility is not enough: we need systems that remain understandable, replaceable, and governable.

This talk uses the rewrite of Bub as a case study in a deliberately counterintuitive design choice. At a time when AI is increasingly good at producing demos and edge features, Bub’s core is still largely designed and handwritten by humans. Bub grew out of messy multi-person group chats rather than polished single-user demos, which exposed structural problems early: once channels, skills, and memory-related capabilities accumulated, continuing to absorb them into the framework core would make the system harder to understand, configure, and maintain.

I will share why the rewrite pushed more variation out of the framework core, kept the system small and hook-first, and treated built-ins as replaceable default plugins. I will also discuss Bub’s tape model as a way to make context more explicit, reconstructable, and reviewable for both humans and agents. The broader argument is practical: when feature generation gets cheaper, careful human design of core boundaries, dependency direction, extension points, and context becomes more important, not less.


### Speakers:


<img src="https://cdn.sessionize.com/image/6bf9-400o400o1-DQtQav4AMVTHbmyVtQMfBY.jpg" width="200" /><br/>

卓燃 尚: ASF Member, Senior Engineer @ OceanBase

Data Systems · AI Infrastructure · OSS

