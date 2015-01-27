# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals, print_function

from astropy.extern import six

import numpy as np

from ...asdftypes import AsdfType


class ComplexType(AsdfType):
    name = 'core/complex'
    types = [complex, np.complex, np.cfloat, np.cdouble, np.clongdouble]

    @classmethod
    def to_tree(cls, node, ctx):
        return six.text_type(node)

    @classmethod
    def from_tree(cls, tree, ctx):
        tree = tree.replace(
            'inf', 'INF').replace(
            'i', 'j').replace(
            'INF', 'inf').replace(
            'I', 'J')
        return complex(tree)
