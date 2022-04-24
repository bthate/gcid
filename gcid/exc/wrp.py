# This file is placed in the Public Domain.


import sys
import termios
import time
import traceback


from run.cbs import Callbacks
from exc.dmn import cprint
from exc.utl import wait


def wrap(func):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        cprint("")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        for err in Callbacks.errors:
            traceback.print_exception(type(err), err, err.__traceback__)
