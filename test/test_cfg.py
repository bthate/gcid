# This file is placed in the Public Domain.


"config"


import unittest


from gcid.obj.fnc import edit
from gcid.run.prs import parse

from gcid.obj import Object, update

class Config(Object):

    pass

class Test_Cfg(unittest.TestCase):

    def test_parse(self):
        p = Config()
        parse(p, "mod=irc")
        self.assertEqual(p.prs.sets.mod, "irc")

    def test_parse2(self):
        p = Config()
        parse(p, "mod=irc,rss")
        self.assertEqual(p.prs.sets.mod, "irc,rss")

    def test_edit(self):
        d = Object()
        update(d, {"mod": "irc,rss"})
        edit(Config, d)
        self.assertEqual(Config.mod, "irc,rss")
