from dataclasses import dataclass
from environs import Env
from typing import Optional
from functools import lru_cache


@dataclass
class TgBot:
    token: str
    admins_ids: list[int]
    use_redis: bool

    @staticmethod
    def load_from_env(env: Env):
        token = env.str('BOT_TOKEN')
        admin_ids = list(map(int, env.list('ADMIN_IDS')))
        use_redis = env.bool('USE_REDIS')

        return TgBot(token=token, admins_ids=admin_ids, use_redis=use_redis)


@dataclass
class RedisConfig:
    redis_pass: Optional[str]
    redis_port: Optional[int]
    redis_host: Optional[str]

    def dsn(self) -> str:
        """
        Constructs and returns a Redis DSN (Data Source Name) for this database configuration.
        """

        return f"redis://{self.redis_host}:{self.redis_port}/1"

    @staticmethod
    def load_from_env(env: Env):
        redis_pass = env.str("REDIS_PASSWORD")
        redis_port = env.int("REDIS_PORT")
        redis_host = env.str("REDIS_HOST")

        return RedisConfig(
            redis_pass=redis_pass, redis_port=redis_port, redis_host=redis_host
        )


@dataclass
class Config:
    tg_bot: TgBot
    redis: Optional[RedisConfig] = None


@lru_cache
def _get_environment(path: str | None = None) -> Env:
    env: Env = Env()
    env.read_env(path=path)

    return env


@lru_cache
def load_config(path: str | None) -> Config:
    env = _get_environment(path)

    config = Config(
        tg_bot=TgBot.load_from_env(env),
        redis=RedisConfig.load_from_env(env)
        )

    return config
