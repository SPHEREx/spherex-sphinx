"""Sphinx configuration for SPHEREx technotes."""

from contextlib import suppress
from pathlib import Path

from technote.sphinxconf import *  # noqa: F401 F403

with suppress(ValueError):
    # Remove the sphinxcontrib-bibtex extension so that we can add it back
    # in the proper order relative to documenteer.ext.githubbibcache.
    extensions.remove("sphinxcontrib.bibtex")  # noqa: F405

extensions.extend(  # noqa: F405
    [
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
]

# Configurations for the technote theme.
html_theme_options = {
    "light_logo": "spherex-logo-color-light.png",
    "dark_logo": "spherex-logo-color-dark.png",
    "logo_link_url": "https://spherex-docs.ipac.caltech.edu",
    "logo_alt_text": "SPHEREx",
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
