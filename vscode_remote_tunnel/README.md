# VScode remote tunnel helper script

Helper script [start_vscode_tunnel.py](./start_vscode_tunnel.py) makes initiating a visual studio code remote tunnel in
cheaha easier. It performs the following tasks:

* creates and submits sbatch script to slurm
* waits for slurm job to start running and displays its log file to show github url and access code, which are needed to
  access the remote tunnel in VScode
* provides reasonable defaults 

> ⚠️ NOTE: This helper script was developed to use with [Cheaha at
> UAB](https://docs.rc.uab.edu/cheaha/getting_started/). It likely can be modified to suit other cluster environments.

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

# request for a particular node(s)
./start_vscode_tunnel.py --nodelist c[0167-0171]
```

## How to get started with VScode remote tunneling in Cheaha

Following are general instructions on how to start using VScode remote tunneling:

* SSH into [cheaha](https://docs.rc.uab.edu/cheaha/getting_started/)
* Download code cli tool (standalone binary) in cheaha

```sh
curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz
tar -xf vscode_cli.tar.gz
# move it to bin dir
mv code /home/$USER/bin
```

* If you haven’t already, add ~/bin/ dir to $PATH.  Be sure, `code -h` executes without any error.
* Run our helper script [start_vscode_tunnel.py](./start_vscode_tunnel.py) as described above.
* Output of the helper script will include a line with an 8-character code and a URL. Navigate to the URL on any browser
  and enter the code. 
  * *Important!* It is recommended not to use the https://vscode.dev/ URL provided. That URL leads to an instance of
    VSCode running on a third party cloud service (provided by Microsoft) and is not known to be approved for sensitive
    nor protected data! Instead, please use local VSCode installations only on trusted UAB machines (e.g., your laptop).
* Open VSCode on your *local, trusted machine*, click the `><` button in the lower-left of the main VSCode window to
  open the command palette. Select “Connect to Tunnel...” to find your tunnel. The names of tunnels started on Cheaha
  should be the same as the compute node hostname, e.g., `c0150`. You may be prompted to authenticate to GitHub.