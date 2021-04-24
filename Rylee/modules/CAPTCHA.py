import Rylee.modules.sql.captcha_sql as sql
from Rylee import tbot, CMD_HELP
from Rylee.events import is_admin
import os
from telethon import Button, events

turnon = ["on", "yes", "enable"]
turnoff = ["off", "no", "disable"]

@tbot.on(events.NewMessage(pattern="^[!?/]captcha ?(.*)"))
@is_admin
async def lel(event, perm):
 if not perm.change_info:
         await event.reply("You are missing the following rights to use this command:CanChangeInfo!")
         return
 args = event.pattern_match.group(1)
 settings = sql.get_mode
 if not args:
  if settings == False:
   await event.reply("Currently Welcome CAPTCHAs are disabled for this Chat.")
  else:
   await event.reply("Currently Welcome CAPTCHAs are enabled for this Chat.")
 elif args in turnon:
  mode = True
  await event.reply("Enabled Welcome CAPTCHAs for this chat.")
  x = sql.set_mode(event.chat_id, mode)
 elif args in turnoff:
  mode = False
  await event.reply("Disabled Welcome CAPTCHAs for this chat.")
  x = sql.set_mode(event.chat_id, mode)
