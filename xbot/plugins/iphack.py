#made by LEGENDX22 creaor LEGENDX22
#kang with credits else gay aur maa chod dunga 
#ported To X Bot


import json
import urllib.request

from xbot.utils import admin_cmd

from xbot import CMD_HELP

from . import *

@borg.on(x_cmd(pattern="ip (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    a = result["type"]
    b = result["country_code"]
    c = result["region_name"]
    d = result["city"]
    e = result["zip"]
    f = result["latitude"]
    g = result["longitude"]
    await event.edit(
        f"<b><u>INFORMATION GATHERED SUCCESSFULLY</b></u>\n\n<b>Ip type :-</b><code>{a}</code>\n<b>Country code:- </b> <code>{b}</code>\n<b>State name :-</b><code>{c}</code>\n<b>City name :- </b><code>{d}</code>\n<b>zip :-</b><code>{e}</code>\n<b>Latitude:- </b> <code>{f}</code>\n<b>Longitude :- </b><code>{g}</code>\n",
        parse_mode="HTML",
    )


CmdHelp("ip tracker").add_command(
  "ip", "Type  .ip {ip address} It will Track The Information Of The Ip Address"
).add_info(
  "Track The Ip Address."
).add_warning(
  "✅ Harmless Module."
).add()
