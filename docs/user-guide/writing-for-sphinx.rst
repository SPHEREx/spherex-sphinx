##################
Writing for Sphinx
##################

SPHEREx uses Sphinx_ to generate documentation sites.
Sphinx_ primarily uses the reStructuredText markup language, although a variant of Markdown is also supported.

Resources for learning reStructuredText
=======================================

- `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__, from Sphinx.
- `Cross referencing syntax <https://www.sphinx-doc.org/en/master/usage/referencing.html>`__, from Sphinx.
- `API links with Sphinx domains <https://www.sphinx-doc.org/en/master/usage/domains/index.html>`__, from Sphinx.
   Note that in SPHEREx documentation, the `default role <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-default_role>`__ (text inside single backticks) is automatically treated as using the ``:py:obj:`` domain for linking to a Python API.
- The Rubin Observatory has a `ReStructuredText style guide <https://developer.lsst.io/restructuredtext/style.html>`_ that summarizes common reStructuredText syntax.

Documentation for extensions
============================

The spherex-sphinx :doc:`base configuration <base-config>` brings in a number of extensions that provide custom reStructuredText roles and directives.

Internal extensions
-------------------

spherex-sphinx provides some custom roles and directives that provide specific functionality for SPHEREx documentation.

- :doc:`crossref` provides roles for referencing other SPHEREx documentation.

Third-party extensions
----------------------

- `sphinx-automodapi`_ provides the ``automodapi`` directive, which generates API documentation pages for all public APIs in a given Python module.
- `sphinxcontrib.mermaid`_ provides the ``mermaid`` directive, which renders `Mermaid.js`_ diagrams as code.
- `Intersphinx`_ provides ways of linking to other Sphinx sites, including their Python API documentation.
- `sphinx_design`_ provides tools for creating sophisticated layouts, including tabs, accordions, card grids, buttons, and badges.
