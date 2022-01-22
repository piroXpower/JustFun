import asyncio
from pyrogram import idle
from config import SUPPORT, bot
from config import blaze


async def main():
    await blaze.start()
    await bot.join_chat("RaichuOfficial")            
    await bot.send_message(
            SUPPORT,
            "<b>Congrats!! Raichu UserBot has started successfully!</b>",
        )
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @TEAMDEECODE |
    ------------------
"""
    )
    await idle()
    


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
