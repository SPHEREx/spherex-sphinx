"""Sphinx configurations and extensions for SPHEREx."""

__all__ = ["__version__"]

from importlib.metadata import PackageNotFoundError, version

__version__: str
"""The version string of spherex-sphinx"""

try:
    __version__ = version("spherex-sphinx")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"
