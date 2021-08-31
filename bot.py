from pyrogram import Client,types
import uuid
import logging

DOMAIN = "https://file-to-link-ar.herokuapp.com"
logging.basicConfig()
client = Client("bot",'3069922','66b2a19c29c56c943c726af7200c41fd',bot_token="1877221140:AAHBauy1O1O0sXmE9RGtrzeZ6GsX7iIx_xU",
#proxy=dict(hostname="127.0.0.1",port=8010)
# )



@client.on_message()
async def handler1(_,m:types.Message):
    photo = m.photo
    print(m)
    if photo:
        await client.download_media(m,f"files/{photo.file_id}.png")
        await m.reply(f"Link: {DOMAIN}/{photo.file_id}.png")



client.run()
