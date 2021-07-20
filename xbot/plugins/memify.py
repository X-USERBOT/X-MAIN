import cv2
import os
import io
import random
import shutil
import re
import textwrap
import lottie

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

from . import *


path = "./xmify/"
if not os.path.isdir(path):
    os.makedirs(path)


@bot.on(x_cmd(pattern="mmf ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mmf ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(event, "You need to reply to an image with .mmf` 'text on top' ; 'text on bottom'")
        return
    await eor(event, "🤪 **Memifying...**")
    reply = await event.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs) 
    tal, semx = img.read()
    cv2.imwrite("xbot.webp", semx)
    text = event.pattern_match.group(1)
    webp_file = await draw_meme_text("xbot.webp", text)
    await event.client.send_file(
        event.chat_id, webp_file, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    shutil.rmtree(path)
    os.remove("xbot.webp")
    os.remove(webp_file)


@bot.on(x_cmd(pattern="mms ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mms ?(.*)", allow_sudo=True))
async def sed(xboy):
    if xboy.fwd_from:
        return
    if not xboy.reply_to_msg_id:
        await eod(xboy, "You need to reply to an image with .mms` 'text on top' ; 'text on bottom'")
        return
    await eor(xboy, "🤪 **Memifying...**")
    reply = await xboy.get_reply_message()
    imgs = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(imgs) 
    tal, semx = img.read()
    cv2.imwrite("xbot.webp", semx)
    text = xboy.pattern_match.group(1)
    photo = await draw_meme("xbot.webp", text)
    await xboy.client.send_file(
        xboy.chat_id, photo, reply_to=xboy.reply_to_msg_id
    )
    await xboy.delete()
    shutil.rmtree(path)
    os.remove("xbot.webp")
    os.remove(photo)
    
@bot.on(x_cmd(pattern="doge(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="doge(?: |$)(.*)", allow_sudo=True))
async def nope(xbot):
    x = xbot.pattern_match.group(1)
    if not x:
        if xbot.is_reply:
            (await xbot.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(xbot, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(xbot, "Doge need some text to make sticker.")

    troll = await bot.inline_query("DogeStickerBot", f"{(deEmojify(x))}")
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
     await eod(xbot, "Error 404:  Not Found")


@bot.on(x_cmd(pattern="gg(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="gg(?: |$)(.*)", allow_sudo=True))
async def nope(xbot):
    x = xbot.pattern_match.group(1)
    if not x:
        if xbot.is_reply:
            (await xbot.get_reply_message()).message
        else:
            if Config.ABUSE == "ON":
                return await eor(xbot, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(xbot, "Doge need some text to make sticker.")

    troll = await bot.inline_query("GooglaxBot", f"{(deEmojify(x))}")
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
     await eod(xbot, "Error 404:  Not Found")

    
CmdHelp("memify").add_command(
  "mmf", "<reply to a img/stcr/gif> <upper text> ; <lower text>", "Memifies the replied image/gif/sticker with your text and sends output in sticker format.", "mmf <reply to a img/stcr/gif> hii ; hello"
).add_command(
  "mms", "<reply to a img/stcr/gif> <upper text> ; <lower text>", "Memifies the replied image/gif/sticker with your text and sends output in image format.", "mms <reply to a img/stcr/gif> hii ; hello"
).add_command(
  "doge", "<text>", "Makes A Sticker of Doge with given text."
).add_command(
  "gg", "<text>", "Makes google search sticker."
).add_info(
  "Make Memes on telegram 😉"
).add_warning(
  "✅ Harmless Module."
).add()
