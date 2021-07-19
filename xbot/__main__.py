import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from xbot import LOGS, bot, tbot
from xbot.config import Config
from xbot.utils import load_module
from xbot.version import __xbot__ as xver
hl = Config.HANDLER
X_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/cc64741c316f3d720b998.jpg"

# let's get the bot ready
async def x_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"X_SESSION - {str(e)}")
        sys.exit()


# hellbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting χ-υѕєявσт 🔰")
            bot.loop.run_until_complete(x_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 χ-υѕєявσт Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "xbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/The-HellBot/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "hellbot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your χ-υѕєявσт Is Now Working ⚡")
LOGS.info(
   " Join @X_User_Bot For Updatee About χ-υѕєявσт Also Join Discussion Group.."
)

# that's life...
async def x_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                X_PIC,
                caption=f"#START \n\nDeployed χ-υѕєявσт Successfully\n\n**χ-υѕєявσт - {xver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [χ-υѕєявσт Channel](t.me/X_User_Bot) for Updates & [χ-υѕєявσт Chat](t.me/x_discussion) for any query regarding χ-υѕєявσт",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join HellBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@X_User_Bot"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@HellBot_Chat"))
#    except BaseException:
#        pass


bot.loop.create_task(x_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# hellbot
