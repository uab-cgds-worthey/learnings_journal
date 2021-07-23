# Common RC Scripts
Scripts to create shared bash and zsh commands for Cheaha.

## Scripts
### .requiredrc
A script with all the commands required based on commonly used pipelines, directories, and tools. 
#### **How to use**
Locate `.bashrc` and `.zshrc` in the `$HOME` directory and add the following lines:
```bash
if [ -f "/data/project/worthey_lab/tools/learnings_journal/rc_scripts/.requiredrc"]; then
    . "/data/project/worthey_lab/tools/learnings_journal/rc_scripts/.requiredrc"
fi
```
#### **commands**
Change directory to the projects directory (`/data/project/worthey_lab/projects`)
```shell
projects
```

Change directory to the lab space (`/data/project/worthey_lab`)
```shell
worthey_lab
```

Change directory to experimental pipelines directory (`/data/project/worthey_lab/projects/experimental_pipelines/<directory_name>`)
```shell
experimental_pipeline <directory_name>
```

Change directory to user scratch directory
```shell
scratch
```

Load codicem
```shell
codicem
```

Load congenica
```shell
congenica
```

Change directory to logs for small variant caller pipeline
```shell
smvp_logs
```

Get status of jobs running small variant caller pipeline 
```shell
smvp_stat n
```

Change directory to logs for manta sv caller pipeline
```shell
svp_logs
```

Get status of jobs running manta sv caller pipeline
```shell
svp_stat n
```

Start a simple interactive session
```shell
srun_simple
```

Start a interactive session using medium partition
```shell
srun_medium
```

Start a interactive session using express partition
```shell
srun_express
```

Well formatted sacct
```shell
SC
```

Well formatted squeue
```shell
SQ
```

Well fromatted squeue with submission time and command ran information
```shell
SQ_long
```

Number of jobs running 
```shell
njobs
```

Information for a particular job
```shell
scontr jobid
```

Status information for a job
```shell
SR jobid
```

### `.recommendedrc`
This script contains optional commands that are useful.
#### **How to use**
Locate `.bashrc` and `.zshrc` in `$HOME` and add the following lines:
```bash
if [ -f "/data/project/worthey_lab/tools/learnings_journal/rc_scripts/.recommendedrc"]; then
    . "/data/project/worthey_lab/tools/learnings_journal/rc_scripts/.recommendedrc"
fi
``` 
#### **commands**
Interactive remove
```shell
rmi file
```

Interactive copy
```shell
cpi file
```

Interactive move 
```shell
mvi <source> <target>
```

List files in long format
```shell
ll
```

Change directory to user data directory
```shell
data
```

Change directory to user home directory
```shell
home
```

Obtain accurate disk usage information 
```shell
ds
```

Start an interactive session with large amount of resources (`--cpus-per-task=4 --mem-per-cpu=4096`)
```shell
inodebig
```

Start an interactive session with less resources (`--cpus-per-task=1 --mem-per-cpu=2048`)
```shell
inodesmall
```

Activate a conda environment
```shell
conda_activate <env_name>
```

Deactivate a conda environment
```shell
conda_deactivate
```