---
title: "State of Scala API in Apache Flink"
date: "2023-08-19T15:45:00" 
track: "streaming"
presenters: "alexey"
stype: "English Session"
---
As a Scala developer writing new Flink job, you expect to use latest Scala 3 version, rather the one Flink was compiled with. Support of Scala 2.13 and Scala 3 was not really possible until Flink 1.15 came out. In this talk we will review how the Scala API was done in Apache Flink prior the version 1.15 and what has changed in that release. Apache Flink chose quite opposite way to enable Scala developers to use any Scala version than Apache Spark project and that is interesting discussion on its own.

During this talk we will go through the SBT example project to build Flink jobs with Scala 3. We will look at the current community options of Scala wrappers for Flink Java API and challenges related to that. In the result, we will see that using Scala in Flink jobs is much more convenient than writing your streaming jobs with Java API. An introduction of the Scala CLI makes the whole packaging experience of Scala Jobs a pure joy.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230607/1640066470.jpg" width="200" /><br>alexey: Ververica, Solution Architect, I am a Solution Architect working for last the last 6 years on data solutions and products. At Ververica I am focusing on supporting clients to solve their challenges in adopting data stream processing with Apache Flink. Among my previous project and companies I developed different systems such as Data Lakes, Data Integration and Data Virtualization Layers. I have also spent many years on developing data services for investment banks including currency trading software. In my spare time, I also contribute to various open-source projects or start my own for fun. My hobbies are astronomy, playing music and gym.

 <br><br>