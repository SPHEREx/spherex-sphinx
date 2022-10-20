"""Test the configuration utilities in spherexsphinx.conf._utils."""

from __future__ import annotations

import pytest
from sphinx.errors import ConfigError

from spherexsphinx.conf._utils import get_asset_path


@pytest.mark.parametrize(
    "name", ["spherex-logo-color-light.png", "spherex-logo-color-dark.png"]
)
def test_get_asset_path(name: str) -> None:
    """Test `get_asset_path` for known static assets."""
    path = get_asset_path(name)
    assert path.endswith(name)


def test_get_asset_path_nonexistant() -> None:
    """Test that `get_asset_path` throws a Sphinx ConfigError for non-existant
    assets.
    """
    with pytest.raises(ConfigError):
        get_asset_path("nonexistant.txt")
