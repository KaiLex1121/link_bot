from dataclasses import dataclass, field
from sqlalchemy.ext.asyncio import AsyncSession

from src.dao import UserDAO, ChatDAO


@dataclass
class HolderDAO:
    session: AsyncSession
    user: UserDAO = field(init=False)
    chat: ChatDAO = field(init=False)

    def __post_init__(self):
        self.user = UserDAO(self.session)
        self.chat = ChatDAO(self.session)

    async def commit(self):
        await self.session.commit()
