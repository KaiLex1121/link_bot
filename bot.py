import asyncio
from config_data.config import load_config, Config
from aiogram import Bot, Dispatcher
from handlers import user_handlers, admin_handlers
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandStart


async def main() -> None:

    config: Config = load_config('.env')
    bot: Bot = Bot(config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
