from aiogram.fsm.storage.redis import Redis


_redis: Redis = Redis(decode_responses=True)


async def add_to_redis(key: str, value: str) -> str:
    return await _redis.set(name=key, value=value)


async def get_from_redis(key: str) -> str:
    return await _redis.get(key)
