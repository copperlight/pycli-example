[![Snapshot](https://github.com/copperlight/pycli-example/actions/workflows/snapshot.yml/badge.svg)](https://github.com/copperlight/pycli-example/actions/workflows/snapshot.yml) [![Release](https://github.com/copperlight/pycli-example/actions/workflows/release.yml/badge.svg)](https://github.com/copperlight/pycli-example/actions/workflows/release.yml)

## Introduction

This project provides a minimal example of CLI application packaging for Python.

## Installation

This package supports Python >= 3.6.

Install:

```
pip3 install git+https://github.com/copperlight/pycli-example.git
```

Upgrade:

```
pip3 install --upgrade git+https://github.com/copperlight/pycli-example.git
```

## Local Development

Setup and activate a virtualenv, for local development:

```shell
./setup-venv.sh
source venv/bin/activate
```

Run tests locally:

```
pytest
```

Run the latest version locally, so you can skip installing the package and cycle faster: 

```
python3 ./pycli_example/cmd.py -h
```

Install the CLI app in the virtualenv, so you can run it as a user would:

```shell
python3 setup.py install
pycli-example -h
pycli-example -n Frasier
```

## Release Process

* Make some changes.
* Bump the version in [setup.py](./setup.py), maybe following [Semantic Versioning](https://semver.org/).
* Update the [CHANGELOG.md](./CHANGELOG.md).
* Push the changes.
* Upgrade the package on user systems.
