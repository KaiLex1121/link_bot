from keyboards.keyboards import UserKeyboards, AdminKeyboards
from aiogram.types import Message, ReplyKeyboardMarkup
from filters.admin import AdminFilter
from config_data.config import Config
from config_data import config


def get_start_keyboard_by_role(message: Message) -> ReplyKeyboardMarkup:
    cfg: Config = config.load_config('.env')
    ids = cfg.tg_bot.admins_ids

    if message.from_user.id in ids:
        return AdminKeyboards.admin_start_keyboard
    return UserKeyboards.start_keyboard