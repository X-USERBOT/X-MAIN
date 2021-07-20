import re
from . import *

# Credits to @ForGo10God developer of HellBot.
# This is my first plugin that I made when I released first HellBot.
# Modified to work in groups with inline mode disabled.
# Added error msg if no voice is found.
# So please dont remove credit. 
# You can use it in your repo. But dont remove these lines...

@bot.on(x_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(xbot):
    x = xbot.pattern_match.group(1)
    if not x:
        if xbot.is_reply:
            (await xbot.get_reply_message()).message
        else:
            await edit_or_reply(xbot, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(x))}")
    if troll:
        await xbot.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                xbot.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
    	await eod(xbot, "**Error 404:**  Not Found")
    	
@bot.on(x_cmd(pattern="meev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="meev(?: |$)(.*)", allow_sudo=True))
async def nope(xbot):
    x = xbot.pattern_match.group(1)
    if not x:
        if xbot.is_reply:
            (await xbot.get_reply_message()).message
        else:
            await edit_or_reply(xbot, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("Myinstantsbot", f"{(deEmojify(x))}")
    if troll:
        await xbot.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                xbot.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
    	await eod(xbot, "**Error 404:**  Not Found")


CmdHelp("memevoice").add_command(
	"mev", "<query>", "Searches the given meme and sends audio if found."
).add_command(
	"meev", "<query>", "Same as {hl}mev"
).add_info(
	"Audio Memes."
).add_warning(
	"✅ Harmless Module."
).add()
