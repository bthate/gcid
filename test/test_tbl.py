# This file is placed in the Public Domain.


"table"


import inspect
import os
import sys
import unittest


from gcid.run.tbl import Table


from gcid.obj import Object, keys, values

import gcid.obj


Table.add(gcid.obj)


class Test_Table(unittest.TestCase):

    def test_mod(self):
        self.assertTrue("gcid.obj" in Table.mod.keys())
