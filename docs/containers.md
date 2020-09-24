- [Containers](#containers)
  - [Tutorial resources](#tutorial-resources)
  - [Singularity](#singularity)
    - [Troubleshooting:](#troubleshooting)
      - [Using snakemake with Singularity and Conda](#using-snakemake-with-singularity-and-conda)
  - [Using docker containers from private gitlab registry](#using-docker-containers-from-private-gitlab-registry)
    - [Docker](#docker)
    - [Singularity](#singularity-1)

# Containers

## Tutorial resources

* [Research Computing's tutorial on Singularity](https://gitlab.rc.uab.edu/rc-training-sessions/singularity_containers/-/tree/master)


## Singularity

- By default singularity bind mounts `/home/$USER`, `/tmp`, and `$PWD` into your container at runtime. [Source](https://singularity.lbl.gov/quickstart#working-with-files).
  - If mounting home is undesirable, it may be turned off. For singularity run, these options are available:

    ```sh
    -H|--home <spec>    A home directory specification.  spec can either be a
                        src path or src:dest pair.  src is the source path
                        of the home directory outside the container and dest
                        overrides the home directory within the container
    --no-home           Do NOT mount users home dire
    ```

    - Use `--no-home` if mounting home dir is not needed or undesirable.
    - Use`--home` if the container expects a home directory. Example usage:  `--home ${PWD}/tmp:$HOME`

  - IT would be happy if tmp directory is pointed instead to a scratch directory, as singularity containers may fill /tmp up fast.
    - Example: `--bind /data/user/jdoe/tmp:/tmp`
  - If you develop and build container first with docker and then pull into singularity, follow the [suggestions from Singularity folks](https://singularity.lbl.gov/quickstart#working-with-files) to avoid surprises.



### Troubleshooting:

#### Using snakemake with Singularity and Conda

- When using singularity+conda with snakemake, node's `/tmp` get used during creation of conda environment instead of user-supplied directory via singularity's `--bind` option. I reported this bug here - https://github.com/snakemake/snakemake/issues/193.
  - This doesn't affect the jobs run by snakemake, thankfully.
  - Solution: Workaround is to create conda environment in compute node and when snakemake fails with `CreateCondaEnvironmentException` and `NoSpaceLeftError`, then:
    - remove dir `/tmp/conda` from that node manually
    - restart snakemake so that it completes creation of remaining conda environments.
    - When done creating all conda environments, be a good samaritan and delete dir `/tmp/conda` so that it doesn't affect other users using that node and IT doesn't hate you.


## Using docker containers from private gitlab registry

Gitlab's docs - https://docs.gitlab.com/ee/user/packages/container_registry/#authenticating-to-the-gitlab-container-registry

### Docker

```sh
# needs personal access token if you have 2-factor authentication enabled - https://docs.gitlab.com/ee/user/packages/container_registry/#authenticating-to-the-gitlab-container-registry
docker login  gitlab.rc.uab.edu:4567

# Example: pull from registry
URL="gitlab.rc.uab.edu:4567/center-for-computational-genomics-and-data-science/utility-images/static-analysis:v0.1"
docker pull "$URL"
```

### Singularity

See Singularity's doc on [making use of private images from Private Registries](https://sylabs.io/guides/3.5/user-guide/singularity_and_docker.html#making-use-of-private-images-from-private-registries)

```sh
# this will interactively ask for blazer credentials. For username, user blazer id without "@uab.edu"
singularity pull --docker-login "docker://${URL}"

# If interactively providing credentials is not desired, they may be passed via singularity env variables
# Don't enter plain passwords for env variables though. One not-so-great-but-still-better workaround is
# to assign using password stored in a user-read-only files.
# This may be desired for cases that use containers from private registry.
export SINGULARITY_DOCKER_USERNAME='blazer_id'
export SINGULARITY_DOCKER_PASSWORD=<redacted>
singularity pull "docker://${URL}"
```
