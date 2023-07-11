import asyncio
from config_data.config import load_config, Config
from aiogram import Bot, Dispatcher
from handlers import user_handlers
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandStart
from keyboards.set_menu import set_main_menu


async def main() -> None:

    config: Config = load_config('.env')
    bot: Bot = Bot(config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Register user_handler router
    dp.include_router(user_handlers.router)
    dp.startup.register(set_main_menu)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
