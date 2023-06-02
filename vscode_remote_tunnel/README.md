# VScode remote tunnel helper script

Helper script [start_vscode_tunnel.py](./start_vscode_tunnel.py) makes initiating a visual studio code remote tunnel in cheaha easier. It performs the following tasks:

* creates and submits sbatch script to slurm
* waits for slurm job to start running and displays its log file to show github url and access code, which are needed to access the remote tunnel in VScode
* provides reasonable defaults 


## Requirements

* Python3

## Usage

Run the script in slurm cluster.

```sh
# to run with defaults
./start_vscode_tunnel.py

# to see help message
./start_vscode_tunnel.py -h

# example custom usage
./start_vscode_tunnel.py --cpu 4 --mem-per-cpu "4G" --partition short 
```