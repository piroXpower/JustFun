
import os

from dotenv import load_dotenv
from pyrogram import Client, filters

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "12553697"))
API_HASH = os.getenv("API_HASH", "ddbd36c19c379ce3e23eaf3a29a02ba7")
SESSION = os.getenv("SESSION", "")

HNDLR = os.getenv("HNDLR", ".")
SUPPORT = os.getenv("SUPPORT", "RaichuOfficial")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5046520072").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Ub.plugins"))

