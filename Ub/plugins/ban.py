from Ub import tlthn as blaze
from Ub.status import *
from telethon import events, Button
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights


@blaze.on(events.NewMessage(pattern="^[.?/]kick ?(.*)"))
@is_admin
async def ban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply("You are missing the following rights to use this command:CanBanUsers!")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to ban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await Evil.get_entity(us)
    await Evil(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}")

