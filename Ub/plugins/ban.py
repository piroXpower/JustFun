@blaze.on_message(filters.command(["ban"], prefixes=f"{HNDLR}"))
@authorized_users_only
def ban(bot, message):
    await blaze.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await blaze.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Banned Successfully")
try:
   except Exception as exc:
    await message.reply_to_message.reply(f"{exc}")

@blaze.on_message(filters.command(["ban"], prefixes=f"{HNDLR}"))
@authorized_users_only
def ban(bot, message):
    await blaze.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await blaze.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Unban Successfully")
try:
   except Exception as exc:
    await message.reply_to_message.reply(f"{exc}")
