from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admins_ids: list[int]

    @staticmethod
    def load_from_env(env: Env):
        """
        Creates the TgBot object from environment variables.
        """
        token: str = env.str("BOT_TOKEN")
        admin_ids: list[int] = list(map(int, env.list("ADMIN_IDS")))
        return TgBot(token=token, admins_ids=admin_ids)


@dataclass
class Config:
    """
    Creates the TgBot object from environment variables.
    """

    tg_bot: TgBot


def _get_environment(path: str | None = None) -> Env:
    """
    Reads environment.
    """

    env: Env = Env()
    env.read_env(path=path)

    return env


def get_channel_link(channel: str | None = None) -> str:
    """
    Loads links from environment variables.
    """

    env: Env = _get_environment()

    if channel == 'main':
        return env('MAIN_CHANNEL_LINK')
    return env('SECOND_CHANNEL_LINK')


def load_config(path: str | None) -> Config:
    """

    The main configuration class that integrates all the other configuration classes.

    This class holds the other configuration classes, providing a centralized point of access for all settings.

    Attributes
    ----------
    tg_bot : TgBot
        Holds the settings related to the Telegram Bot.

    """

    env = _get_environment()

    config = Config(tg_bot=TgBot.load_from_env(env))

    return config
