# learnings_journal

Repository to document tips and tricks we learn on how to use certain tools.

> **_NOTE:_**  In a past life, this repo used a different remote Git management provider, [UAB
> Gitlab](https://gitlab.rc.uab.edu/center-for-computational-genomics-and-data-science/sciops/learnings_journal). It was migrated to
> Github in June 2023, and the Gitlab version has been archived.


## Topics

* [Containers](./docs/containers.md)
* [Snakemake](./docs/snakemake.md)
* [Slurm](./docs/slurm.md)
* [Random tips and tricks](./docs/random_stuff.md)
* [Startup scripts](./startup_scripts)
* [VScode and remote tunnels](./vscode_remote_tunnel)

## Documentation

This repository uses MkDocs for the documentation site.

```sh
python3 -m venv venv
python3 -m pip install -r requirements.txt
mkdocs serve
```

The GitHub Actions workflow builds the documentation and deploys it to GitHub Pages after changes are merged to `main` or `master`.
