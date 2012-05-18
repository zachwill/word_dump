#!/usr/bin/env python

"""
Return two random words.
"""

from random import sample
from .words import words


def juxtapose():
    """Return two random words."""
    random = sample(words, 2)
    return " ".join(random)
