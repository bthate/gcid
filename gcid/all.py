# This file is placed in the Public Domain.


import gcid.bsc as bsc
import gcid.mdl as mdl
import gcid.irc as irc
import gcid.rss as rss


from .hdl import Table


Table.add(bsc)
Table.add(mdl)
Table.add(irc)
Table.add(rss)
