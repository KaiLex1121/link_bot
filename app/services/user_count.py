import datetime

from sqlalchemy import and_, func
from sqlalchemy.future import select


async def get_users_count_by_days(
    instance,
    required_field,
    days: int
) -> int:
    required_date = datetime.date.today() - datetime.timedelta(days)
    required_date_start = datetime.datetime(
        required_date.year,
        required_date.month,
        required_date.day
    )
    required_date_end = datetime.datetime(
        required_date.year,
        required_date.month,
        required_date.day,
        23, 59, 59
    )

    result = await instance.session.execute(
        select(func.count(instance.model.id))
        .where(
            and_(
                required_field >= required_date_start,
                required_field <= required_date_end
            )
        )
    )
    return result.scalar_one()
