from Rylee import tbot, CMD_HELP
import os
from Rylee.events import is_admin
from Rylee.Function import can_promote_users, get_user
from telethon import events

@tbot.on(events.NewMessage(pattern="^[!/?]promote ?(.*)"))
@is_admin
async def _(event, perm):
 if not perm.add_admins:
      return await event.reply("You are missing the following rights to use this command:CanAddAdmins!")
 user, title = await get_user(event)
 await event.reply(f"{user.id}-{title}")
