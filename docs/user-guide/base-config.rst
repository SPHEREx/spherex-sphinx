#########################
Base Sphinx configuration
#########################

spherex-sphinx's `spherexsphinx.conf.base` module provides a base configuration for SPHEREx's Sphinx_ projects, and uses :doc:`spherex.toml <spherex-toml>` files to customize that configuration on a per-project basis.
Your project uses this base configuration by importing it into the :file:`conf.py` file, as described in :doc:`getting-started`.

This page shows the base configuration for reference, and to aid in extending the configuration in your project's :file:`conf.py` file if necessary.

.. literalinclude:: ../../src/spherexsphinx/conf/base.py
   :language: py
   :caption: spherexsphinx.conf.base
