# This file is placed in the Public Domain.


import getpass
import os
import pwd
import sys
import termios
import time
import traceback


from gcid.obj import values
from gcid.tbl import Cls, Cmd, Tbl


def daemon():
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    os.umask(0)
    si = open("/dev/null", 'r')
    so = open("/dev/null", 'a+')
    se = open("/dev/null", 'a+')
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())


def privileges(name=None):
    if os.getuid() != 0:
        return
    if name is None:
        try:
            name = getpass.getuser()
        except KeyError:
            pass
    try:
        pwnam = pwd.getpwnam(name)
    except KeyError:
        return False
    os.setgroups([])
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)
    os.umask(0o22)
    return True


def root():
    if os.geteuid() != 0:
        return False
    return True


def watcher(clt, quit=False):
    done = []
    while 1:
        time.sleep(1.0)
        for ex in clt.errors:
            if ex.reason not in done:
                done.append(ex.reason)
                print("\n")
                traceback.print_exception(type(ex), ex, ex.__traceback__)
                if quit:
                    break
        if quit:
            break


def wrap(func):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
