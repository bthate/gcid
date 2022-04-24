# This file is placed in the Public Domain.


"find objects"


import time


from obj.dbs import Db, fntime
from obj.dbs import find
from obj.fnc import format


from run.cmd import Commands
from run.prs import elapsed


def __dir__():
    return (
        "fnd",
    )


def fnd(event):
    if not event.args:
        db = Db()
        res = ",".join(
            sorted({x.split(".")[-1].lower() for x in db.types()}))
        if res:
            event.reply(res)
        else:
            event.reply("no types yet.")
        return
    otype = event.args[0]
    nr = -1
    got = False
    for fn, o in find(otype):
        nr += 1
        txt = "%s %s" % (str(nr), format(o))
        if "t" in event.prs.opts:
            txt = txt + " %s" % (elapsed(time.time() - fntime(fn)))
        got = True
        event.reply(txt)
    if not got:
        event.reply("no result")


Commands.add(fnd)
