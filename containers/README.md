# Running RStudio & VS Code on CHEAHA

Short overview and quick steps for running RStudio Server and VS Code Server on CHEAHA using Singularity containers.

## Overview

- Runs on compute nodes (not login nodes)
- Mounts your home, data, and project directories
- Persistent settings between sessions
- Pre-built containers live at:
```
/data/project/worthey_lab/containers_temp
```

## Run Containers

### One-Time Setup

```bash
mkdir -p ~/rstudio_base/{etc/rstudio,home,run,tmp,var-lib,secure}
mkdir -p ~/code-server-base/{.config,.cache,home,run,tmp}
mkdir -p ~/singularity_sessions_slurm/logs
chmod 700 ~/rstudio_base/secure
```

### Run RStudio

```bash
sbatch rstudio/run_rstudio_slurm.sh
squeue -u $USER
```

Tunnel from your local machine (replace `your_username` and the node name):
```bash
ssh -N -L 127.0.0.1:8799:127.0.0.1:8799 -J your_username@cheaha.rc.uab.edu your_username@c0167
```

Open: http://localhost:8799

### Run VS Code

```bash
sbatch vscode/run_code_server_slurm.sh
squeue -u $USER
```

Tunnel from your local machine (replace `your_username` and the node name):
```bash
ssh -N -L 127.0.0.1:8769:127.0.0.1:8769 -J your_username@cheaha.rc.uab.edu your_username@c0167
```

Open: http://localhost:8769

## Build or Modify Containers

- CHEAHA uses Singularity to run containers
- Apptainer is only needed locally if you want to build custom containers
- RStudio build details: see [containers/rstudio/README.md](containers/rstudio/README.md)
- VS Code build README will be added later

## Mounts (Quick)

- RStudio: `~/cheaha_home`, `~/cheaha_data`, `~/your_project`
- VS Code: `/mnt/cheaha_home`, `/mnt/cheaha_data`, `/mnt/your_project`
