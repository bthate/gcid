# This file is placed in the Public Domain.


"OTP-CR-117/19"


def __dir__():
    return (
        "cfg",
        "cmd",
        "dbs",
        "evt",
        "flt",
        "fnc",
        "fnd",
        "irc",
        "jsn",
        "krn",
        "log",
        "opt",
        "prs",
        "req",
        "rss",
        "rpt",
        "tbl",
        "tdo",
        "thr",
        "tmr",
        "udp",
        "usr",
        "wsd"
    )


from gcid.tbl import Tbl


from gcid import cfg
from gcid import cmd
from gcid import dbs
from gcid import evt
from gcid import flt
from gcid import fnc
from gcid import jsn
from gcid import krn
from gcid import opt
from gcid import prs
from gcid import rpt
from gcid import tbl
from gcid import thr
from gcid import tmr

from gcid import fnd
from gcid import irc
from gcid import log
from gcid import opt
from gcid import req
from gcid import rss
from gcid import sta
from gcid import tdo
from gcid import udp
from gcid import usr
from gcid import wsd


for mn in __dir__():
    md = getattr(locals(), mn, None)
    if md:
        Tbl.add(md)
