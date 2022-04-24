# This file is placed in the Public Domain.


"object command"


import base64
import threading
import time


from gcid.obj import Object, get, keys, update


from gcid.obj.dbs import Config, find, last, save
from gcid.obj.fnc import edit, format, register
from gcid.run.bus import Bus
from gcid.run.cmd import Commands
from gcid.run.prs import elapsed, parse
from gcid.run.thr import getname


starttime = time.time()


def __dir__():
    return (
        "cmd",
        "dfg",
        "flt",
        "pwd",
        "thr"
    )


def dfg(event):
    if not event.args:
        event.reply(format(Config))
        return
    edit(Config, event.prs.sets)
    event.reply("ok")


Commands.add(dfg)


def cmd(event):
    event.reply(",".join((sorted(keys(Commands.cmd)))))


Commands.add(cmd)


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(Bus.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(" | ".join([getname(o) for o in Bus.objs]))


Commands.add(flt)


def thr(event):
    result = []
    for t in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(t).startswith("<_"):
            continue
        o = Object()
        update(o, vars(t))
        if get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - starttime)
        result.append((up, t.getName()))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append("%s(%s)" % (txt, elapsed(up)))
    if res:
        event.reply(" ".join(res))


Commands.add(thr)
