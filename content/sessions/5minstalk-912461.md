---
title: "Reimagining Software Testing with AI: A Reusable and Scalable Design"
date: "2025-07-27T11:20:00"
track: "5minstalk"
presenters: "Yunbo Ni"
stype: "Chinese Session"
---

With the growing demand for AI-driven software testing (AI4Testing), there is a pressing need for general and efficient frameworks that can leverage large language models (LLMs) to enhance software quality. However, existing LLM-based testing approaches often suffer from two key limitations: the generated test programs are overly simplistic, and exhaustive interaction with LLMs can be computationally expensive.

We propose a general framework that decouples the testing process into two distinct phases: an offline phase and an online phase. In the offline phase, we leverage LLMs to generate a diverse collection of small, feature-rich code pieces. In the online phase, these code pieces are strategically reused and composed to form complex test programs. This design significantly improves both the efficiency and expressiveness of AI-assisted testing.

We instantiate this idea in a tool named LegoFuzz, applied to the domain of C compiler testing. The results are striking: we discovered 66 bugs in GCC and LLVM, nearly half of which are miscompilation bugs—serious and hard-to-detect issues that existing LLM-based tools failed to uncover.

Our framework demonstrates the potential of modular, reuse-based design in AI4Testing and highlights new opportunities beyond compiler testing. Its flexible architecture makes it well-suited for adaptation to various software systems and practical integration into industrial continuous integration (CI) pipelines.

### Speakers:


<img src="https://sessionize.com/image/de01-400o400o2-E7ebZmPfsiUEsffiUdgK9B.png" width="200" /><br/>

Yunbo Ni: Incoming PhD student at CUHK, focusing on research in testing.

I am an undergraduate student of Software Engineering in Nanjing University. I am supervised by Prof. Yang Feng at SSCT-Lab. My research interests lie in the Programming Language and Software Engineering. 

I’ll be joining Chinese University of Hong Kong (CUHK) as a Ph.D. student in 2025 Fall, under the supervision of Prof. Shaohua Li.

