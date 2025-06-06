---
title: "The Exploration and Practice of State Storage in Tencent Big Data Flink with Separation of Computati"
date: ""
track: "datastorage"
presenters: "YanPeng shi"
stype: "Chinese Session"
--- 

1.Background:
Flink, as a stateful stream processing system, has a state storage engine that plays a crucial role. In Flink, state is used to store intermediate results during the data stream computation process. Flink provides state read and write services for operators through the State Backend component. However, under the current architecture where computation and storage are integrated, the following issues arise:
a. Local disk limitations: The state data in RocksDB is heavily dependent on local disks, and when the local disk space is full, jobs cannot run properly.
b. Slow checkpoint generation: The large size of checkpoint state data leads to prolonged upload times. Additionally, periodic checkpoints can cause traffic spikes and CPU spikes, affecting the processing speed and throughput of the business logic itself.
c. Slow checkpoint recovery: The native recovery process requires downloading the entire checkpoint state file, which is slow in scenarios with large states.

2.Functional Architecture:
a. Fuse supports remote read and write: Based on the Fuse mechanism, remote storage is mounted to a local directory, allowing state to be directly stored in remote distributed storage using RocksDB's POSIX semantics.
b. Fast checkpoint with file sharing: In the separation of computation and storage architecture, state file data is incrementally and asynchronously persisted in remote storage during job execution. When taking a job checkpoint snapshot, only a small amount of data in the Memtable needs to be flushed to remote storage, along with the corresponding metadata.
c. Lazy loading for fast recovery: In the separation of computation and storage architecture, the state backend supports remote access to state data. During state recovery, users only need to download a small amount of metadata before the job can start processing data. Subsequently, state files will be asynchronously loaded into local disk cache based on caching strategies, enabling quick recovery of large state jobs through lazy loading.

3. Performance Optimization:
a. Read/write cache and metadata cache: Utilizing local disks as a cache, combined with RocksDB's own Block Cache/Memtable memory cache, forms a hot-warm-cold data hierarchy. Frequently accessed warm data is stored in memory and local cache, while infrequently accessed cold data is kept in remote storage, reducing state access latency.
b. Local cache affinity recovery scheduling: Based on TaskManager state cache files, remote state reads are minimized. During recovery scheduling, jobs are rescheduled to their previous locations whenever possible, providing better performance for the jobs.

4. Effectiveness and Benefits:
Job processing performance comparison: Through read/write caching, job performance reaches 80% of that in RocksDB Local mode.
Timeliness: The downtime during job recovery is reduced by 60%.

5. Future Plans:
Intelligent caching strategy: A more intelligent and fine-grained caching mechanism.
Asynchronous batch access to community state: Further reducing the impact of remote state access through asynchronous mechanisms.
Hot updates for underlying Fuse components: Updates to the underlying Fuse components will not affect upper-layer applications.

### Speakers:

<img src="https://sessionize.com/image/8ab3-400o400o1-J6rdbW4HhzZRzSqmcX56bS.jpg" width="200" /><br/>

Tencent Senior Engineer, graduated with a Master's degree from Beijing University of Posts and Telecommunications in 2021, focusing on Flink core development.