#credits to userge

import os, urllib, requests, asyncio

from . import *

@bot.on(x_cmd("boobs$"))
@bot.on(sudo_cmd(pattern="boobs$", allow_sudo=True))
async def boobs(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Finding some big boobs for u 🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some big boobs🤪")
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()

@bot.on(x_cmd("butts$"))
@bot.on(sudo_cmd(pattern="butts$", allow_sudo=True))
async def butts(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("Finding some beautiful butts for u🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some beautiful butts🤪")
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()

CmdHelp("adult zone").add_command(
  "boobs or buttst", "Send Beautiful Butts/Boobs"
).add_info(
  "18+ Only"
).add_warning(
  "✅ 18+ NSFW."
).add()
