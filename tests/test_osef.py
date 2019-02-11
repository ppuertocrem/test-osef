#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `osef` package."""

import pytest


from osef import osef


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import requests
    return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    assert osef.fun(response.content)
