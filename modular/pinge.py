################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

from datetime import datetime

from pyrogram.raw.functions import Ping

from Mix import *


@ky.ubot("ping", sudo=True)
@ky.devs("mping")
async def ping(c: user, m):
    emo = Emojii(c.me.id)
    emo.initialize()
    start = datetime.now()
    await c.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    _ping = f"""
**{emo.ping} Pong !! `{str(delta_ping).replace('.', ',')}ms`**
**{emo.pong} Mix-Userbot**
**{emo.alive} {c.me.first_name} **"""
    await m.reply(_ping)


@bot.on_message(filters.command("ping"))
async def ping(u, m):
    await m.reply_text("<b> Mix Userbot Tes</b>")
