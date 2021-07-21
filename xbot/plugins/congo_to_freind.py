import random

from xbot import CMD_HELP
from xbot.utils import x_cmd

from . import *


RUNSREACTS = [
    "`Aur Bata Bsdk Kar Liya Tunee Party De Chal!`",
    "`Chal Gand Phad Dunga Udd Mat Abb And Congo`",
    "`Oo Wow Mere Beta Sikh Gaya! Congo`",
    "`Chall Badhiya Congo`",
    "`Fuck You And Congo.`",
    "`Mere Ladke Lavde te lashan Akhir  Karliya Tune.`",
    "`Very Good.`",
    "`Veryy Good Nhi Bulanga Bass Tu Chutiya Hai!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]


@bot.on(x_cmd(pattern=r"chalbsdk ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"chalbsdk  ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(RUNSREACTS) - 1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


CmdHelp("chalbsdk").add_command(
  "chalbsdk", "Gives A Congratulations To Freind"
).add_info(
  "Congratulations To Freind"
).add_warning(
  "✅ Harmless Module (But If Freind Hates Gali Them Don't Do This)."
).add()
