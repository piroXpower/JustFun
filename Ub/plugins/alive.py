from Ub.helpers.decorators import authorized_users_only
from config import HNDLR
import psutil
from psutil._common import bytes2human
from pyrogram import filters
from pyrogram import Client as blaze
from Ub import START_TIME
from datetime import datetime
import time

__version__== "1.3.6"

Alive_pic = "https://telegra.ph/file/a8fff8cafaf00ee379280.jpg", 

@blaze.on_message(filters.command(["alive"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def get_sysinfo(client, m):
     m_reply = await m.reply_photo(
                                 photo="https://telegra.ph/file/a8fff8cafaf00ee379280.jpg",
                                 caption="**Kʀɪᴘʏᴀ Dʜʏᴀɴ Dᴇ**\n**Rᴀɪᴄʜᴜ Usᴇʀʙᴏᴛ Aʙʜɪ Jɪɴᴅᴀ Hᴀɪ**\n\n𝗩𝗘𝗥𝗦𝗜𝗢𝗡𝗦:-\n\n𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠:{version}\n𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠:64 bit\n\n**[USERBOT-SUPPORT](t.me/RaichuOfficiL)\n[USERBOT-CHANNE](t.me/RaichuUpdate), 

 ) 
