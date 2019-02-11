# -*- coding: utf-8 -*-

"""Main module."""

from bs4 import BeautifulSoup

def fun(x):
    """
    A Subpoint
    ----------
    This is my idea.

    A subsubpoint
    +++++++++++++
    This is a smaller idea.

    COMPLEX TABLE:
    +------------+------------+-----------+
    | Header 1   | Header 2   | Header 3  |
    +============+============+===========+
    | body row 1 | column 2   | column 3  |
    +------------+------------+-----------+
    | body row 2 | Cells may span columns.|
    +------------+------------+-----------+
    | body row 3 | Cells may  | - Cells   |
    +------------+ span rows. | - contain |
    | body row 4 |            | - blocks. |
    +------------+------------+-----------+
    """
    return 'GitHub' in BeautifulSoup(x).title.string
