"""Base configurations for SPHEREx Sphinx projects.

Use these configurations from your project's Sphinx conf.py file::

    from spherexsphinx.conf.base import *
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from ._utils import SpherexConfig, get_asset_path

c = SpherexConfig.load()

# Core Sphinx configurations =================================================

# General information about the project.
project = c.config.project.title
copyright = c.config.project.copyright
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

epilog_path = Path("_rst_epilog.rst")
if epilog_path.is_file():
    rst_epilog = epilog_path.read_text()

pygments_style = "sphinx"

# The reST default role cross-links Python (used for this markup: `text`)
default_role = "py:obj"

# Ignore unavoidable Sphinx warnings.
# Pydantic cross links aren't possible, so ignore them.
nitpick_ignore_regex = [
    ("py:.*", "pydantic.*"),
]
nitpick_ignore_regex.extend(c.config.sphinx.nitpick_ignore_regex)

nitpick_ignore = [
    ("py:class", "unittest.mock.Base"),
    ("py:class", "unittest.mock.CallableMixin"),
    ("py:class", "pydantic.BaseModel"),
    ("py:class", "BaseModel"),
]
nitpick_ignore.extend(c.config.sphinx.nitpick_ignore)

# Extensions =================================================================

extensions = [
    "sphinxcontrib.jquery",
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
    "spherexsphinx.ext.crossref",
]
c.extend_sphinx_extensions(extensions)

# HTML =======================================================================
# Uses https://pydata-sphinx-theme.readthedocs.io/en/stable/

html_theme = "pydata_sphinx_theme"

# Jinja templating context
html_context: Dict[str, Any] = {}

# Optional for the PyData Sphinx Theme
html_theme_options: Dict[str, Any] = {
    "logo": {
        "text": project,
        "image_light": "spherex-logo-color-light.png",
        "image_dark": "spherex-logo-color-dark.png",
    },
    "use_edit_page_button": True,
    "pygment_light_style": "tango",
    "pygment_dark_style": "github-dark",
    "icon_links": [],
    "favicons": [
        {
            "rel": "icon",
            "sizes": "64x64",
            "href": "spherex-favicon.png",
        }
    ],
}

c.set_edit_on_github(html_theme_options, html_context)

if c.github_url:
    html_theme_options["icon_links"].append(
        {
            "name": "GitHub",
            "url": c.github_url,
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        }
    )

html_title = project
html_short_title = project
if c.base_url:
    html_baseurl = c.base_url

# Redundant when linking to GitHub
html_show_sourcelink = False
html_copy_source = False

# Assets available to the HTML theme from spherexsphinx's "assets" directory
html_static_path = [
    get_asset_path("spherex-logo-color-light.png"),
    get_asset_path("spherex-logo-color-dark.png"),
    get_asset_path("spherex-favicon.png"),
]

# Intersphinx ================================================================
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html

intersphinx_mapping: Dict[str, Tuple[str, Optional[str]]] = {}
c.apply_intersphinx_mapping(intersphinx_mapping)

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
