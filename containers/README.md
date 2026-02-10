# Running RStudio & VS Code on CHEAHA

Instructions for running RStudio Server and VS Code Server on CHEAHA using Singularity containers.

## What You Get

- RStudio and VS Code running on compute nodes (not login nodes)
- Access to your home directory, data storage, and lab projects
- Persistent configurations and R libraries between sessions

## Prerequisites

- CHEAHA account with SSH access
- SSH key configured for tunneling from your local machine

## Quick Start

### 1. Get the Container Images

Pre-built containers are available at:
```
/data/project/worthey_lab/containers_temp
```

Or build your own using Apptainer (locally) and transfer to CHEAHA:
```bash
# On your local machine (with Apptainer installed)
apptainer build rstudio_custom.sif rstudio.def

# Transfer to CHEAHA
scp rstudio_custom.sif your_username@cheaha.rc.uab.edu:~/
```

**Note:** CHEAHA has Singularity for running containers. Apptainer is only needed locally if you want to build custom containers from `.def` files or pull from Docker.

### 2. Set Up Directories (One-Time)

```bash
mkdir -p ~/portable_rstudio_dirs/{etc/rstudio,home,run,tmp,var-lib,secure}
mkdir -p ~/code-server-base/{.config,.cache,home,run,tmp}
mkdir -p ~/singularity_sessions_slurm/logs
chmod 700 ~/portable_rstudio_dirs/secure
```

### 3. Submit the Job

```bash
sbatch rstudio/run_rstudio_slurm.sh
# or
sbatch vscode/run_code_server_slurm.sh
```

Check which compute node it's running on:
```bash
squeue -u $USER
```
Note the node name (e.g., `c0167`).

### 4. Create SSH Tunnel (From Your Local Machine)

```bash
# For VS Code (port 8769)
ssh -N -L 127.0.0.1:8769:127.0.0.1:8769 -J your_username@cheaha.rc.uab.edu your_username@c0167

# For RStudio (port 8799)
ssh -N -L 127.0.0.1:8799:127.0.0.1:8799 -J your_username@cheaha.rc.uab.edu your_username@c0167
```

Replace:
- `your_username` with your CHEAHA username
- `c0167` with the compute node from step 3

Keep this terminal open.

### 5. Open in Browser

- **VS Code**: http://localhost:8769
- **RStudio**: http://localhost:8799

## What Gets Mounted

### RStudio

Inside RStudio, you'll find:
- `~/cheaha_home` - your CHEAHA home directory
- `~/cheaha_data` - your `/data/user/$USER` directory  
- `~/nf1_rat_lw` - NF1 Rat Cohort project data

### VS Code

- `/mnt/cheaha_home` - your CHEAHA home directory
- `/mnt/cheaha_data` - your `/data/user/$USER` directory
- `/mnt/nf1_rat_lw` - NF1 Rat Cohort project data

## Job Settings

### RStudio
- 8 CPUs, 32 GB RAM
- 150 hours max runtime
- Port 8799

### VS Code  
- 8 CPUs, 32 GB RAM
- 8 hours max runtime
- Port 8769

Edit the SBATCH directives in the job scripts to change these.

## Adding More Mounts

Edit the `--bind` lines in your job script:

```bash
--bind "/data/project/worthey_lab/projects/your_project:/home/$USER/my_project"
```

## R Packages

R packages install to a persistent location automatically:

```r
install.packages("ggplot2")
.libPaths()  # check where packages are stored
```

## Tools Included

- samtools, bcftools, bedtools
- CNVkit (in VS Code container via Micromamba)
- HDF5, Arrow libraries
- Standard compression tools

## Managing Jobs

```bash
# Check running jobs
squeue -u $USER

# Cancel a job
scancel <JOB_ID>

# Check logs
cat ~/singularity_sessions_slurm/logs/rstudio_sing_<JOB_ID>.err
```

## Troubleshooting

**Can't connect?**
- Check job is running: `squeue -u $USER`
- Check logs: `cat ~/singularity_sessions_slurm/logs/*.err`
- Make sure SSH tunnel is still open
- Verify you're using the right compute node in your SSH command

## Notes

- CHEAHA uses Singularity to run containers
- Apptainer is only needed locally if you want to build your own containers
- R packages and VS Code settings persist between sessions
- For large file transfers, use `rsync` instead of the SSH tunnel
