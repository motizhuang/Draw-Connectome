#!/usr/bin/env python

"""Tests for `draw_connectome1` package."""


import unittest
from click.testing import CliRunner

from draw_connectome1 import draw_connectome1
from draw_connectome1 import cli


class TestDraw_connectome1(unittest.TestCase):
    """Tests for `draw_connectome1` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'draw_connectome1.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
