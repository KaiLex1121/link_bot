import datetime

from sqlalchemy import and_, func
from sqlalchemy.future import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import dto
from app.dao.base import BaseDAO
from app.models.database.user import User
from app.services.user_count import get_users_count_by_days


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_tg_id(self, tg_id: int) -> User:
        result = await self.session.execute(
            select(User).where(User.tg_id == tg_id)
        )
        return result.scalar_one()

    async def get_new_users_count_by_days(self, days: int = 0) -> int:
        result = await get_users_count_by_days(
            self, self.model.created_at, days
        )
        return result

    async def get_active_users_count_by_days(self, days: int = 0) -> int:
        result = await get_users_count_by_days(
            self, self.model.updated_at, days
        )
        return result

    async def upsert_user(self, user: dto.User) -> dto.User:
        kwargs = dict(
            tg_id=user.tg_id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            is_bot=user.is_bot,
            language_code=user.language_code,
        )
        saved_user = await self.session.execute(
            insert(User)
            .values(**kwargs, updated_at=func.now())
            .on_conflict_do_update(
                index_elements=(User.tg_id,),
                set_=dict(**kwargs, updated_at=func.now()),
                where=User.tg_id == user.tg_id,
            )
            .returning(User)
        )
        return saved_user.scalar_one().to_dto()
