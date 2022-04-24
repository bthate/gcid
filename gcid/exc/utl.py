# This file is placed in the Public Domain.


import os
import sys
import time


from run.cbs import Callbacks


def __dir__():
    return (
        "cprint",
        "init",
        "wait"
    )

def cprint(*args):
    print(*args)
    sys.stdout.flush()


def init(mod):
    try:
        mod.init()
    except Exception as ex:
        Callbacks.errors.append(ex)


def wait():
    while 1:
        time.sleep(1.0)
