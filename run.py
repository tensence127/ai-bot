import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from config import BOT_TOKEN

async def main():
    try:
        async with Bot(token=BOT_TOKEN) as bot:
            dp = Dispatcher()
            dp.include_router(router)
            await dp.start_polling(bot)
    except Exception as e:
        print(f'Не удалось запустить бота, ошибка {e}')
        raise SystemExit(1) from e

if __name__ == "__main__":
    asyncio.run(main())
