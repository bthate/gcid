# This file is placed in the Public Domain.


"config tests"


import os
import sys


sys.path.insert(0, os.getcwd())


import unittest


from gcid.obj.dbs import Config
from gcid.run.prs import parse


from gcid.obj import Object, update

class Test_Config(unittest.TestCase):

    def test_parse(self):
        p = Config()
        parse(p, "mod=irc")
        self.assertEqual(p.mod, "irc")

    def test_parse2(self):
        p = Config()
        parse(p, "mod=irc,rss")
        self.assertEqual(p.mod, "irc,rss")
