###########################
Writing numpydoc docstrings
###########################

SPHEREx's Python codebase uses `numpydoc`_\ -formatted docstrings.
These docstrings use reStructuredText and are structured so that Sphinx tooling can automatically generate an API reference from them.

To learn about the `numpydoc`_ format, see the `numpydoc style guide documentation`_.

Using type annotations with docstrings
======================================

The original `numpydoc`_ format expresses type annotation information in the ``Parameters`` and ``Returns`` sections of the docstring.
With Python type annotations, type information for parameters no longer needs to be included with each parameter description.
The return still needs to include type information though.

Here is an example of a function with type annotations:
An example of a function using type annotations:

.. code-block:: python

    def add(a: int, b: int) -> int:
        """Add two numbers.

        Parameters
        ----------
        a
            The first number to add.
        b
            The second number to add.

        Returns
        -------
        int
            The sum of the two numbers.
        """
        return a + b

Notice how the ``a`` and ``b`` parameters do not include type information in the docstring; the generated API reference will use the type from the annotations instead.
However the ``Returns`` section still needs to include the return type as the key.
If the type description is *only* a type, you don't need to wrap the type in backticks as a link — it will automatically be formatted as an API link.
However, for more complex types, you will need to use backticks to create links to individual types:

.. code-block:: text

   Returns
   -------
   `int` or `float`
       The result.
