# This file is placed in the Public Domain.


"command tests"


import inspect
import random
import unittest


from gcid.obj.dbs import Class, Config
from gcid.obj.fnc import format
from gcid.run.cbs import Callbacks
from gcid.run.cmd import Commands, Command, dispatch
from gcid.run.hdl import Handler
from gcid.run.prs import parse
from gcid.run.tbl import Table
from gcid.run.thr import launch


from gcid.obj import Object, get, keys, values


events = []


param = Object()
param.commands = [""]
param.config = ["nick=opbot", "server=localhost", "port=6699"]
param.display = ["reddit title,summary,link", ""]
param.fetch = [""]
param.find = ["log", "log txt==test", "rss", "rss rss==reddit", "config server==localhost"]
param.fleet = ["0", ""]
param.log = ["test1", "test2"]
param.meet = ["root@shell", "test@user"]
param.more = [""]
param.nick = ["dfly", "dflybot", "dfly_"]
param.password = ["bart blabla"]
param.rss = ["https://www.reddit.com/r/python/.rss"]
param.todo = ["things todo"]


def getmain(name):
    main =  __import__("__main__")
    return getattr(main, name, None)

         
c = getmain("c")
c.threaded = True
c.start()


def consume(events):
    fixed = []
    res = []
    for e in events:
        e.wait()
        fixed.append(e)
    for f in fixed:
        try:
            events.remove(f)
        except ValueError:
            continue
    return res


class Test_Commands(unittest.TestCase):


    def test_commands(self):
        cmds = sorted(Commands.cmd)
        random.shuffle(cmds)
        for cmd in cmds:
            for ex in get(param, cmd, [""]):
                e = Command()
                e.txt = cmd + " " + ex
                e.orig = repr(c)
                c.put(e)
                events.append(e)
        consume(events)
        self.assertTrue(not events)
