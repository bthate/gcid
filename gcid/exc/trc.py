# This file is placed in the Public Domain.


import os
import traceback


from gcid.run.thr import getname


def __dir__():
    return (
        "from_exception",
    )


def from_exception(ex, txt="", sep=" "):
    result = []
    for fr in traceback.extract_tb(ex.__traceback__):
        fnc = str(fr).split()[-1][:-1]
        nme = os.sep.join(fr.filename.split(os.sep)[-2:])
        result.append("%s %s.%s" % (nme, fnc, fr.lineno))
    return "%s -> %s -> %s" % (getname(ex), " -> ".join(result), ex)
