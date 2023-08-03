# xyrha-cookiecutter-pypackage

A cookiecutter template for a simple python package with strict linting and formatting rules.

## Features

- Use `tox` to lint, test, build the docs and build the package.
- Lint with:
  - `black`
  - `ruff`
  - `mypy`
  - `pylint`
- Use `pytest` to write unit and integration tests.
- Build a `sphinx` documentation with a `sphinx_material` theme.

## Create a new project

Use `cruft` to create and update your package with the latest development of the template.
Alternatively, use `cookiecutter` to create your package without `cruft`.
As a first optional step, create a new virtual environment and install necessary dependencies.

``` shell
python3.12 -m venv venv
source venv/bin/activate
pip install cruft isort black
cruft create git@github.com:xyrha/xyrha-cookiecutter-pypackage.git
```

### Updating an existing project

- Use `cruft check` to check for template updates.
- Use `cruft update` to update to a new version fo the template.

## Usage

- Use `tox` to lint and test your package.
- Use `tox -e py312-lint` to only execute the lint stage.
- Use `tox -e py312-test` to only execute the test stage.
- Use `tox -e docs` to build the docs.
- Use `tox -e build` to build the package.
- Use `pip install -e .[dev]` to install all defined dependencies for development into your current environment.
