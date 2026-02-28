"""Tests for landing-page."""

import pytest
from landing_page import page


class TestPage:
    """Test suite for page."""

    def test_basic(self):
        """Test basic usage."""
        result = page("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            page("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = page(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
