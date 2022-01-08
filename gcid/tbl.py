# This file is placed in the Public Domain.


"OTP-CR-117/19"


import _thread


from .fnc import register
from .obj import Object, get
from .utl import locked


cmdlock = _thread.allocate_lock()


class Cbs(Object):

    cbs = Object()

    @staticmethod
    def add(k, v):
        Cbs.cbs[str(k)] = v

    @staticmethod
    def get(typ):
        return get(Cbs.cbs, typ)

    @staticmethod
    def dispatch(event):
        if event and event.type in Cbs.cbs:
            Cbs.cbs[event.type](event)


class Cls(Object):

    cls = Object()

    @staticmethod
    def add(clz):
        register(Cls.cls, "%s.%s" % (clz.__module__, clz.__name__), clz)

    @staticmethod
    def full(name):
        name = name.lower()
        res = []
        for cln in Cls.cls:
            if cln.split(".")[-1].lower() == name:
                res.append(cln)
        return res

    @staticmethod
    def get(nm):
        return get(Cls.cls, nm)


class Cmd(Object):

    cmds = Object()

    @staticmethod
    def add(cmd):
        register(Cmd.cmds, cmd.__name__, cmd)

    @staticmethod
    def dispatch(e):
        e.parse()
        f = Cmd.get(e.cmd)
        if f:
            f(e)
            e.show()
        e.ready()

    @staticmethod
    def handle(e):
        try:
            Cmd.dispatch(e)
        except Exception as ex:
            e.errors.append(ex)
            e.ready()

    @staticmethod
    def get(cmd):
        return get(Cmd.cmds, cmd)


class Dpt(Object):

    cbs = Object()

    @staticmethod
    def add(cb):
        register(Dpt.cbs, cb.__name__, cb)

    @staticmethod
    @locked(cmdlock)
    def handle(clt, e):
        e.parse()
        cb = Dpt.get(e.type)
        if cb:
            cb(clt, e)
            e.show()
        e.ready()

    @staticmethod
    def get(cmd):
        return get(Dpt.cmds, cmd)


class Tbl(Object):

    mod = Object()

    @staticmethod
    def add(o):
        Tbl.mod[o.__name__] = o

    @staticmethod
    def get(nm):
        return get(Tbl.mod, nm, None)
