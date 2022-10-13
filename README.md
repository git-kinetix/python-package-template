# python-package-template

This repository contains the boilerplate code for a Python module that allows us to read and write FBX files.

# Contents

- `.github` contains unit tests workflows and everything related to github processes (code owners, pull request template, dependabot...) 
- `{{package_name}}` contains the source files of the package.
- `setup.py` tells pip and other python package managers how to install our package.
- `.pre-commit-config.yaml` contains our pre-commit hooks to ensure a clean development process
- `requirements.txt` contains a list of the python packages required by this module
- `tests/` is a folder containing tests to be run with pytest.
