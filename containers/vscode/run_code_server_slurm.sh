#!/bin/bash
#
#SBATCH --job-name=code-server_singularity
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --partition=amd-hdr100,intel-dcb,largemem,long,medium,short
#SBATCH --time=8:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

set -euo pipefail

# See containers/README.md for usage details

USER="$(whoami)"
BASE="$HOME/code-server-base"
IMG="/data/project/worthey_lab/containers_temp/code-server_4.108.2.sif"
PORT=8769

mkdir -p "$BASE"/{.config,.cache,home,run,tmp}

cheaha_usr_home="/home/$USER"
cheaha_usr_data="/data/user/$USER"
worthey_lab_projects="/data/project/worthey_lab/projects/"  # replace with your own project path

singularity exec \
  --bind "$BASE/home/:/home/$USER" \
  --bind "$BASE/.config:/home/$USER/.config" \
  --bind "$BASE/.cache:/home/$USER/.cache" \
  --bind "$cheaha_usr_home:/mnt/cheaha_home" \
  --bind "$cheaha_usr_data:/mnt/cheaha_data" \
  --bind "$worthey_lab_projects:/mnt/worthey_lab_projects" \
  "${IMG}" \
  code-server --bind-addr="127.0.0.1:${PORT}" --auth=none
