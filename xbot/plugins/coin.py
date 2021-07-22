import random

from xbot import CMD_HELP

from xbot.utils import x_cmd

from . import *

@bot.on(x_cmd(pattern="coin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "heads":
            await event.edit("`The coin landed on:` **Heads**. \n You were correct.")
        elif input_str == "tails":
            await event.edit(
                "`The coin landed on:` **Heads**. \n You weren't correct, try again ..."
            )
        else:
            await event.edit("`The coin landed on:` **Heads**.")
    elif r % 2 == 0:
        if input_str == "tails":
            await event.edit("`The coin landed on:` **Tails**. \n You were correct.")
        elif input_str == "heads":
            await event.edit(
                "`The coin landed on:` **Tails**. \n You weren't correct, try again ..."
            )
        else:
            await event.edit("`The coin landed on:` **Tails**.")
    else:
        await event.edit("¯\_(ツ)_/¯")
        
CmdHelp("coin").add_command(
  "coin", "Flip The Coin Results Will Be Random"
).add_info(
  "Flips The Coin And Random Heads/Tails Is Given If You Select tails/ then after coin command send tails/heads Then Results Will Be Shown."
).add_warning(
  "✅ Harmless Module."
).add()
