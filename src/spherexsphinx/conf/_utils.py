"""Utilities for Sphinx configuration."""

from __future__ import annotations

import sys
from collections.abc import MutableMapping
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

from git import Repo
from pydantic import BaseModel, Field, HttpUrl, ValidationError
from sphinx.errors import ConfigError

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib

__all__ = [
    "get_asset_path",
    "SpherexConfig",
    "ConfigRoot",
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
    pathlib.Path
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
            "Name of the project, used as titles throughout the "
            "documentation site."
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
            intersphinx_mapping[project] = (str(url), None)

    def extend_sphinx_extensions(self, extensions: List[str]) -> None:
        """Append additional sphinx extensions from sphinx.extensions to
        the existing default extensions list.

        Parameters
        ----------
        extensions
            List of base Sphinx extensions to append to.
        """
        extensions.extend(self.config.sphinx.extensions)

    def set_edit_on_github(
        self,
        html_theme_options: MutableMapping[str, Any],
        html_context: MutableMapping[str, Any],
    ) -> None:
        """Configures the Edit on GitHub functionality, if possible."""
        if self.github_url is None:
            raise ConfigError("project.github_url is not set.")

        parsed_url = urlparse(self.github_url)
        path_parts = parsed_url.path.split("/")
        try:
            # first part is "/"
            github_owner = path_parts[1]
            github_repo = path_parts[2].split(".")[0]  # drop .git if present
        except IndexError:
            raise ConfigError(
                f"Could not parse GitHub repo URL: {self.github_url}"
            )

        repo = GitRepository(Path.cwd())
        try:
            # the current working directory for sphinx config is always
            # the same as the directory containing the conf.py file.
            doc_dir = str(Path.cwd().relative_to(repo.working_tree_dir))
        except ValueError:
            raise ConfigError(
                "Cannot determine the path of the documentation directory "
                "relative to the Git repository root."
            )

        html_theme_options["use_edit_page_button"] = True
        html_context["github_user"] = github_owner
        html_context["github_repo"] = github_repo
        html_context[
            "github_version"
        ] = self.config.project.github_default_branch
        html_context["doc_path"] = doc_dir

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
            config = ConfigRoot.model_validate(tomllib.loads(toml_content))
        except ValidationError as e:
            message = (
                f"Syntax or validation issue in spherex.toml:\n\n" f"{str(e)}"
            )
            raise ConfigError(message)
        return cls(config=config)


class GitRepository:
    """Access to to metadata about the Git repository of the documentation
    project.
    """

    def __init__(self, dirname: Path) -> None:
        self._repo = Repo(dirname, search_parent_directories=True)

    @property
    def working_tree_dir(self) -> Path:
        """The root directory of the Git repository."""
        path = self._repo.working_tree_dir
        if path is None:
            raise RuntimeError("Git repository is not available.")
        return Path(path)
