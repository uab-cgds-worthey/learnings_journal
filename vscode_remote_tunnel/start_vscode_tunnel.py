#!/usr/bin/env python3

"""
Helper script to run vscode remote tunnel job in slurm
* provides reasonable defaults but they are configurable
* creates and submits sbatch script to slurm
* waits for log file and shows github url and access code
"""

from pathlib import Path
import os.path
import subprocess
import tempfile
import time
import argparse


def get_full_path(x):
    full_path = Path(x).resolve()

    return str(full_path)


def create_dirpath(arg):
    dpath = get_full_path(os.path.expandvars(arg))
    if not Path(dpath).is_dir():
        Path(dpath).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dpath}")

    return dpath


def write_script(cpu, mem_per_cpu, partition, logdir):
    "constructs slurm job script and writes to file"

    Path(logdir).mkdir(parents=True, exist_ok=True)

    script_txt = f"""\
#!/bin/bash
#
#SBATCH --job-name=vscode_tunnel
#SBATCH --ntasks=1
#SBATCH --cpus-per-task={cpu}
#SBATCH --mem={mem_per_cpu}
#SBATCH --partition={partition}
#SBATCH --output={logdir}/%x_%j.log

code tunnel --name cheaha_tunnel
    """

    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", delete=False
    ) as script_fpath:
        script_fpath.write(script_txt)

    return script_fpath.name


def run_shell_command(command, fpath):

    result = subprocess.run([command, fpath], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

    return result.stdout.decode("utf-8")


def print_job_logs(log_dpath, sbatch_out):
    "Waits for slurm job logfile to exist and reads its contents"

    jobid = sbatch_out.strip().split(" ")[-1]
    log_fpath = Path(log_dpath) / f"vscode_tunnel_{jobid}.log"

    try:
        int(jobid)
    except ValueError:
        print(f"ERROR: Job id '{jobid}' not an integer")
        raise SystemExit(1)

    print(f"Waiting for slurm job '{jobid}' to start...")
    sleep_time = 1
    while not log_fpath.exists():
        time.sleep(1)

        if sleep_time > 10:
            print("Still waiting...")
            sleep_time = 1
        else:
            sleep_time += 1

    time.sleep(3)  # give vscode time to setup server

    # now print the file contents
    run_shell_command("cat", log_fpath)

    return None


def main(args):

    # construct script to submit to slurm
    script_fpath = write_script(args.cpu, args.mem_per_cpu, args.partition, args.logdir)

    # submit script to slurm or print its contents
    if args.print_script:
        run_shell_command("cat", script_fpath)
    else:
        sbatch_out = run_shell_command("sbatch", script_fpath)

    # wait for job to start and print log file contents.
    # this helps with showing github link and access code
    print_job_logs(args.logdir, sbatch_out)

    return None


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description="Helper script to initiate vscode remote tunneling",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    PARSER.add_argument(
        "-c",
        "--cpu",
        help="No. of CPUs to request",
        default=2,
        metavar="",
    )

    PARSER.add_argument(
        "-m",
        "--mem-per-cpu",
        help="Memory per CPU to request",
        default="8G",
        metavar="",
    )

    PARSER.add_argument(
        "-p",
        "--partition",
        help="Slurm partition to request",
        default="express",
        metavar="",
    )

    LOGDIR_DEFAULT = "/data/user/${USER}/logs/vscode_tunneling/"
    PARSER.add_argument(
        "-l",
        "--logdir",
        help="Dirpath to store log files",
        default=LOGDIR_DEFAULT,
        type=lambda x: create_dirpath(x),
        metavar="",
    )

    PARSER.add_argument(
        "-ps",
        "--print-script",
        action="store_true",
        help="Print script instead of submitting it as slurm job",
    )

    ARGS = PARSER.parse_args()

    main(ARGS)
