# -*- coding: utf-8 -*-

"""Main module."""

from bs4 import BeautifulSoup

def fun(x):
    return 'GitHub' in BeautifulSoup(x).title.string
