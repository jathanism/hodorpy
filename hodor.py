#!/usr/bin/env python

"""
Hodor.
"""

import sys
sys.tracebacklimit = 0  # python 2.7

__version__ = 'Hodor.'
__author__ = 'Hodor.'
__copyright__ = 'Hodor.'


class HodorError(RuntimeError):
    """
    In case when Hodor meets another Hodor
    """

# Hodor.
HODOR = 'Hodor.'


class Hodor(object):
    """
    Hodor.

    :param hodor:
        Hodor.
    """
    def __init__(self, hodor=HODOR):
        self._hodor = hodor

    def hodor(self):
        hodor = self._hodor
        return hodor

    def hodor_hodor(self):
        return self.hodor_hodor()

    def __call__(self):
        hodor = self.hodor()
        return hodor

    def __str__(self):
        return self.hodor()


hodor = Hodor(HODOR)


if __name__ == '__main__':
    print(hodor.hodor())

    try:
        print(hodor.hodor_hodor())
    except RuntimeError as e:
        raise HodorError(e.message.replace('recursion', 'hodor'))
