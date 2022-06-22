---
title: "Apache Ozone behind Simulation and AI industries"
date: "" 
track: "bigdata"
presenters: "Kota Uenishi"
stype: "English Session"
---
This talk introduces two types of workloads over Apache Ozone, in self-hosted supercomputer systems of Preferred Networks. They're the result of our effort connecting the AI & HPC ecosystem (PyTorch, GPU) to BigData ecosystem (JVM, commodity hardware).
One is distributed training of deep learning models. It is essentially a repeated random-read workload of about a few million images for a single round of training. Because of the random-read nature of the workload, prefetching the data cannot hide the latency enough to optimize the throughput. We introduce how we mitigated the issue by introducing a client-side cache system.
Another is dataset generation from scientific simulations (first-principles calculation), and image rendering from 3D models. The amount of data grows constantly proportional to the amount of computational resources (e.g. GPUs). We introduce a new form of the small files problem in Apache Ozone - the overhead of a metadata of a single object cannot be zero. We also discuss how we aggregate multiple (hundreds to million) files as a dataset file, under the constraints in the current situation of the client-side; such as libraries like boto, zip, and an ideal archive format.
 ### Speakers: 
 <img src="images/speaker/1151.png" width="200" /><br>Kota Uenishi: Preferred Networks, Inc., Engineer, Kota Uenishi is a software engineer from Preferred Networks, and has recently contributed a few patches to Apache Ozone. His team runs Apache Ozone to boost the potential of supercomputers owned by Preferred Networks. He used to work for Chainer project, one of the historical deep learning framework that supports massively distributed training and familiar with large scale deep learning workloads.
 