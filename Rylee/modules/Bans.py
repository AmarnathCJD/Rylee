from Rylee import tbot, CMD_HELP
import os
from telethon import events
from Rylee.events import is_admin

@tbot.on(events.NewMessage(pattern="^[!/?]ben ?(.*)"))
async def ben(event):
 if event.reply_to_msg_id:
  k = await event.get_reply_message()
  id = k.sender_id
  name = k.sender.first_name
 else:
  id = event.sender_id
  name = event.sender.first_name
 await event.respond(f"Another one bites the dust...!\nBanned [{name}](tg://user?id={id}).")
