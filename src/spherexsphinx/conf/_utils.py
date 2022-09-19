"""Utilities for Sphinx configuration."""

from __future__ import annotations

from pathlib import Path

from sphinx.errors import ConfigError


def get_asset_path(name: str) -> str:
    """Get the absolute path to a file in ``assets`` for use with Sphinx's
    ``html_static_path``.
    """
    path = Path(__file__).parent.joinpath("../assets", name)
    path.resolve()
    if not path.exists():
        raise ConfigError(
            f"Asset {name!r} does not exist.\n"
            f"Tried to resolve to {path} inside the installed "
            "spherexsphinx package."
        )
    return str(path)
