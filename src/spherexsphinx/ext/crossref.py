"""Cross referencing roles."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Optional

from docutils import nodes

if TYPE_CHECKING:
    from docutils.nodes import Node, system_message
    from docutils.parsers.rst.states import Inliner
    from sphinx.application import Sphinx

__all__ = ["spherexdoc_link_role", "setup"]


def spherexdoc_link_role(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Optional[dict] = None,
    content: Optional[list[str]] = None,
) -> tuple[list[Node], list[system_message]]:
    """Link to a SPHEREx document or project hosted on
    ``spherex-docs.ipac.caltech.edu`` given the project name (first part of
    the URL path).

    Example::

        :spherexdoc:`SSDC-MS-001`
    """
    m = re.search(r"(?P<display>.+)<(?P<reference>.+)>", text)
    if m:
        display_text = m.group("display").strip()
        path = m.group("reference").lower().strip()
    else:
        display_text = text
        path = text.lower().strip()

    if options is None:
        options = {}

    node = nodes.reference(
        text=display_text,
        refuri=f"https://spherex-docs.ipac.caltech.edu/{path}",
        **options,
    )
    return [node], []


def setup(app: Sphinx) -> None:
    """Set up the extensions (Sphinx hook)."""
    app.add_role("spherexdoc", spherexdoc_link_role)
