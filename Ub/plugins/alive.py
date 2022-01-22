from Ub.helpers.decorators import authorized_users_only
from config import HNDLR
import psutil
from psutil._common import bytes2human
from pyrogram import filters
from pyrogram import Client blaze

ALIVE_IMG = "https://telegra.ph/file/a8fff8cafaf00ee379280.jpg"

@blaze.on_message(filters.command(["alive"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def get_sysinfo(client, m):
    response = "**Raichu Userbot Is Active And On Fire🔥**:\n"
    m_reply = await m.reply_photo(
                                 photo={ALIVE_IMG},
                                 captio={response}
 ) 
