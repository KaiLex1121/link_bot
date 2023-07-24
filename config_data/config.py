from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admins_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def _get_environment(path: str | None = None) -> Env:

    env: Env = Env()
    env.read_env(path=path)

    return env


def get_main_channel_link() -> str:

    env: Env = _get_environment()

    return env('MAIN_CHANNEL_LINK')


def get_second_channel_link() -> str:

    env: Env = _get_environment()

    return env('SECOND_CHANNEL_LINK')


def load_config(path: str | None) -> Config:

    env = _get_environment(path=path)

    config = Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                                 admins_ids=env.list('ADMIN_IDS'),
                                 ))

    return config
