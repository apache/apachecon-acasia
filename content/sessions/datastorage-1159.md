---
title: "Smooth Migration Practice from MapReduce to Spark at ByteDance"
date: "2023-08-19T14:00:00" 
track: "datastorage"
presenters: "Wei Zhongjia"
stype: "Chinese Session"
---
As the business grows, ByteDance runs approximately 1.2 million Spark jobs online every day, while there are still about 20,000 to 30,000 MapReduce tasks running online every day. As a long-standing batch processing framework, from the perspective of big data development, MapReduce engine operation and maintenance faces a series of problems, such as low ROI for framework updates and poor adaptability to new computing scheduling frameworks. From the user's perspective, there are also a series of issues with using the MapReduce engine, such as poor computing performance, requiring additional Pipeline tools to manage serially executed jobs, and wanting to migrate to Spark but having many legacy jobs that use various scripts not supported by Spark itself. In this context, ByteDance's Batch team designed and implemented a smooth migration solution for MapReduce tasks to Spark. This solution allows users to smoothly migrate from MapReduce to Spark by adding only a few parameters or environment variables to legacy jobs, greatly reducing migration costs and achieving good cost benefits.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230609/1631399580.png" width="200" /><br>Wei Zhongjia is a basic infrastructure engineer at ByteDance. He joined ByteDance in 2018 and currently works as a big data development engineer in the basic infrastructure team, focusing on the field of big data distributed computing. He is mainly responsible for Spark kernel development and ByteDance's self-developed Shuffle Service development.
 <br><br>