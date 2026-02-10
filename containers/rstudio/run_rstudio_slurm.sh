#!/bin/bash
#
#SBATCH --job-name=rstudio_singularity
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --partition=amd-hdr100,intel-dcb,largemem,long
#SBATCH --time=150:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

set -euo pipefail

# See containers/README.md for usage details

USER="$(whoami)"
PORT=8799
BASE="$HOME/rstudio_base"
IMG="/data/project/worthey_lab/containers_temp/rstudio_custom_4.4.2.sif"

mkdir -p "$BASE"/{etc/rstudio,home,run,tmp,var-lib,secure}
chmod 700 "$BASE/secure"

if [ ! -f "$BASE/secure/secure-cookie-key" ]; then
  head -c 64 /dev/urandom | base64 > "$BASE/secure/secure-cookie-key"
  chmod 600 "$BASE/secure/secure-cookie-key"
fi

mkdir -p "$BASE/home/R_libs"
chmod 755 "$BASE/home/R_libs"

cat > "$BASE/etc/rstudio/rserver.conf" <<EOF
www-address=127.0.0.1
www-port=$PORT
auth-none=1
secure-cookie-key-file=/home/$USER/secure/secure-cookie-key
EOF

mkdir -p "$BASE/home"/{cheaha_home,cheaha_data,worthey_lab_projects}

cheaha_usr_home="/home/$USER"
cheaha_usr_data="/data/user/$USER"
worthey_lab_projects="/data/project/worthey_lab/projects/"  # replace with your own project path

export SINGULARITYENV_R_LIBS_USER="/home/$USER/R_libs"

unset R_LIBS R_LIBS_SITE R_HOME

singularity exec \
  --bind "$BASE/home:/home/$USER" \
  --bind "$BASE/run:/run" \
  --bind "$BASE/tmp:/tmp" \
  --bind "$BASE/var-lib:/var/lib/rstudio-server" \
  --bind "$BASE/etc/rstudio:/etc/rstudio" \
  --bind "$BASE/secure:/home/$USER/secure" \
  --bind "$cheaha_usr_home:/home/$USER/cheaha_home" \
  --bind "$cheaha_usr_data:/home/$USER/cheaha_data" \
  --bind "$worthey_lab_projects:/home/$USER/worthey_lab_projects" \
  "$IMG" \
  /usr/lib/rstudio-server/bin/rserver \
    --server-daemonize=0 \
    --server-user="$USER"
