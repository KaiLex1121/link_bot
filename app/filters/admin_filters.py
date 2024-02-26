from aiogram.filters import BaseFilter
from aiogram.types import Message
from app.config.main_config import Config


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message, config: Config) -> bool:
        return (obj.from_user.id in config.tg_bot.admins_ids) == self.is_admin
