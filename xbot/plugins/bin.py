from telethon import functions, types, events
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from . import *

@bot.on(x_cmd(pattern="bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    xbot = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Searching ur bin 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/bin {}".format(xbot))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@bot.on(x_cmd(pattern="vbv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    xbot = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/vbv {}".format(xbot))
              respond = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if respond.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
              
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
    
@bot.on(x_cmd(pattern="key ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    xbot = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/key {}".format(xbot))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
  
@bot.on(x_cmd(pattern="iban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    xbot = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/iban {}".format(xbot))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @Carol5_bot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
             
           
           
CmdHelp("Bin Chacker").add_command(
  "bin", "Checks The Bin"
).add_command(
  "vbv", "Checks The Vbv"
).add_command(
  "key", "Checks The Sk Key"
).add_command(
  "iban", "Checks The Iban"
).add_info(
  "Check Bin/Iban/skey/vbv Etc."
).add_warning(
  "✅ Harmless Module."
).add()
