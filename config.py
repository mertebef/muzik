from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("7682089699:AAG1NfwiKJ2QveEsK7dNkIKEvzK9ONrsQqA")
THUMB_IMG = getenv("THUMB_IMG", "https://graph.org/file/fa5ccd7123f36f9e12592.jpg")
BOT_NAME = getenv("BOT_NAME", "🎧 Muud Müzik")
API_ID = int(getenv("27264326"))
API_HASH = getenv("eef640f8abe078ff5c89defa3195c5c1")
BOT_USERNAME = getenv("@muzikzireflex_bot") 
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "PlutoFederation")
PLAYLIST_NAME = getenv("PLAYLIST_NAME", "PlutoFm") 
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
OWNER = getenv("7372527536", "7372527536")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
PLAYLIST_ID = int(getenv("PLAYLIST_ID"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7372527536").split()))
