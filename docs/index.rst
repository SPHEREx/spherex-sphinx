##############
spherex-sphinx
##############

**Sphinx configurations and extensions for SPHEREx.**

Install spherex-sphinx with ``pip``:

.. code-block:: bash

   pip install git+https://github.com/SPHEREX/spherex-sphinx.git@main

:doc:`Learn how to set up a Sphinx project with these configurations in the User guide. <user-guide/getting-started>`

In your documentation project's :file:`conf.py` Sphinx configuration file, apply the base configuration:

.. code-block:: py
   :caption: conf.py

   from spherexsphinx.conf.base import *

spherex-sphinx is developed on GitHub at https://github.com/SPHEREx/spherex-sphinx.

.. toctree::
   :hidden:

   user-guide/index
   changelog
   dev/index
