from Ub.helpers.decorators import authorized_users_only
from config import HNDLR
import psutil
from psutil._common import bytes2human
from pyrogram import filters
from pyrogram import Client as blaze
from Ub import START_TIME
from datetime import datetime
import time


Alive_pic = "https://telegra.ph/file/a8fff8cafaf00ee379280.jpg", 

@blaze.on_message(filters.command(["alive"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def gooe_search(client, message):
    start_time = time.time()
    uptime = (datetime.now() - START_TIME)
    reply_msg = f"**MADE IN 🇮🇳 , MADE WITH 😻**"
    reply_msg += "------------------\n\n"
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    reply_msg += f"🔸Pɪɴɢ Tɪᴍᴇ: **{ping_time}ms\n**"
    reply_msg += f"🔹Kɪɴɢ Uᴘᴛɪᴍᴇ: **{uptime}\n**"
    reply_msg += f"🔸Sᴜᴘᴘᴏʀᴛ: **@RaiChuOffiCial\n**"
    reply_msg += f"🔹Rᴇᴘᴏ: **[HERE](https://github.com/ProXSammY/RaiChu)\n**"
    reply_msg += f"🔸Pʏᴛʜᴏɴ: **3.8\n\n**"
    reply_msg += f"🍹Sᴇʀᴠᴇʀꜱ Fᴜɴᴄᴛɪᴏɴɪɴɢ Nᴏʀᴍᴀʟ🍹"
    await client.send_photo(message.chat.id , reply_msg)
    await message.delete()
    if vcbot is not None:
        vcbot.send_message(message.chat.id, "Voice player alive")
