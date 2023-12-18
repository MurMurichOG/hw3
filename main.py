import asyncio
from aiogram import types
import logging
from handlers.bot import bot, dp
from handlers.start import start_router



async def main():
    await bot.set_my_commands([types.BotCommand(command="start", description="Начало"), types.BotCommand(command="stop", description="Стоп")])

    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())