# This file is placed in the Public Domain.


"log text"


def __dir__():
    return (
        "Log",
        "log"
    )


from gcid.obj.dbs import Class, save
from gcid.run.cmd import Commands


from gcid.obj import Object

class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


def log(event):
    if not event.rest:
        event.reply("log <txt>")
        return
    o = Log()
    o.txt = event.rest
    save(o)
    event.reply("ok")


Class.add(Log)
Commands.add(log)
