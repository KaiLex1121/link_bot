import asyncio
import logging

from config_data.config import load_config, Config
from aiogram import Bot, Dispatcher
from handlers import user_handlers, admin_handlers
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder, Redis
from aiogram.fsm.storage.memory import MemoryStorage

from middlewares.config import ConfigMiddleware
from middlewares.redis import RedisMiddleware


def register_global_middlewares(dp: Dispatcher, config: Config, redis: Redis) -> None:

    middleware_types = [
        ConfigMiddleware(config),
        RedisMiddleware(redis)
    ]

    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)


def get_storage(config: Config) -> MemoryStorage | RedisStorage:

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
    register_global_middlewares(dp=dp, config=config, redis=storage.redis)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot has stopped")