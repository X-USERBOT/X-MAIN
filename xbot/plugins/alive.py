from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

x_pic = Config.ALIVE_PIC or "https://telegra.ph/file/cc64741c316f3d720b998.jpg"
alive_c = f"__**🔥🔥 χ-υѕєявσт 🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {x_mention} 』\n\n"
alive_c += f"•♦• Telethon     :  {tel_ver} \n"
alive_c += f"•♦• χ-υѕєявσт       :  {x_ver}\n"
alive_c += f"•♦• Sudo            :  {is_sudo}\n"
alive_c += f"•♦• Channel      :  {x_channel}\n"

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

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))

msg = f"""
⚡ χ-υѕєявσт ⚡
{Config.ALIVE_MSG}
🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅
Telethon :  {tel_ver}
χ-υѕєявσт  :  {x_ver}
Uptime   :  {uptime}
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
  "✅ Harmless Module"
).add()
