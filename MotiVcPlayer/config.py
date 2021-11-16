
import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@attitude_galaxy")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/eae8df409be94d740a5cd.jpg")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@Moti_pro_vc_assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "@sweetkingdom1")
PROJECT_NAME = getenv("PROJECT_NAME", "MotiVcPlayer v1")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/Attitudeshauryaking/moti-music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
