import aiohttp
import asyncio
import os

URL = os.getenv("PING_URL", "https://your-bot-name.koyeb.app")  # <-- yahan aapka actual bot URL daalein

async def keep_awake():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(URL) as resp:
                    print(f"[SelfPing] Pinged {URL} - Status {resp.status}")
        except Exception as e:
            print(f"[SelfPing] Error pinging: {e}")
        await asyncio.sleep(30)
