from aiogram.fsm.storage.redis import Redis
from typing import Union, Awaitable, Any


async def add_to_redis(redis: Redis, key: str, value: str) -> Union[Awaitable, Any]:
    return await redis.set(name=key, value=value)


async def get_from_redis(redis: Redis, key: str) -> Union[Awaitable, Any]:
    return (await redis.get(key).decode('utf-8'))
