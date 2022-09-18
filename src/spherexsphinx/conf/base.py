"""Base configurations for SPHEREx Sphinx projects.

Use these configurations from your project's Sphinx conf.py file::

    from spherexsphinx.conf.base import *
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

# Core Sphinx configurations =================================================

# General information about the project.
project = "spherex-sphinx"
copyright = "2022 California Institute of Technology"
author = "SPHEREx"

version = "latest"
release = version

language = "en"

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

root_doc = "index"

exclude_patterns = ["_build", "README.rst", "_rst_epilog.rst"]

rst_epilog = Path("_rst_epilog.rst").read_text()

pygments_style = "sphinx"

# The reST default role cross-links Python (used for this markup: `text`)
default_role = "py:obj"

# Extensions =================================================================

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "sphinxcontrib.mermaid",
]

# HTML =======================================================================
# Uses https://pydata-sphinx-theme.readthedocs.io/en/stable/

html_theme = "pydata_sphinx_theme"

# Jinja templating context
html_context: Dict[str, Any] = {
    "github_user": "SPHEREx",
    "github_repo": "spherex-sphinx",
    "github_version": "main",
    "doc_path": "docs",
}

# Optional for the PyData Sphinx Theme
html_theme_options = {
    "logo": {"text": "SPHEREx Sphinx"},
    "use_edit_page_button": True,
    "pygment_light_style": "tango",
    "pygment_dark_style": "github-dark",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/SPHEREx/spherex-sphinx",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        }
    ],
}

html_title = project
html_short_title = project
html_baseurl = "https://spherex-docs.ipac.caltech.edu/spherex-sphinx/"

# Redundant when linking to GitHub
html_show_sourcelink = False
html_copy_source = False

# Intersphinx ================================================================
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

intersphinx_timeout = 10.0  # seconds

intersphinx_cache_limit = 5  # days

# Link check builder =========================================================
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_retries = 2
linkcheck_timeout = 15  # seconds
# Regular expressions of links to skip in the check
linkcheck_ignore: List[str] = []

# Python API reference =======================================================

# Automodapi
# https://sphinx-automodapi.readthedocs.io/en/latest/automodapi.html
automodapi_toctreedirnm = "api"

# sphinx_autodoc_typehints
always_document_param_types = True
typehints_defaults = "comma"

# napoleon
napoleon_google_docstring = False  # non-default
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# MyST Parser for Markdown support ===========================================

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Mermaid diagram support ====================================================
# https://github.com/mgaitan/sphinxcontrib-mermaid
# https://mermaid-js.github.io/mermaid/#/

# Render in browser with "raw" foramt
mermaid_output_format = "raw"
