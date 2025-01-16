# experiments

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![CI](https://github.com/tschm/experiments/actions/workflows/ci.yml/badge.svg)](https://github.com/tschm/experiments/actions/workflows/ci.yml)
[![Created for Cradle](https://img.shields.io/badge/Created%20for-Cradle-blue?style=flat-square)](https://github.com/cvxgrp/cradle)

We support the creation of notebooks without the ambition to release software.
The repo is not minimalistic but comes with a curated set of pre-commit hooks
and follows modern and established guidelines.

* Uses uv for dependency management
* Offers a list of curated pre-commit hooks
* GitHub Actions for continuous integration
* Code formatting with ruff
* Interactive notebooks with marimo
* Support of a DevContainer

## Table of Contents

* [Usage](#usage)
* [Development Commands](#development-commands)
* [License](#license)
* [Contributing](#contributing)
* [Contact](#contact)

## Usage

This is serving as a feeder into the [cradle](https://github.com/cvxgrp/cradle)
system only. It's not a traditional Python package and does not
require installation although you could clone the repository
and start using the provided notebooks and tools.

1. Clone the repository:

    ```bash
    git clone https://github.com/tschm/package.git
    ```

2. Navigate to the project directory:

    ```bash
    cd package
    ```

## Development Commands

```bash
make fmt     # Install pre-commit hooks and run them on all files
```

## Contributing

* Fork the repository
* Create your feature branch (git checkout -b feature/amazing-feature)
* Commit your changes (git commit -m 'Add some amazing feature')
* Push to the branch (git push origin feature/amazing-feature)
* Open a Pull Request

## Contact

Thomas Schmelzer - [@tschm](https://github.com/tschm)

Project Link: <https://github.com/tschm/package>
