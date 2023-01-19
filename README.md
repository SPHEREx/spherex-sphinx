# spherex-sphinx

[Sphinx documentation](https://www.sphinx-doc.org/en/master/) configurations and extensions for SPHEREx.

Install with `pip`:

```sh
pip install git+https://github.com/SPHEREX/spherex-sphinx.git@main
```

Read more at https://spherex-docs.ipac.caltech.edu/spherex-sphinx/

spherex-sphinx is developed by SPHEREx at https://github.com/SPHEREx/spherex-sphinx.

## Features

<!-- A bullet list with things that this package does -->
- Sphinx configuration for SPHEREx Sphinx documentation projects, featuring the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

## Developing spherex-sphinx

The best way to start contributing to spherex-sphinx is by cloning this repository, creating a virtual environment, and running the `make init` command:

```sh
git clone https://github.com/SPHEREx/spherex-sphinx.git
cd spherex-sphinx
make init
```

You can run tests and build documentation with [tox](https://tox.wiki/en/latest/):

```sh
tox
```

To learn more about the individual environments:

```sh
tox -av
```
