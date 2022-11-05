from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","Tgm Drugs Of Yuvan")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "thavarajtj")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/tamilbestfriendss")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3f0c65d3899e9985eb202.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e2021dfd84a80c17cfff8.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
