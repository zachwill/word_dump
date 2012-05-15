#!/usr/bin/env python

"""
Return two random words.
"""

from random import sample

from simplejson import loads
from termcolor import cprint


def two_random_words():
    """Return two random words."""
    with open('json/words.json') as f:
        data = loads(f.read())
        random = sample(data, 2)
        return " ".join(random)


if __name__ == '__main__':
    output = '\n  %s\n' % two_random_words()
    cprint(output, attrs=['bold'])
