################################
Linking to SPHEREx documentation
################################

The ``spherexsphinx.ext.crossref`` extension provides ways to reference other SPHEREx documentation from a SPHEREx Sphinx documentation project.
This extension is enabled with the :doc:`default configuration <base-config>`.

Linking to other SPHEREx documents
==================================

Use the ``spherexdoc`` role to link to the root URL of other SPHEREx documents.
The simplest usage is to provide the document ID (or the first part of the document's URL path on ``spherex-docs.ipac.caltech.edu``).

.. code-block:: rst

   :spherexdoc:`SSDC-MS-001`

Result: :spherexdoc:`SSDC-MS-001`

You can also customize the link's display text by providing the display text followed by the document's ID in angle brackets:

.. code-block:: rst

   :spherexdoc:`Decompress <ssdc-ms-001>`

Result: :spherexdoc:`Decompress <ssdc-ms-001>`
