from pyrogram import Client,types
import uuid
import logging
import time

DOMAIN = "https://file-to-link-ar.herokuapp.com"
logging.basicConfig()
client = Client("bot",'3069922','66b2a19c29c56c943c726af7200c41fd',bot_token="1877221140:AAHBauy1O1O0sXmE9RGtrzeZ6GsX7iIx_xU",
#proxy=dict(hostname="127.0.0.1",port=8010)
)

if not os.path.exists("files"):
    os.mkdir("files")

@client.on_message()
async def handler1(_,m:types.Message):
    photo = m.photo
    if photo:
        name = f"{int(time.time())}.png"
        path = await client.download_media(m,f"files/{name}")
        print(path)
        await m.reply(f"Link: {DOMAIN}/{name}")



client.run()
