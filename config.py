import re, os, time
from typing import List
id_pattern = re.compile(r'^.\d+$') 

class Config(object):

    API_ID = os.environ.get("API_ID", "32541562")
    API_HASH = os.environ.get("API_HASH", "e37e4432298d5a5eb4a6e32c18804283")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8333565963:AAGVAf8wPMVRM1imA8R3v7xIxmw6Ts6gXmI") 
    BOT = None

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "Rename_Bot")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://asvm:incorrectasvm@cluster0.v2z8vnw.mongodb.net/?appName=Cluster0")
 
    # other configs
    PIC = os.environ.get("PIC", "https://i.ibb.co/4RLprbc0/20260823-215817.jpg")
    ADMIN = int(os.environ.get("ADMIN", "8676822109"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002521835919"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944 # calculation 6*1024*1024*1024=results

    # premium mode feature ✅
    UPLOAD_LIMIT_MODE = True 
    PREMIUM_MODE = True 
    
    #force subs
    IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
    AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "").split())) # Add Multiple channel ids
    AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
    FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>{}, ᴛʜɪs ɪs ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ & ᴘᴏᴡᴇʀғᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ 🚀...\n
Wɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs, ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟs & ᴄᴜsᴛᴏᴍɪᴢᴇ ᴄᴀᴘᴛɪᴏɴs. ✨

Vɪᴅᴇᴏ ➜ Fɪʟᴇ | Fɪʟᴇ ➜ Vɪᴅᴇᴏ | Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ | Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ Sᴜᴘᴘᴏʀᴛ | Fᴀsᴛ & Eᴀsʏ Rᴇɴᴀᴍɪɴɢ | Sɪᴍᴘʟᴇ • Fᴀsᴛ • Pᴏᴡᴇʀғᴜʟ"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : {}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : {}
├📕 Lɪʙʀᴀʀy : {}
├✏️ Lᴀɴɢᴜᴀɢᴇ: {}
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: {}</b>     
╰───────────────⍟ """

    HELP_TXT = """✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \n\nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ Document, Video, Audio ]."""

    UPGRADE_PREMIUM= """
•⪼ ★𝘗𝘭𝘢𝘯𝘴    -  ⏳𝘋𝘢𝘵𝘦 - 💸𝘗𝘳𝘪𝘤𝘦 
•⪼ 🥉𝘉𝘳𝘰𝘯𝘻𝘦  -   3𝘥𝘢𝘺𝘴 -   39
•⪼ 🥈𝘚𝘪𝘭𝘷𝘦𝘳   -   7𝘥𝘢𝘺𝘴 -   59
•⪼ 🥇𝘎𝘰𝘭𝘥    -  15𝘥𝘢𝘺𝘴 -  99
•⪼ 🏆𝘗𝘭𝘢𝘵𝘪𝘯𝘶𝘮 -  1𝘮𝘰𝘯𝘵𝘩 -  179
•⪼ 💎𝘋𝘪𝘢𝘮𝘰𝘯𝘥 -  2𝘮𝘰𝘯𝘵𝘩 -  339

- 𝘋𝘢𝘪𝘭𝘺 𝘜𝘱𝘭𝘰𝘢𝘥 𝘓𝘪𝘮𝘪𝘵 𝘜𝘯𝘭𝘪𝘮𝘪𝘵𝘦𝘥
- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 𝘙𝘴.9"""
    
    UPGRADE_PLAN= """
𝘗𝘭𝘢𝘯: 𝘗𝘳𝘰
𝘋𝘢𝘵𝘦: 1 𝘮𝘰𝘯𝘵𝘩 
𝘗𝘳𝘪𝘤𝘦: 179
𝘓𝘪𝘮𝘪𝘵: 100 𝘎𝘉

𝘗𝘭𝘢𝘯: 𝘜𝘭𝘵𝘢 𝘗𝘳𝘰 
𝘋𝘢𝘵𝘦: 1 𝘮𝘰𝘯𝘵𝘩 
𝘗𝘳𝘪𝘤𝘦: 199
𝘓𝘪𝘮𝘪𝘵: 1000 𝘎𝘉

- 𝘋𝘪𝘴𝘤𝘰𝘶𝘯𝘵 𝘈𝘭𝘭 𝘗𝘭𝘢𝘯 𝘙𝘴.9"""
    
    THUMBNAIL = """🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>

<b>•></b> Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /delthumb - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /viewthumb - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
"""

    CAPTION= """📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /setcaption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /seecaption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /delcaption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ:- `/setcaption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`"""

    BOT_STATUS = """⚡️ ʙᴏᴛ sᴛᴀᴛᴜs ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 ᴛᴏᴛᴀʟ ᴜsᴇʀꜱ: `{}`
💸 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: `{}`
֍ ᴜᴘʟᴏᴀᴅ: `{}`
⊙ ᴅᴏᴡɴʟᴏᴀᴅ: `{}`"""

    LIVE_STATUS = """⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V𝟹.𝟶.𝟶 [STABLE]"""

    DIGITAL_METADATA = """❪ SET CUSTOM METADATA ❫

- /metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

`--change-title ASVM
--change-video-title ASVM
--change-audio-title ASVM
--change-subtitle-title ASVM
--change-author ASVM`
"""
    
    CUSTOM_FILE_NAME = """<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /setprefix - To add a prefix along with your _filename.
➢ /seeprefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /delprefix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /setsuffix - To add a suffix along with your filename_.
➢ /seesuffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
➢ /delsuffix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!

Exᴀᴍᴩʟᴇ:- `/setsuffix @TechifyBots`
Exᴀᴍᴩʟᴇ:- `/setprefix @TechifyBots`"""

    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
    
More Update Coming Soon..."""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

`--change-title ASVM
--change-video-title ASVM
--change-audio-title ASVM
--change-subtitle-title ASVM
--change-author ASVM`
"""
    
    PROGRESS = """<b>
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
┃  𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗜𝗡𝗚...\n\n
┣⪼ 𝗦𝗜𝗭𝗘: {1} | {2} | 𝗗𝗢𝗡𝗘: {0}% | 𝗦𝗣𝗘𝗘𝗗: {3}/s | 𝗘𝗧𝗔: {4}
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯</b>"""
