## For Future
from datetime import datetime
import time
from telethon import TelegramClient
from config import STRING_SESSION, API_ID, API_HASH

starttimer=datetime.now()
START_TIME = datetime.now()

ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

print("DATE AND TIME LOADED") 
