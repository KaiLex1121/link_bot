from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsLink(BaseFilter):

    def is_link_check(self, message: Message):
        return (
            message.text.startswith("http://")
            or message.text.startswith("https://")
            or message.text.startswith("t.me")
        )

    async def __call__(self, obj: Message) -> bool:
        return self.is_link_check(obj)
