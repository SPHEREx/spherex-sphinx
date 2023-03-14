"""Test the crossref extension."""

from __future__ import annotations

from pathlib import Path
from typing import IO

import pytest
from bs4 import BeautifulSoup
from sphinx.application import Sphinx
from sphinx.util import logging


@pytest.mark.sphinx("html", testroot="crossref")
def test_example_page_rendering(app: Sphinx, status: IO, warning: IO) -> None:
    """Test against the ``test-crossref`` test root."""
    app.verbosity = 2
    logging.setup(app, status, warning)
    app.builder.build_all()

    index_path = Path(app.outdir) / "index.html"
    html_source = index_path.read_text()
    soup = BeautifulSoup(html_source, "lxml")

    # Simple link
    simple_section = soup.find(id="simple")
    simple_link = simple_section.select("a.external")[0]
    assert (
        simple_link["href"]
        == "https://spherex-docs.ipac.caltech.edu/ssdc-ms-001"
    )
    assert simple_link.text == "SSDC-MS-001"

    # Custom display
    custom_section = soup.find(id="custom-display")
    custom_link = custom_section.select("a.external")[0]
    assert (
        custom_link["href"]
        == "https://spherex-docs.ipac.caltech.edu/ssdc-ms-002"
    )
    assert custom_link.text == "Assemble Raw Data"
