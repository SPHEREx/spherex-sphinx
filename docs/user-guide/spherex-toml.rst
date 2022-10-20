######################
spherex.toml reference
######################

spherex-sphinx uses a custom file, called :file:`spherex.toml` located alongside the standard Sphinx :file:`conf.py` file, to maintain project configurations.
This file enables you to set configurations without knowing the details of how the :doc:`base Sphinx configuration <base-config>` for SPHEREx documentation projects is set up.
This page describes the syntax for :file:`spherex.toml` file.

[project]
=========

project.title
-------------

The name of the project.

.. code-block:: toml

   [project]
   title = "spherex-sphinx"

project.copyright
-----------------

The project's copyright statement.

.. code-block:: toml

   [project]
   copyright = "2022 California Institute of Technology"

project.base_url
----------------

The root URL of the project.
This URL is used for building the "canonical" link relation header tags.

.. code-block:: toml

   [project]
   base_url = "https://spherex-docs.ipac.caltech.edu/spherex-sphinx/"

project.github_url
------------------

The URL of the project's GitHub repository.
This URL is used for adding "Edit this page" links to the sidebar of each page.

.. code-block:: toml

   [project]
   github_url = "https://github.com/SPHEREx/spherex-sphinx"

[sphinx]
========

sphinx.extensions
-----------------

A list of `Sphinx extensions <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`__ to use in the project, *in addition* to the base extensions included in :doc:`spherexsphinx.conf.base <base-config>`.

.. code-block:: toml

   [sphinx]
   extensions = [
       "sphinxcontrib.bibtex"
   ]

Note that you will need to include additional extension packages in your project's Python dependencies.
You may also need to configure the additional extensions in your project's :file:`conf.py` file.

[sphinx.intersphinx.projects]
=============================

`Intersphinx <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`__ is a Sphinx extension for linking to items — like Python classes, functions, or ``ref`` targets — in other Sphinx documentation projects.
Sphinx is used by most projects in the scientific Python ecosystem, including Astropy, Numpy, Scipy, and Python itself.
In this configuration, set reference name to the key, and the value is to the root URL of the project.

.. code-block:: toml

   [sphinx.intersphinx.projects]
   python = "https://docs.python.org/3"
   astropy = "https://docs.astropy.org/en/stable/"
