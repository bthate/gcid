# This file is placed in the Public Domain.


import gcid.basic as basic
import gcid.model as model
import gcid.irc as irc
import gcid.rss as rss


from gcid.handler import Table


Table.add(basic)
Table.add(model)
Table.add(irc)
Table.add(rss)
