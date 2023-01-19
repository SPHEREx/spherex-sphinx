"""Test the package version."""

from __future__ import annotations

from spherexsphinx import __version__


def test_version() -> None:
    """Ensure that the version is set."""
    assert isinstance(__version__, str)
    # indicates the package is not installed otherwise
    assert __version__ != "0.0.0"
