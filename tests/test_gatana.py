"""Smoke tests for the gatana package."""

from __future__ import annotations

import gatana


def test_version_is_string() -> None:
    """Package exposes a version string."""
    assert isinstance(gatana.__version__, str)


def test_version_not_empty() -> None:
    """Version string is not empty."""
    assert len(gatana.__version__) > 0
