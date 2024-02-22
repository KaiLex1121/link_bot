import asyncio
import logging

from app.config.main_config import load_config, Config
from aiogram import Bot, Dispatcher
from handlers import user_handlers, admin_handlers
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder, Redis
from aiogram.fsm.storage.memory import MemoryStorage


from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from middlewares.config import ConfigMiddleware
from middlewares.redis import RedisMiddleware
from app.middlewares.database import DBMiddleware
from app.models.database import create_pool
from typing import Union


def setup_middlewares(
    dp: Dispatcher,
    pool: async_sessionmaker[AsyncSession],
    bot_config: Config,
    redis: Redis
) -> None:
    dp.update.outer_middleware(ConfigMiddleware(bot_config))
    dp.update.outer_middleware(DBMiddleware(pool))
    dp.update.outer_middleware(RedisMiddleware(redis))


def get_storage(config: Config) -> Union[MemoryStorage, RedisStorage]:

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
    setup_middlewares(dp, create_pool(config.db), config, storage.redis)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    finally:
        logger.error("Bot has stopped")