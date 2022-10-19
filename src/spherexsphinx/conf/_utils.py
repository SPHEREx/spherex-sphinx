"""Utilities for Sphinx configuration."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from pydantic import BaseModel, Field, HttpUrl, ValidationError
from sphinx.errors import ConfigError

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib

__all__ = [
    "get_asset_path",
    "SpherexConfig",
]


def get_asset_path(name: str) -> str:
    """Get the absolute path to a file in ``assets`` for use with Sphinx's
    ``html_static_path``.

    Parameters
    ----------
    name
        The name of an asset file in the ``assets`` directory.

    Returns
    -------
    path
        Path to the asset file.
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


class ProjectModel(BaseModel):
    """Model for the project table in the spherex.toml configuration file,
    dealing with overall project metadata.
    """

    title: str = Field(
        description=(
            "Name of the project, used as titles throughout the documentation "
            "site."
        )
    )

    base_url: Optional[HttpUrl] = Field(
        description="Canonical URL of the site's root page."
    )

    copyright: str = Field(
        description="Copyright statement, without a 'copyright' prefix word.",
        default_factory=(
            lambda: f"{datetime.now().year} California Institute of Technology"
        ),
    )

    github_url: Optional[HttpUrl] = Field(
        description="The URL of the project's GitHub repository."
    )

    github_default_branch: str = Field(
        "main",
        description="The project's default development branch on GitHub.",
    )

    version: str = Field("latest", description="Version string.")


class IntersphinxModel(BaseModel):
    """Model for the sphinx.intersphinx table in spherex.toml."""

    projects: Dict[str, HttpUrl] = Field(
        description=(
            "URLs of projects to add to the intersphinx configuration."
        ),
        default_factory=dict,
    )


class SphinxModel(BaseModel):
    """Model for the sphinx table in the spherex.toml configuration file,
    dealing with sphinx configurations.
    """

    intersphinx: IntersphinxModel

    extensions: List[str] = Field(
        description=(
            "Additional Sphinx extensions to use, beyond the base set."
        ),
        default_factory=list,
    )


class ConfigRoot(BaseModel):
    """Root of the spherex.toml configuration file."""

    project: ProjectModel

    sphinx: SphinxModel


@dataclass
class SpherexConfig:
    """Configuration from a spherex.toml configuration file."""

    config: ConfigRoot

    @property
    def base_url(self) -> Optional[str]:
        """The base URL for the project, which can be used as the root
        for each pages canonical url link.
        """
        if self.config.project.base_url is not None:
            return str(self.config.project.base_url)
        else:
            return None

    @property
    def github_url(self) -> Optional[str]:
        """The URL of the project's GitHub repository, if available."""
        if self.config.project.github_url is not None:
            return str(self.config.project.github_url)
        else:
            return None

    def apply_intersphinx_mapping(
        self, intersphinx_mapping: Dict[str, Tuple[str, Optional[str]]]
    ) -> None:
        """Apply the configurations from sphinx.intersphinx.projects to
        the existing mapping.

        Parameters
        ----------
        intersphinx_mapping
            Base intersphinx mapping configuration to extend.
        """
        for project, url in self.config.sphinx.intersphinx.projects.items():
            intersphinx_mapping[project] = (url, None)

    def extend_sphinx_extensions(self, extensions: List[str]) -> None:
        """Append additional sphinx extensions from sphinx.extensions to
        the existing default extensions list.

        Parameters
        ----------
        extensions
            List of base Sphinx extensions to append to.
        """
        extensions.extend(self.config.sphinx.extensions)

    @classmethod
    def load(cls) -> SpherexConfig:
        """Load the spherex.toml file from the current directory.

        When Sphinx executes a conf.py file, the current working directory
        is the root of the documentation project (where conf.py resides).
        """
        path = Path("spherex.toml")
        if not path.is_file():
            raise ConfigError("Cannot find the spherex.toml file.")
        toml_content = path.read_text()
        try:
            config = ConfigRoot.parse_obj(tomllib.loads(toml_content))
        except ValidationError as e:
            message = (
                f"Syntax or validation issue in spherex.toml:\n\n" f"{str(e)}"
            )
            raise ConfigError(message)
        return cls(config=config)
