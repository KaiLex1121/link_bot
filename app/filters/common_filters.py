from aiogram.filters import BaseFilter
from aiogram.types import Message
from app.config.main_config import Config
from app.config import main_config


class IsLink(BaseFilter):

    is_link: bool = True

    def is_link(self, message: Message):
        return message.text.startswith('http://') or message.text.startswith('https://') or message.text.startswith('t.me')

    async def __call__(self, obj: Message) -> bool:
        return self.is_link(obj)