from dataclasses import dataclass, field
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.chat import ChatDAO
from app.dao.user import UserDAO


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
