#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6270657520:AAG8HnQesUcsV7mjqolRT9hJex1dZKI4WNg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26461352"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ab9cc32776ada8335852b50cd96bb8c6")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001637710147"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5069888600"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://AiTool:AiTool@cluster0.pxliet0.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5069888600 5554564210").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{filename}\n\n{💝 𝗝𝗼𝗶𝗻 𝗕𝗮𝗰𝗸𝗨𝗽 : <a href=https://t.me/luluofficiall>𝑪𝒍𝒊𝒄𝒌 𝑯𝒆𝒓𝒆</a> 👈\n💝 𝗠𝗼𝘃𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 : <a href=https://t.me/luluofficiall>𝑪𝒍𝒊𝒄𝒌 𝑯𝒆𝒓𝒆</a> 👈}")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🤩"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
