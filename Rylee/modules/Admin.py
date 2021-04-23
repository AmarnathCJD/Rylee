from Rylee import tbot, CMD_HELP
import os
from Rylee.events import is_admin
from Rylee.Function import can_promote_users, get_user
from telethon import events, Button
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

@tbot.on(events.NewMessage(pattern="^[!/?]promote ?(.*)"))
@is_admin
async def _(event, perm):
 if not perm.add_admins:
      return await event.reply("You are missing the following rights to use this command:CanAddAdmins!")
 user, title = await get_user(event)
 if not title:
  title = "Admin"
 if await is_admin(event, user.id):
  return await event.reply("This user is already an admin!")
 await event.respond(f"Promoted **{user.first_name}** in **{event.chat.title}**!")
 await tbot(EditAdminRequest(event.chat_id, user.id, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=True,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank=title))

 
