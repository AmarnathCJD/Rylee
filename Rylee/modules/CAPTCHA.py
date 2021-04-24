import Rylee.modules.sql.captcha_sql as sql
from Rylee import tbot, CMD_HELP
from Rylee.events import is_admin
from Rylee.Function import can_change_info, ck_admin
import os
from telethon import Button, events

turnon = ["on", "yes", "y"]
turnoff = ["off", "no", "n"]

@tbot.on(events.NewMessage(pattern="^[!?/]captcha ?(.*)"))
async def lel(event):
 args = event.pattern_match.group(1)
 avoid = ["kick", "mode on", "kicktime", "kick", "kick off", "kick yes", "kick on", "kick no", "kick y", "kick n", "mode off", "mode on", "mode y", "mode n", "mode yes", "mode no", "kicktime [0-9]"]
 if args:
  if args in avoid:
   return
 if event.is_private:
   return await event.reply("This command is made to be used in group chats, not in pm!")
 if not await ck_admin(event, event.sender_id):
   return await event.reply("Only admins can execute this command.")
 if not await can_change_info(message=event):
   return await event.reply("You are missing the following rights to use this command:CanChangeInfo!")
 settings = sql.get_mode(event.chat_id)
 if not args:
  if settings == True:
   await event.reply("Users will be asked to complete a CAPTCHA before being allowed to speak in the chat.\nTo change this setting, try this command again followed by one of yes/no/on/off")
  elif settings == False:
   await event.reply("Users will NOT be muted when joining the chat.\nTo change this setting, try this command again followed by one of yes/no/on/off")
 elif args in turnon:
  mode = True
  await event.reply("CAPTCHAs have been enabled. I will now mute people when they join.")
  x = sql.set_mode(event.chat_id, mode)
  if not x:
    sql.set_captcha(event.chat_id, "button")
 elif args in turnoff:
  mode = False
  await event.reply("CAPTCHAs have been disabled. Users can join normally.")
  x = sql.set_mode(event.chat_id, mode)
 else:
  await event.reply(f"That isn't a boolean - expected one of y/yes/on or n/no/off; got: {args}")

@tbot.on(events.NewMessage(pattern="^[!?/]captchamode ?(.*)"))
@is_admin
async def lel(event, perm):
 options = ["math", "button", "text", "multibutton"]
 if not perm.change_info:
         await event.reply("You are missing the following rights to use this command:CanChangeInfo!")
         return
 settings = sql.get_style(event.chat_id)
 args = event.pattern_match.group(1)
 if not args:
  text = ""
  if settings == False:
   await event.reply("Enable CAPTCHAs First.!")
  elif settings in options:
   if settings == "button":
    text = """
The current CAPTCHA mode is: button
Button CAPTCHAs simply require a user to press a button in their welcome message to confirm they're human.

Available CAPTCHA modes are: button/math/text/multibutton
"""
   elif settings == "text":
    text = """
The current CAPTCHA mode is: text
Text CAPTCHAs require the user to answer a CAPTCHA containing letters and numbers.

Available CAPTCHA modes are: button/math/text/mutlibutton
"""
   elif settings == "math":
    text = """
The current CAPTCHA mode is: math
Math CAPTCHAs require the user to solve a basic maths question. Please note that this may discriminate against users with little maths knowledge.

Available CAPTCHA modes are: button/math/text/multibutton
"""
   elif settings == "multibutton":
    text = """
The current CAPTCHA mode is: multibutton
Multibutton CAPTCHAs require users to solve a button puzzle

Available CAPTCHA modes are: button/math/text/multibutton
"""
  await event.reply(text)
 elif args in options:
  style = args
  text = "CAPTCHA set to **{}**.".format(style)
  await event.reply(text)
  x = sql.set_style(event.chat_id, style)
  if not x:
   sql.set_captcha(event.chat_id, style)
 else:
  await event.reply(f"{args} is not a recognised CAPTCHA mode! Try one of: button/math/text/multibutton")


@tbot.on(events.NewMessage(pattern="^[!?/]captchakick ?(.*)"))
@is_admin
async def lel(event, perm):
 optionsp = ["y", "yes", "on"]
 optionsn = ["n", "no", "off"]
 args= event.pattern_match.group(1)
 time = 300
 settings = sql.get_time(event.chat_id)
 if not args:
   if settings == False or settings == 0:
    await event.reply("""Users that don't complete their CAPTCHA are allowed to stay in the chat, muted, and can complete the CAPTCHA whenever.

To change this setting, try this command again followed by one of yes/no/on/off""")
   else:
    await event.reply("""I am currently kicking users that haven't completed the CAPTCHA after 0 seconds

To change this setting, try this command again followed by one of yes/no/on/off""")
 elif args in optionsp:
  if settings:
   time = settings
  await event.reply(f"I will now kick people that haven't solved the CAPTCHA after {time/60} minutes.")
 elif args in optionsn:
  time = 0
  await event.reply("I will no longer kick people that haven't solved the CAPTCHA.")
 x = sql.set_time(event.chat_id, time)
 
  


