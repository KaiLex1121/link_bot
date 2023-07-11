from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admins_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path=path)

    config = Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                                 admins_ids=env.list('ADMIN_IDS')))

    return config
