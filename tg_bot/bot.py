import asyncio
import logging

from config_data.config import load_config, Config
from aiogram import Bot, Dispatcher
from handlers import user_handlers, admin_handlers
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.fsm.storage.memory import MemoryStorage


def get_storage(config: Config):

    if config.tg_bot.use_redis:
        storage = RedisStorage.from_url(
            url=config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True)
        )
    else:
        storage = MemoryStorage()

    return storage


logger = logging.getLogger(__name__)
log_level = logging.INFO


async def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger.info("Bot has started")

    config = load_config('.env')
    storage = get_storage(config=config)
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher(storage=storage)

    dp.include_router(user_handlers.router)
    dp.include_router(admin_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot has stopped")