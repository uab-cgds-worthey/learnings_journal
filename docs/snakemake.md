# Snakemake

## Issues

### Not removing output files of failed jobs in cluster

When a snakemake job fails, its typical behavior is to remove its output files as they may be incomplete, corrupted, etc. When used in HPC cluster though, [snakemake can't always detect when a job has failed](https://stackoverflow.com/q/52500725/3998252). For example, it can't detect a job was cancelled by user, killed by job scheduler slurm (for example, ran out of allocated memory, etc), etc. We can make snakemake be aware of such job fails, to certain extent, by using a [custom script with  `--cluster-status` option](https://stackoverflow.com/a/59253812/3998252).

However, this is not a fool-proof solution as snakemake won't automatically remove output files of such failed jobs. In some cases it may tag them as incomplete and will warn when the pipeline is rerun, but this does not always happen. *Hence, it is highly recommended to manually review such failures and remove the output files manually.*
