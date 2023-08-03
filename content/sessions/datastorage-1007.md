---
title: "How increasing partition size in Apache Cassandra can reduce disk usage by over 30%"
date: "2023-08-19T16:45:00" 
track: "datastorage"
presenters: "John Del Castillo"
stype: "English Session"
---
Did you know that over-partitioning in Apache Cassandra can lead to excessive storage requirements? 

In this presentation, we explore how, at Instaclustr, were able to reduce the storage footprint of our metrics data by over 30%, from 244tb to 157tb, and improve general performance of our cluster - simply by making a small change to the schema of the tables we were using. 

Instaclustr manages a fleet of over 10 000 customer servers as part of our managed service offering and part of that system includes real time metrics collection from the operating system and running applications which are stored in a 70 node Apache Cassandra cluster. 

We will go into detail explaining what problems the existing schema was designed to solve, how our Cassandra experts determined what we needed to change, and why the change was able to drastically improve our storage efficiency without major changes to our downstream systems.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230606/1034424690.jpg" width="200" /><br>John Del Castillo: NetApp, Technology Evangelist, I’m a software engineer with over 15 years of experience developing enterprise software solutions across a variety of languages and technologies. 

For 6 years I worked at Instaclustr as a Lead Engineer and for the last year I've taken the mantle of Technology Evangelist, specializing in open-source technology. 

In this role I explore the landscape of open-source technologies, explore new solutions, document interesting use cases and create written and video content to help educate and encourage people to use open source for their business. 
 <br><br>