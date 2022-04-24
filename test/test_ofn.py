# This file is placed in the Public Domain.


"config tests"


import os
import sys


sys.path.insert(0, os.getcwd())


import unittest


from obj import Object, update


from obj.dbs import Config
from obj.fnc import edit


class Test_functions(unittest.TestCase):


    def test_edit(self):
        d = Object()
        update(d, {"mod": "irc,rss"})
        edit(Config, d)
        self.assertEqual(Config.mod, "irc,rss")
