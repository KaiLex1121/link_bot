from keyboards.keyboards import UserKeyboards, AdminKeyboards
from aiogram.types import Message, ReplyKeyboardMarkup
from app.config.main_config import Config


def get_start_keyboard_by_role(
    message: Message,
    config: Config
) -> ReplyKeyboardMarkup:
    ids = config.tg_bot.admins_ids

    if message.from_user.id in ids:
        return AdminKeyboards.start_keyboard
    return UserKeyboards.start_keyboard
