# filename: userbot.py
import os
import re
import asyncio
from telethon import TelegramClient, events
from telethon.errors import RPCError

# 1) my.telegram.org dan API_ID va API_HASH oling va quyiga qo'ying
API_ID = int(21865287)
API_HASH = "0360d80b68a06231ec386486953f3a9d"
SESSION_NAME = "session"  # bu fayl .session sifatida saqlanadi

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


SOURCE_CHAT = 777000                         # yangi manba id
TARGET_CHAT = "@tg_code_for"  # kanal username yoki -100... id
# ========================

# client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_all(event):
    msg = event.message

    # Agar action (join/leave) bo'lsa ham forward qilmoqchi bo'lsangiz, bu qatorni olib tashlang.
    # if msg.action:
    #     print(f"SKIP action message id={msg.id}")
    #     return

    try:
        # Oddiy forward — original forward belgilari saqlanadi
        await client.forward_messages(entity=TARGET_CHAT, messages=msg, from_peer=SOURCE_CHAT)
        print(f"FORWARDED id={msg.id} -> {TARGET_CHAT}")
    except RPCError as e:
        print("Telegram RPC error:", e)
    except Exception as e:
        print("Error:", e)

async def main():
    print("Userbot (forward-all) ishga tushmoqda...")
    await client.start()  # birinchi marta telefon va kodni siz kiritasiz
    print(f"Tayyor: manba {SOURCE_CHAT} -> kanal {TARGET_CHAT}")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())