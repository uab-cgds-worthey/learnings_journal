# Building RStudio Container

## Prerequisites

- Apptainer installed on your local machine (Windows WSL2, Linux, or Mac)

## Build

```bash
apptainer build rstudio_custom_4.4.2.sif rstudio.def
```

That gives you `rstudio_custom_4.4.2.sif` to transfer to CHEAHA.

## What's Inside (Quick Flavor)

This is not a plain RStudio image. It comes with a stack of tools I mostly use. I also built this while running PureCN, which needs CNVkit for one of its steps:
- CNVkit (via Micromamba)
- samtools, bcftools, bedtools, tabix
- Python 3 with common scientific packages
- Micromamba (so you can manage extra envs if needed)

## Transfer to CHEAHA

```bash
scp rstudio_custom_4.4.2.sif your_username@cheaha.rc.uab.edu:~/
```

Or just grab it with Cyberduck/FileZilla if you prefer a UI.

## Notes

- I tested higher version tags (4.5), but Singularity/Apptainer on CHEAHA works well up to 4.4.2 right now
- If CHEAHA updates their OS, this might change
