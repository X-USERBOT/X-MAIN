from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

from . import *

x_row = Config.BUTTONS_IN_HELP
x_emoji = Config.EMOJI_IN_HELP
x_pic = Config.PMPERMIT_PIC or "https://telegra.ph/file/cc64741c316f3d720b998.jpg"
cstm_pmp = Config.CUSTOM_PMPERMIT
ALV_PIC = Config.ALIVE_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Config.LOGGER_ID
mssge = (
    str(cstm_pmp)
    if cstm_pmp
    else "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
)

USER_BOT_WARN_ZERO = "Enough Of Your Flooding In My Master's PM!! \n\n**๐ซ Blocked and Reported**"

X_FIRST = (
    "**๐ฅ ฯ-ฯัััะฒฯั Prรฎvรฃโ รฉ Sรชรงรผrรฏty Prรธโ รถรงรตl ๐ฅ**\n\nThis is to inform you that "
    "{} is currently unavailable.\nThis is an automated message By X-Userbot.\n\n"
    "{}\n\n**Please Choose Why You Are Here!!**".format(x_mention, mssge))

alive_txt = """
**โ๏ธ โัgัฮทโฮฑัั ฮฑฦ ฯ-ฯัััะฒฯั ฮนั ฯฮทโฮนฮทั โ๏ธ**
{}
**๐ ๐ฑ๐๐ ๐๐๐๐๐๐ ๐**

**Telethon :**  `{}`
**ฯ-ฯัััะฒฯั  :**  **{}**
**Uptime   :**  `{}`
**Abuse    :**  **{}**
**Sudo      :**  **{}**
"""

def button(page, modules):
    Row = x_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{x_emoji} " + pair + f" {x_emoji}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"โ๏ธ Back {x_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"โข โ โข", data="close"
            ),
            custom.Button.inline(
               f"{x_emoji} Next โถ๏ธ", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "xbot_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"๐ฐ **{x_mention}**\n\n๐ __No.of Plugins__ : `{len(CMD_HELP)}` \n๐๏ธ __Commands__ : `{len(apn)}`\n๐๏ธ __Page__ : 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query.startswith("fsub"):
            hunter = event.pattern_match.group(1)
            hell = hunter.split("+")
            user = await bot.get_entity(int(x[0]))
            channel = await bot.get_entity(int(x[1]))
            msg = f"**๐ Welcome** [{user.first_name}](tg://user?id={user.id}), \n\n**๐ You need to Join** {channel.title} **to chat in this group.**"
            if not channel.username:
                link = (await bot(ExportChatInviteRequest(channel))).link
            else:
                link = "https://t.me/" + channel.username
            result = [
                await builder.article(
                    title="force_sub",
                    text = msg,
                    buttons=[
                        [Button.url(text="Channel", url=link)],
                        [custom.Button.inline("๐ Unmute Me", data=unmute)],
                    ],
                )
            ]

        elif event.query.user_id == bot.uid and query == "alive":
            he_ll = alive_txt.format(Config.ALIVE_MSG, tel_ver, x_ver, uptime, abuse_m, is_sudo)
            alv_btn = [
                [Button.url(f"{X_USER}", f"tg://openmessage?user_id={P_4_PEEYUSH}")],
                [Button.url("My Channel", f"https://t.me/{my_channel}"), 
                Button.url("My Group", f"https://t.me/{my_group}")],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=he_ll,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=he_ll,
                    title="XBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=he_ll,
                    title="XBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )

        elif event.query.user_id == bot.uid and query == "pm_warn":
            xbo_t = X_FIRST.format(x_mention, mssge)
            result = builder.photo(
                file=x_pic,
                text=xbo_t,
                buttons=[
                    [
                        custom.Button.inline("๐ Request ๐", data="req"),
                        custom.Button.inline("๐ฌ Chat ๐ฌ", data="chat"),
                    ],
                    [custom.Button.inline("๐ซ Spam ๐ซ", data="heheboi")],
                    [custom.Button.inline("Curious โ", data="pmclick")],
                ],
            )

        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**โก โัgัฮทโฮฑัั ฮฑฦ ฯ-ฯัััะฒฯั โก**",
                buttons=[
                    [Button.url("๐ Repo ๐", "https://t.me/x_discussion")],
                    [Button.url("๐ Deploy ๐", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FX-USERBOT%2FX-MAIN&template=https%3A%2F%2Fgithub.com%2FX-USERBOT%2X-MAIN")],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[โโโ โ]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "@X_User_Bot",
                text="""**Hey! This is [ฯ-ฯัััะฒฯั](https://t.me/X_User_Bot) \nYou can know more about me from the links given below ๐**""",
                buttons=[
                    [
                        custom.Button.url("๐ฅ CHANNEL ๐ฅ", "https://t.me/X_User_Bot"),
                        custom.Button.url(
                            "โก GROUP โก", "https://t.me/X_Discussion"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "โจ REPO โจ", "https://github.com/LiveToLife/X-Userbot"),
                        custom.Button.url
                    (
                            "๐ฐ TUTORIAL ๐ฐ", "Not Available"
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"๐ฐ This is ฯ-ฯัััะฒฯั PM Security for {x_mention} to keep away unwanted retards from spamming PM..."
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"โ **Request Registered** \n\n{x_mention} will now decide to look for your request or not.\n๐ Till then wait patiently and don't spam!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**๐ Hey {x_mention} !!** \n\nโ๏ธ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
            await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {x_mention} to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**๐ Hey {x_mention} !!** \n\nโ๏ธ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"๐ฅด **Gtfo Blocked Restard**"
            )
            await bot(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await bot.send_message(
                LOG_GP,
                f"**Blocked**  [{first_name}](tg://user?id={ok}) \n\nReason:- Spam",
            )


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(1)).decode("UTF-8")
        x = hunter.split("+")
        if not event.sender_id == int(x[0]):
            return await event.answer("This Ain't For You!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(x[1]), int(x[0])))
        except UserNotParticipantError:
            return await event.answer(
                "You need to join the channel first.", alert=True
            )
        await bot.edit_permissions(
            event.chat_id, int(x[0]), send_message=True, until_date=None
        )
        await event.edit("Yay! You can chat now !!")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
            if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
                current_page_number=0
                simp = button(current_page_number, CMD_HELP)
                veriler = button(0, sorted(CMD_HELP))
                apn = []
                for x in CMD_LIST.values():
                    for y in x:
                        apn.append(y)
                await event.edit(
                    f"๐ฐ **{x_mention}**\n\n๐ __No.of Plugins__ : `{len(CMD_HELP)}` \n๐๏ธ __Commands__ : `{len(apn)}`\n๐๏ธ __Page__ : 1/{veriler[0]}",
                    buttons=simp[1],
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = "ัะฝฮนั ฮนั ะผั ะผฮฑัััั ฯัััะฒฯั ัฯฯ ยขฮฑฮทั ฯัั ฮนั ะผฮฑะบั ัฯฯั ฯฯฮท ฦัฯะผ @X_User_Bot . ยฉ ฯ-ฯัััะฒฯั"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            veriler = custom.Button.inline(f"{x_emoji} Re-Open Menu {x_emoji}", data="reopen")
            await event.edit(f"**โ๏ธ  ะผรชรฑรป ฯ-ฯัััะฒฯั ฯrรตvรฎdรชr รฌs รฑรดw รlรถsรซd โ๏ธ**\n\n**Bot Of :**  {x_mention}\n\n        [ยฉ๏ธ X-Userbotโข๏ธ]({chnl_link})", buttons=veriler, link_preview=False)
        else:
            reply_pop_up_alert = "ัะฝฮนั ฮนั ะผั ะผฮฑัััั ฯัััะฒฯั ัฯฯ ยขฮฑฮทั ฯัั ฮนั ะผฮฑะบั ัฯฯั ฯฯฮท ฦัฯะผ @X_User_Bot . ยฉ ฯ-ฯัััะฒฯัโข"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"๐ฐ **{x_mention}**\n\n๐ __No.of Plugins__ : `{len(CMD_HELP)}`\n๐๏ธ __Commands__ : `{len(apn)}`\n๐๏ธ __Page__ : {page + 1}/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "ัะฝฮนั ฮนั ะผั ะผฮฑัััั ฯัััะฒฯั ัฯฯ ยขฮฑฮทั ฯัั ฮนั ะผฮฑะบั ัฯฯั ฯฯฮท ฦัฯะผ @X_User_Bot . ยฉ ฯ-ฯัััะฒฯัโข",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "โก " + cmd[0] + " โก", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"{x_emoji} Main Menu {x_emoji}", data=f"page({page})")])
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**๐ File :**  `{commands}`\n**๐ข Number of commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "ัะฝฮนั ฮนั ะผั ะผฮฑัััั ฯัััะฒฯั ัฯฯ ยขฮฑฮทั ฯัั ฮนั ะผฮฑะบั ัฯฯั ฯฯฮท ฦัฯะผ @X_User_Bot . ยฉ ฯ-ฯัััะฒฯั โข",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**๐ File :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**โ ๏ธ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**โ ๏ธ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**โน๏ธ Info :**  {CMD_HELP_BOT[cmd]['info']['info']}\n\n"
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**๐  Commands :**  `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**๐  Commands :**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**๐ฌ Explanation :**  `{command['usage']}`\n\n"
        else:
            result += f"**๐ฌ Explanation :**  `{command['usage']}`\n"
            result += f"**โจ๏ธ For Example :**  `{HANDLER[:1]}{command['example']}`\n\n"
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                result,
                buttons=[
                    custom.Button.inline(f"{x_emoji} Return {x_emoji}", data=f"Information[{page}]({cmd})")
                ],
                link_preview=False,
            )
        else:
            return await event.answer(
                "ัะฝฮนั ฮนั ะผั ะผฮฑัััั ฯัััะฒฯั ัฯฯ ยขฮฑฮทั ฯัั ฮนั ะผฮฑะบั ัฯฯั ฯฯฮท ฦัฯะผ @X_User_Bot . ยฉ ฯ-ฯัััะฒฯั โข",
                cache_time=0,
                alert=True,
            )


# hellbot
