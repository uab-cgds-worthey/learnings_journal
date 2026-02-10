# Building VS Code Container

## Prerequisites

- Apptainer installed on your local machine (Windows WSL2, Linux, or Mac)

## Build

```bash
apptainer build code-server_4.108.2.sif code-server.def
```

That gives you `code-server_4.108.2.sif` to transfer to CHEAHA.

## What's Inside

Direct Docker pull of code-server version 4.108.2. Just VS Code Server, nothing extra.

## Transfer to CHEAHA

```bash
scp code-server_4.108.2.sif your_username@cheaha.rc.uab.edu:~/
```

Or just grab it with Cyberduck/FileZilla if you prefer a UI.
