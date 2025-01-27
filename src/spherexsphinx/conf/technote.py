"""Sphinx configuration for SPHEREx technotes."""

from pathlib import Path

from technote.sphinxconf import *  # noqa: F401 F403

extensions.extend(  # noqa: F405
    [
        "sphinxcontrib.mermaid",
        "sphinx_prompt",
        "sphinx_design",
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
