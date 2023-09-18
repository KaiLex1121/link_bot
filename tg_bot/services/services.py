from typing import Union
from keyboards.keyboards import UserKeyboards, AdminKeyboards
from aiogram.types import Message, ReplyKeyboardMarkup
from filters.admin_filters import AdminFilter
from config_data.config import Config, RedisConfig
from config_data import config


def get_start_keyboard_by_role(message: Message) -> ReplyKeyboardMarkup:
    cfg: Config = config.load_config('.env')
    ids = cfg.tg_bot.admins_ids

    if message.from_user.id in ids:
        return AdminKeyboards.admin_start_keyboard
    return UserKeyboards.start_keyboard


def get_redis() -> dict[str, int | str]:
    cfg: Config = config.load_config('.env')
    redis_params = {
        'host': cfg.redis.redis_host,
        'password': cfg.redis.redis_pass,
        'port': cfg.redis.redis_pass
    }

    return redis_params