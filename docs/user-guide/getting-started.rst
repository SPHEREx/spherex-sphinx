###############
Getting started
###############

spherex-sphinx provides base configurations and extensions for SPHEREx's Sphinx_\ -based documentation projects.
This page shows you how to set up a new documentation project, such as a Python package's documentation or a standalone documentation site, with spherex-sphinx.

Installation
============

spherex-sphinx needs to be part of your project's Python dependencies.
How dependencies are declared depends on the nature of the project.
The following are some common patterns.

.. tab-set::

   .. tab-item:: pyproject.toml

      Often in a Python package, development and documentation-only dependencies are installed via an "extra" rather than in the main dependencies list:

      .. code-block:: toml
         :caption: pyproject.toml

         [project.optional-dependencies]
         docs = [
             "spherex-sphinx @ git+https://github.com/SPHEREX/spherex-sphinx.git@main"
         ]

   .. tab-item:: requirements.txt

      If using a pip requirements file, you can specify the spherex-sphinx dependency like this:

      .. code-block:: text
         :caption: requirements.txt

         git+https://github.com/SPHEREX/spherex-sphinx.git@main

   .. tab-item:: pip

      You can directly install spherex-sphinx into your Python environment:

      .. code-block:: sh

         pip install git+https://github.com/SPHEREX/spherex-sphinx.git@main


Add a Sphinx configuration file, conf.py
========================================

Every Sphinx project needs a :file:`conf.py` file that provides its configuration.
spherex-sphinx provides a base module, :doc:`spherexsphinx.conf.base <base-config>`, that configures your project to match SPHEREx's documentation standards.
At the base of your documentation project (which might be the ``docs`` directory for a software documentation project, or the Git repository's root directory for a standalone documentation site), add this ``conf.py`` file:

.. code-block:: py
   :caption: docs/conf.py

   """The Sphinx configuration is derived from spherexsphinx.conf.base
   and can be extended by setting additional variables after the import.
   """

   from spherexsphinx.conf.base import *

.. note::

   As the comment mentions, you can add additional Sphinx configurations (for both Sphinx and its extensions) by setting variables *after* the import.
   Keep in mind that the ``conf.py`` module's namespace is populated by any variable set in :doc:`spherexsphinx.conf.base <base-config>`.
   You can refer to :doc:`base-config` to see what those variables are.

Add a spherex-sphinx configuration file, spherex.toml
=====================================================

spherex-sphinx uses a :doc:`spherex.toml <spherex-toml>` file, located in the same directory as ``conf.py``, to abstract many of the details of the standard Sphinx ``conf.py`` file.
This is a `TOML <https://toml.io/en/>`__\ -formatted file.
Add and customize this ``spherex.toml`` file:

.. code-block:: toml
   :caption: docs/spherex.toml

   [project]
   title = "SPHEREx Sphinx"
   copyright = "2022 California Institute of Technology"
   base_url = "https://spherex-docs.ipac.caltech.edu/spherex-sphinx/"
   github_url = "https://github.com/SPHEREx/spherex-sphinx"

   [sphinx.intersphinx.projects]
   python = "https://docs.python.org/3"
   astropy = "https://docs.astropy.org/en/stable/"

See :doc:`spherex-toml` for details.

The ``[sphinx.intersphinx.projects]`` table is for configuring Intersphinx_, an extension that enables you to link to items like sections and APIs in other Sphinx_ documentation projects.
Add the names and root documentation URLs of any projects that your project will link to.

Add a substitutions and links file, _rst_epilog.rst
===================================================

This is an optional file that you can add in the same directory as both ``spherex.toml`` and ``conf.py``.
Its contents are automatically added to each reStructuredText source file and is a great place to put common link definitions and substitutions for your documentation project.
An example:

.. code-block:: rst
   :caption: docs/_rst_epilog.rst

   .. _SPHEREx: https://spherex.caltech.edu

   .. |done| replace:: :bdg-success:`Done`
   .. |todo| replace:: :bdg-primary-line:`To-do`
   .. |inprogress| replace:: :bdg-seconday-line:`To-do`

The first item is a reusable link definition.
With it, you can type ``SPHEREx_`` in your reStructuredText documentation to create a link to the SPHEREx homepage, labeled "SPHEREx."

The last three items use reStructuredText's substitutions syntax.
You can type ``|done|`` in your documentation, and it expands into the content after the ``replace::``, i.e., :bdg-success:`Done`.

Add a Makefile for the documentation
====================================

Its convenient to use a Makefile for common documentation tasks.
Use this as a starting point:

.. code-block:: makefile
   :caption: docs/Makefile

   .PHONY: html
   html:
   	sphinx-build --keep-going -n -T -b html -d _build/doctrees . _build/html

   .PHONY: clean
   clean:
   	rm -rf api
   	rm -rf _build

Add a .gitignore file for the documentation build products
==========================================================

Typical Sphinx projects have two output directories that should be ignored by version control: ``_build`` (where the built HTML is created) and ``api`` (created automatically by `sphinx-automodapi`_).
This is a typical ``.gitignore`` file that can be added to the ``docs`` directory (or the root of the Sphinx project, generally):

.. code-block:: text
   :caption: docs/.gitignore

   _build/
   api/

Register the documentation project
==================================

To deploy the documentation project to the SPHEREx documentation site, you need to register it though the IPAC docs API (also known as LTD or *LSST the Docs*).
To do this, you need the admin account credentials.
With those, get a token from the API:

.. code-block:: sh

   curl -u 'admin:$PASSWORD' https://docs-api.ipac.caltech.edu/token

Use the content of the ``token`` response field as the username with blank password to authenticate with the API.
To register the documentation, customize the following API request:

.. code-block:: sh

   curl -u '$TOKEN:' -X POST --json '{
       "slug": "spherex-sphinx",
       "title": "SPHEREx Sphinx",
       "source_repo_url": "https://github.com/SPHEREx/spherex-sphinx",
      }' https://docs-api.ipac.caltech.edu/v2/org/spherex/projects

.. _getting-started-gh-actions:

Build and upload the documentation in GitHub Actions CI
=======================================================

Use a GitHub Actions workflow to build and upload documentation as part of your project's CI and release processes.
When uploading through GitHub Actions, the ``ltd`` CLI tool automatically knows the branch or tag associated with the documentation build.

To introspect your project to build an API reference, Sphinx builds documentation in the same Python environment as the installed project.
Therefore you can either add the documentation build to the same GitHub Actions workflow job that tests the project, or replicate the setup steps from the testing job into a separate documentation job.
When your software is installed, ensure that it's installed with the ``[docs]`` extra to include the documentation dependencies.

These workflow steps are an example of how to build and upload documentation in GitHub Actions, assuming that the project is already checked out and installed:

.. code-block:: yaml
   :caption: .github/workflows/docs.yaml

   # For rendering class inheritance diagrams
   - name: Install graphviz
     run: |
       sudo apt-get install graphviz

   - name: Build documentation
     run: |
       cd docs
       make html

   - name: Install LTD Conveyor
     run: |
       python -m pip install ltd-conveyor==0.9.0a2

   - name: Upload documentation
     if: github.event_name == 'push' || github.event_name == 'workflow_dispatch'
     env:
       LTD_PASSWORD: ${{ secrets.SPHEREX_DOCS_API_PASSWORD }}
       LTD_USERNAME: spherex-upload
       DOCNAME: example # UPDATE to match the registered "slug"
     run: |
       ltd --host https://docs-api.ipac.caltech.edu upload \
         --org spherex --project ${{ env.DOCNAME }} --gh \
         --dir docs/_build/html
