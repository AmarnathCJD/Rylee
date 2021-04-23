from Rylee import tbot, CMD_HELP, BOT_ID
import os
from Rylee.events import is_admin
from Rylee.Function import can_promote_users, get_user, ck_admin
from telethon import events, Button
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights, ChannelParticipantsAdmins

@tbot.on(events.NewMessage(pattern="^[!/?]promote ?(.*)"))
@is_admin
async def _(event, perm):
 if event.is_private:
      return await event.reply("This command is made to be used in group chats, not in pm!")
 if not perm.add_admins:
      return await event.reply("You are missing the following rights to use this command:CanAddAdmins!")
 user, title = await get_user(event)
 if not title:
  title = "Admin"
 if await ck_admin(event, user.id):
  return await event.reply("This user is already an admin!")
 try:
  await tbot(EditAdminRequest(event.chat_id, user.id, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=True,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank=title))
  await event.respond(f"Promoted **{user.first_name}** in **{event.chat.title}**!")
 except:
  await event.reply("Seems like I don't have enough rights to do that.")
 
@tbot.on(events.NewMessage(pattern="^[!/?]demote ?(.*)"))
@is_admin
async def _(event, perm):
 if event.is_private:
      return await event.reply("This command is made to be used in group chats, not in pm!")
 if not perm.add_admins:
      return await event.reply("You are missing the following rights to use this command:CanAddAdmins!")
 user, title = await get_user(event)
 if not await ck_admin(event, user.id):
  return await event.reply("This user is not an admin!")
 try:
  await tbot(EditAdminRequest(event.chat_id, user.id, ChatAdminRights(
                    add_admins=False,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None), rank="Not Admin"))
  await event.respond(f"Demoted **{user.first_name}**!")
 except:
  await event.reply("Seems like I don't have enough rights to do that.")
 
@tbot.on(events.NewMessage(pattern="^[!/?]adminlist"))
async def admeene(event):
 if event.is_private:
      return await event.reply("This command is made to be used in group chats, not in pm!")
 if not await ck_admin(event, BOT_ID):
      return
 mentions = f"Admins in <b>{event.chat.title}</b>:"
 async for user in tbot.iter_participants(
            event.chat_id, filter=ChannelParticipantsAdmins
        ):
            if not user.deleted:
              if user.username:
                link_unf = '-@{}'
                link = link_unf.format(user.username)
                mentions += f"\n{link}"
 mentions += "\nNote: These values are up-to-date"
 await event.reply(mentions)
            


