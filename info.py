import re, time
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


# PyroClient Setup 
API_ID = int(environ['API_ID', '28766774'])
API_HASH = environ['API_HASH', 'b8b7a890c64bca1621f3e5666dbd0894']
BOT_TOKEN = environ['BOT_TOKEN', '6950512386:AAHQkHR2n6Q9v9rVIWkP00Ki4obxyEeTTCw']

# Bot settings
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
PICS = (environ.get('PICS' ,'https://telegra.ph/file/0a7ac675cc4c62924bfdb.jpg https://telegra.ph/file/19f532ca9c6f7c62b341f.jpg https://telegra.ph/file/4bab06886e4c17a06e109.jpg https://telegra.ph/file/4aa72a36f453a9f848b65.jpg')).split()
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1124414278').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001916078002').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1124414278').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001916078002')
auth_grp = environ.get('AUTH_GROUP', '-1001861725083')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://Sujansg:YEl29iSyxtAKNZT1@cluster0.p0ng9ea.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URL)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Pᴏᴘᴄᴏʀɴɪx_files')

# Filters Configuration 
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)

WELCOM_PIC = environ.get("WELCOM_PIC", "https://telegra.ph/file/03773b2ef3015e89be3a7.jpg")
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "")

# url shortner
SHORT_URL = environ.get("SHORT_URL", 'adrinolinks.in')
SHORT_API = environ.get("SHORT_API", '90ccb8eec02b00fa42865032c17984d7ce8f81eb')

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001856149007'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'PopcornixBotSupportGroup')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001935596221')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"






