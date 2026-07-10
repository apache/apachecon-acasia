---
title: "Fixing Authorization in Microservices Without Breaking Everything"
date: ""
track: "microservice"
presenters: "Aram Andreasyan"
stype: "English Session"
---

Authorization is one of those things that starts simple and quietly becomes a mess as systems grow. In a microservices setup, it often ends up duplicated across services, implemented slightly differently each time, and hard to reason about when something goes wrong.

In this talk, Aram will walk through what typically happens as teams scale from a single service to many and how access control logic starts to drift across the system. We’ll look at common patterns that seem fine at first but break down over time, especially when services need to share context or enforce consistent rules.

From there, he'll go over a more practical approach to handling authorization as a separate concern instead of embedding it everywhere. This includes how to structure policies, how services interact with an external decision layer, and what changes in terms of development and debugging.

The focus is on real implementation patterns and trade-offs, not theory. By the end, the audience should have a clearer way to think about authorization in distributed systems and how to avoid the usual pitfalls without rewriting everything from scratch.

### Speakers:


<img src="https://cdn.sessionize.com/image/cd9a-400o400o1-sgGoPSzQYUTb5WVgD7YNNt.jpg" width="200" /><br/>

Aram Andreasyan: Director of Solutions

Aram specializes in helping organizations simplify and scale authorization through policy-as-code approaches. With a strong background in cybersecurity, infrastructure, and access control, he works closely with engineering and security teams to design efficient, compliant, and developer-friendly authorization systems.
Prior to Cerbos, Aram consulted for technology startups and enterprise clients across EMEA and North America, focusing on digital transformation and cloud security strategies. Aram has experience working with distributed architectures, MDM (Master Data Management), and complex SaaS deployments. He's passionate about externalized authorization, IAM modernization, and helping economic buyers (CISOs, security architects, and engineering leaders) align technical decisions with regulatory and business needs.
When Aram's not solving authorization challenges, he enjoys staying close to tech communities, mentoring startups, and occasionally moonlight as a cyberpunk lore nerd.

