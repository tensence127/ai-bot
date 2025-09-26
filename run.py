import asyncio 
from aiogram import Bot, Dispatcher
from handlers import router
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN


async def main():
    try:
        storage = MemoryStorage()
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher(storage=storage)
        dp.include_router(router)
        await dp.start_polling(bot)

    except Exception as e:
        print(f'Не удалось запустить бота, ошибка {e}')
        raise SystemExit(1) from e


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    except Exception as e:
        print(f"Unhandled exception during startup: {e}")