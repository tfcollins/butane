#!/usr/bin/env python

"""Tests for `butane` package."""

import pytest

# from click.testing import CliRunner

# from butane import butane
# from butane import cli
import butane

# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'butane.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output

def test_daq2_config():
    # RX
    j = butane.jesd()
    j.L = 4
    j.M = 2
    j.S = 1
    j.N = 16
    j.Np = 16

    print(j.conversion_clock)
