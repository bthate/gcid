# This file is placed in the Public Domain.


"OTP-CR-117/19"


import os
import unittest


from gcd.obj import Object, keys, values
from gcd.tbl import Tbl


import gcdm.bsc


Tbl.add(gcdm.bsc)


class Test_Table(unittest.TestCase):

    def test_mod(self):
        self.assertTrue("gcdm.bsc" in keys(Tbl.mod))
