from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

hell_pic = Config.ALIVE_PIC or "https://telegra.ph/file/cc64741c316f3d720b998.jpg"
alive_c = f"__**🔥🔥 χ-υѕєявσт 🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {xl_mention} 』\n\n"
alive_c += f"•♦• Telethon     :  `{tel_ver}` \n"
alive_c += f"•♦• χ-υѕєявσт       :  __**{x_ver}**__\n"
alive_c += f"•♦• Sudo            :  `{is_sudo}`\n"
alive_c += f"•♦• Channel      :  {x_channel}\n"

#-------------------------------------------------------------------------------

@bot.on(hell_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(hell):
    if hell.fwd_from:
        return
    await x.get_chat()
    await x.delete()
    await bot.send_file(hell.chat_id, hell_pic, caption=alive_c)
    await x.delete()

msg = f"""
**⚡ χ-υѕєявσт ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**Hêllẞø†  :**  **{hell_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(x_cmd(pattern="xbot$"))
@bot.on(sudo_cmd(pattern="xbot$", allow_sudo=True))
async def x_a(event):
    try:
       x = await bot.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "xbot", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
