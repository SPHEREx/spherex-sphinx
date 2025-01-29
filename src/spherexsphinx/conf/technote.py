"""Sphinx configuration for SPHEREx technotes."""

from contextlib import suppress
from pathlib import Path

from technote.sphinxconf import *  # noqa: F401 F403

with suppress(ValueError):
    # Remove the sphinxcontrib-bibtex extension so that we can add it back
    # in the proper order relative to documenteer.ext.githubbibcache.
    extensions.remove("sphinxcontrib.bibtex")  # noqa: F405

with suppress(ValueError):
    # Remove myst-parser if added by technote.sphinxconf so we can
    # add myst-nb.
    extensions.remove("myst_parser")  # noqa: F405

extensions.extend(  # noqa: F405
    [
        "myst_nb",
        "sphinxcontrib.mermaid",
        "sphinx_prompt",
        "sphinx_design",
        "documenteer.ext.githubbibcache",
        "sphinxcontrib.bibtex",
    ]
)

_assets_dir = Path(__file__).parent.joinpath("../assets")

html_static_path: list[str] = [
    str(_assets_dir.joinpath("spherex-logo-color-dark.png").resolve()),
    str(_assets_dir.joinpath("spherex-logo-color-light.png").resolve()),
    str(_assets_dir.joinpath("spherex-technote.css").resolve()),
]

html_css_files = ["spherex-technote.css"]

# A list of paths that contain extra templates (or templates that overwrite
# builtin/theme-specific templates).
_templates_dir = Path(__file__).parent.joinpath("../templates/technote")
templates_path = [str(_templates_dir.resolve())]

# Configurations for the technote theme.
html_theme_options = {
    "light_logo": "spherex-logo-color-light.png",
    "dark_logo": "spherex-logo-color-dark.png",
    "logo_link_url": "https://spherex-docs.ipac.caltech.edu",
    "logo_alt_text": "SPHEREx",
}

# The source file suffixes for .md and .ipynb are automatically managed by
# myst-nb.
source_suffix = {
    ".rst": "restructuredtext",
}

# Configure bibliography with the bib cache
documenteer_bibfile_cache_dir = ".technote/bibfiles"
documenteer_bibfile_github_repos = [
    {
        "repo": "SPHEREx/spherex-tex",
        "ref": "main",
        "bibfiles": [
            "texmf/bibtex/bib/spherex.bib",
        ],
    }
]
# Set up bibtex_bibfiles
# Automatically load local bibfiles in the root directory.
bibtex_bibfiles = [str(p) for p in Path.cwd().glob("*.bib")]

bibtex_reference_style = "author_year"

# Add editions_url to the HTML context so it can be used by the custom
# sidebar template
_id = T.metadata.id  # noqa: F405
if _id is not None:
    html_context["editions_url"] = (  # noqa: F405
        f"https://spherex-docs.ipac.caltech.edu/{_id.lower()}/v/"
    )
