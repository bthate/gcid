# This file is placed in the Public Domain.


"todo items"


import time


from gcid.obj.dbs import Class, find, fntime, save
from gcid.run.prs import elapsed


from gcid.obj import Object


def __dir__():
    return (
        "todo"
    )


class Todo(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


def todo(event):
    if not event.rest:
        nr = 0
        for fn, o in find("todo"):
            event.reply("%s %s %s" % (nr, o.txt, elapsed(time.time() - fntime(fn))))
        return
    o = Todo()
    o.txt = event.rest
    save(o)
    event.reply("ok")


Class.add(Todo)
