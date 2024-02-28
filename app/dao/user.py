from datetime import timedelta, datetime

from sqlalchemy import and_, func
from sqlalchemy.future import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession


from app.dao.base import BaseDAO
from app.models.database.user import User
from app.models import dto


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_tg_id(self, tg_id: int) -> User:
        result = await self.session.execute(select(User).where(User.tg_id == tg_id))
        return result.scalar_one()

    async def get_for_seven_days(self) -> list[User]:

        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        result = await self.session.execute(
            select(func.count(self.model.id))
            .where(
                and_(
                    self.model.created_at >= start_date,
                    self.model.created_at <= end_date
                )
            )
        )
        return result.scalar_one()


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
            .values(**kwargs)
            .on_conflict_do_update(
                index_elements=(User.tg_id,),
                set_=kwargs,
                where=User.tg_id == user.tg_id,
            )
            .returning(User)
        )
        return saved_user.scalar_one().to_dto()
