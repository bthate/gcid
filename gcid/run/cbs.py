# This file is placed in the Public Domain.


"object callback"


from gcid.obj.fnc import register
from .thr import launch

from gcid.obj import Object, get

def __dir__():
    return (
        "Callbacks",
    )


class Callbacks(Object):

    cbs = Object()
    errors = []
    threaded = True

    @staticmethod
    def add(name, cb):
        register(Callbacks.cbs, name, cb)

    @staticmethod
    def callback(e):
        f = Callbacks.get(e.type)
        if not f:
            e.ready()
            return
        try:
            f(e)
        except Exception as ex:
            Callbacks.errors.append(ex)
            e.exc = ex
            e.ready()

    @staticmethod
    def get(cmd):
        return get(Callbacks.cbs, cmd)


    @staticmethod
    def dispatch(e):
        if Callbacks.threaded:
            e.thrs.append(launch(Callbacks.callback, e, name=e.txt))
            return
        Callbacks.callback(e)
