# Common Startup Scripts
Scripts to create shared bash and zsh commands for Cheaha.

## Scripts
### `.recommended_startup_commands`
A script with all recommended commands based on commonly used pipelines, directories, and tools. 
#### **How to use**
Locate `.bashrc` and `.zshrc` in the `$HOME` directory and add the following lines:
```bash
if [ -f "/data/project/worthey_lab/tools/learnings_journal/startup_scripts/.recommended_startup_commands"]; then
    . "/data/project/worthey_lab/tools/learnings_journal/startup_scripts/.recommended_startup_commands"
fi
```
#### **commands**
| Command                                | Purpose                                                                                                                             |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| projects                               | Change directory to the projects directory (`/data/project/worthey_lab/projects`)                                                   |
| worthey_lab                            | Change directory to the lab space (`/data/project/worthey_lab`)                                                                     |
| exp_pipes \<directory_name\> | Change directory to experimental pipelines directory (`/data/project/worthey_lab/projects/experimental_pipelines/<directory_name>`) |
| scratch                                | Change directory to user scratch directory                                                                                          |
| codicem                                | Load codicem                                                                                                                        |
| congenica                              | Load congenica                                                                                                                      |
| smvp_logs                              | Change directory to logs for small variant caller pipeline                                                                          |
| smvp_stat n                            | Get status of jobs running small variant caller pipeline                                                                            |
| svp_logs                               | Change directory to logs for manta sv caller pipeline                                                                               |
| svp_stat n                             | Get status of jobs running manta sv caller pipeline                                                                                 |
| srun_simple                            | Start a simple interactive session                                                                                                  |
| srun_medium                            | Start an interactive session using medium partition                                                                                 |
| srun_express                           | Start an interactive session using express partition                                                                                |
| SC                                     | Well formatted sacct                                                                                                                |
| SQ                                     | Well formatted squeue                                                                                                               |
| SQ_long                                | Well formatted squeue with submission time and command ran info                                                                     |
| njobs                                  | Number of jobs running                                                                                                              |
| scontr jobid                           | Information for a particular job                                                                                                    |
| SR jobid                               | Status information for a job                                                                                                        |


### `.helpful_startup_commands`
This script contains optional commands that are useful.
#### **How to use**
Locate `.bashrc` and `.zshrc` in `$HOME` and add the following lines:
```bash
if [ -f "/data/project/worthey_lab/tools/learnings_journal/startup_scripts/.helpful_startup_commands"]; then
    . "/data/project/worthey_lab/tools/learnings_journal/startup_scripts/.helpful_startup_commands"
fi
``` 
#### **commands**
| Command               | Purpose                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------|
| rmi file              | Interactive remove                                                                                 |
| cpi                   | Interactive copy when overwriting a file                                                           |
| mvi \<source\> \<target\> | Interactive move when overwriting a file                                                           |
| ll                    | List files in long format                                                                          |
| data                  | Change directory to user data directory                                                            |
| home                  | Change directory to user home directory                                                            |
| ds                    | Obtain accurate disk usage information                                                             |
| interbig              | Start an interactive session with large amount of resources (--cpus-per-task=4 --mem-per-cpu=4096) |
| intersmall            | Start an interactive session with less resources (--cpus-per-task=1 --mem-per-cpu=2048)            |
