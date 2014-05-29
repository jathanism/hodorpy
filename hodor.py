#!/usr/bin/env python

"""
Hodor.
"""

__version__ = 'Hodor.'
__author__ = 'Hodor.'
__copyright__ = 'Hodor.'


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

    def __call__(self):
        hodor = self.hodor()
        return hodor
hodor = Hodor(HODOR)


if __name__ == '__main__':
    print(hodor.hodor())
