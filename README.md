# experiments

This repository is a template for the [cradle](https://github.com/cvxgrp/cradle)
system.

Here we support the creation of notebooks without the ambition to release software.
The repo is not minimalistic but comes with a curated set of pre-commit hooks and
follows modern and established guidelines.

* uv support
* curated pre-commit-hooks
* DevContainer
* github ci/cd workflows
* Makefile
* marimo support

```bash
    create  requirements.txt
    create  .pre-commit-config.yaml
    create  README.md
    create  .devcontainer
    create  .devcontainer/startup.sh
    create  .devcontainer/devcontainer.json
    create  .gitignore
    create  .github
    create  .github/workflows
    create  .github/workflows/marimo.yml
    create  .github/dependabot.yml
    create  .python-version
    create  Makefile
    create  notebooks
    create  notebooks/minimal enclosing circle.py
    create  notebooks/{{ project_lower }}.py
```
