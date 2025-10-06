from telethon import TelegramClient
import asyncio
import time

loop = 0
api_id = 29520252
api_hash = '55a15121bb420b21c3f9e8ccabf964cf'
phone_number = '+212669720067'
text = input("msg : ")
async def simple_send():
    async with TelegramClient('session_x', api_id, api_hash) as client:
        await client.start(phone=phone_number)
        await client.send_message('@fakemailbot', text)
        print(f"Sending msg...{loop}")
while True:
   asyncio.run(simple_send())
   loop+=1
   time.sleep(1)
