- [Slurm](#slurm)
  - [Resources](#resources)
    - [UAB's cheaha](#uabs-cheaha)
    - [Slurm cheat/reference sheet](#slurm-cheatreference-sheet)
  - [FAQ](#faq)
    - [Considerations in best choosing resources for jobs](#considerations-in-best-choosing-resources-for-jobs)
    - [Use of `mem` vs `mem-per-cpu`](#use-of-mem-vs-mem-per-cpu)
    - [How busy is cheaha?](#how-busy-is-cheaha)

# Slurm

## Resources

### UAB's cheaha

* [Getting Started guide](https://docs.uabgrid.uab.edu/wiki/Cheaha_GettingStarted)
* Research Computing's training sessions
  * [Job submission and scheduling](https://www.youtube.com/watch?v=G1yBVlPiBfY)
  * [Singularity containers](https://gitlab.rc.uab.edu/rc-training-sessions/singularity_containers/-/tree/master)

### Slurm cheat/reference sheet

* https://support.nesi.org.nz/hc/en-gb/articles/360000691716-SLURM-Reference-Sheet
* https://docs.rc.fas.harvard.edu/kb/convenient-slurm-commands/
* And [Mana's](https://github.com/ManavalanG/random_notes/blob/master/notes/slurm.md) (yup, that's a shameless plug)


## FAQ

### Considerations in best choosing resources for jobs

* Don't request more resources (CPUs, memory, GPUs) than you will need. In addition to using your core hours faster,
  resources intensive jobs will take longer to queue. Use the information provided at the completion of your job (eg:
  via the sacct command) to better define resource requirements.
  [Source](https://support.nesi.org.nz/hc/en-gb/articles/360000705196)
* Smaller partitions will get higher priority.
  * So in cheaha, `express`(max 2 hrs) > `short`(max 12 hrs) > `medium`(max 50 hrs) > `long`(max 150 hrs).
  * If your job can finish in 1 hr, you better use `express` partition and not `medium`.
* Use `--cpus-per-task` for multi-threaded jobs.
  * *Example case study:* Time taken to finish a job is proportional to no. of CPUs alloted, and it will take 4 hrs with
    1 CPU and 0.2 hr with 20 CPU. You have to run this job in parallel for 100 samples. Which would you choose -- 1, 4 or
    20 CPUs?
    * 1 or 4 CPU is a better choice. Demanding 20 CPUs means that slurm's job scheduler has to wait until the node becomes
      available with as many CPUs for each job. While 20 CPUs will get the job done faster, if slurm is busy, chances
      are they will spend more time in the job queue before they are actually run. So using fewer CPUs have upper hand here,
      in general.
    * 1 or 4 CPUs? This is more difficult to answer, as the differences here are likely not as pronounced as 1 vs 20
      CPUs. In the example scenario, use of 1 CPU will finish the job in 4 hours and 4 CPUs in 1 hour. This means that we
      could use `express` partition for 4 CPU job in contrast to 1 CPU job requiring `short` partition. Since `express`
      partition has higher priority over `short` partition, use of 4 CPU is probably a better fit here.
* Reserve `--ntasks` only for MPI jobs. Don't know what that means? You likely need `--cpus-per-task`.


### Use of `mem` vs `mem-per-cpu`

In most circumstances, you should request memory using --mem. The exception is if you are running an MPI job that could
be placed on more than one node, with tasks divided up randomly, in which case --mem-per-cpu is more appropriate.

[Source](https://support.nesi.org.nz/hc/en-gb/articles/360001108756)


### How busy is cheaha?

One way is to use `load`.

```sh
$ load
Allocated nodes:      110
Idle nodes:           16
Total CPU cores:      3744
Allocated cores:      1768
Idle cores:           1340
Unavailable cores:    636
Running/Pending jobs: 527/1677
==========================================
% of used cores on Cheaha: 47.22%
% of used nodes on Cheaha: 87.30%
```
