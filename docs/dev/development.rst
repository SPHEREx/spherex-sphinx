#################
Development guide
#################

This page provides procedures and guidelines for developing and contributing to spherex-sphinx.

.. _dev-environment:

Setting up a local development environment
==========================================

To develop spherex-sphinx, create a virtual environment with your method of choice (like virtualenvwrapper) and then clone or fork, and install:

.. code-block:: sh

   git clone https://github.com/lsst-sqre/spherex-sphinx.git
   cd spherex-sphinx
   make init

This init step does three things:

1. Installs spherex-sphinx in an editable mode with its "dev" extra that includes test and documentation dependencies.
2. Installs pre-commit and tox.
3. Installs the pre-commit hooks.

You must have Docker installed and configured so that your user can start Docker containers in order to run the test suite.

.. _pre-commit-hooks:

Pre-commit hooks
================

The pre-commit hooks, which are automatically installed by running the :command:`make init` command on :ref:`set up <dev-environment>`, ensure that files are valid and properly formatted.
Some pre-commit hooks automatically reformat code:

``isort``
    Automatically sorts imports in Python modules.

``black``
    Automatically formats Python code.

``blacken-docs``
    Automatically formats Python code in reStructuredText documentation and docstrings.

When these hooks fail, your Git commit will be aborted.
To proceed, stage the new modifications and proceed with your Git commit.

.. _dev-run-tests:

Running tests
=============

To test the library, run tox_, which tests the library the same way that the CI workflow does:

.. code-block:: sh

   tox

To see a listing of test environments, run:

.. code-block:: sh

   tox -av

To run a specific test or list of tests, you can add test file names (and any other pytest_ options) after ``--`` when executing the ``py`` tox environment.

.. _dev-build-docs:

Building documentation
======================

Documentation is built with Sphinx_:


.. code-block:: sh

   tox -e docs

The built documentation is located in the :file:`docs/_build/html` directory.
