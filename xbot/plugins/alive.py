from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

x_pic = Config.ALIVE_PIC or "https://telegra.ph/file/cc64741c316f3d720b998.jpg"
alive_c = f"__**đ„đ„ Ï-ÏŃŃŃĐČÏŃ đ„đ„**__\n\n"
alive_c += f"__âŒ ĂwĂ±ĂȘr â__ : ă {x_mention} ă\n\n"
alive_c += f"âąâŠâą Telethon     :  {tel_ver} \n"
alive_c += f"âąâŠâą Ï-ÏŃŃŃĐČÏŃ       :  {x_ver}\n"
alive_c += f"âąâŠâą Sudo            :  {is_sudo}\n"
alive_c += f"âąâŠâą Channel      :  {x_channel}\n"

#-------------------------------------------------------------------------------

@bot.on(x_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(x):
    if x.fwd_from:
        return
    await x.get_chat()
    await x.delete()
    await bot.send_file(x.chat_id, x_pic, caption=alive_c)
    await x.delete()


msg = f"""
âĄ Ï-ÏŃŃŃĐČÏŃ âĄ
{Config.ALIVE_MSG}
đ đ±đđ đđđđđđ đ
Telethon :  {tel_ver}
Ï-ÏŃŃŃĐČÏŃ  :  {x_ver}
Abuse    :  {abuse_m}
Sudo      :  {is_sudo}
"""
botname = Config.BOT_USERNAME

@bot.on(x_cmd(pattern="xbot$"))
@bot.on(sudo_cmd(pattern="xbot$", allow_sudo=True))
async def x(event):
    try:
       x = await bot.inline_query(botname, "alive")
       await x[0].click(event.chat_id)
       if event.sender_id == P_4_PEEYUSH:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "xbot", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "â Harmless Module"
).add()
