import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from google import genai
from dotenv import load_dotenv
from handlers import user

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")
bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
dp.include_router(user)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
