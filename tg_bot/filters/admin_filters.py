from aiogram.filters import BaseFilter
from aiogram.types import Message
from config_data.config import Config
from config_data import config

class AdminFilter(BaseFilter):
    is_admin: bool = True
    cfg = config.load_config('.env')
    ids = cfg.tg_bot.admins_ids

    # async def __call__(self, obj: Message, config: Config) -> bool:
    #     return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin

    async def __call__(self, obj: Message) -> bool:
        return (obj.from_user.id in self.ids) == self.is_admin