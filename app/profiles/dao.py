from sqlalchemy import select

from app.base.dao import BaseDAO
from app.database import async_session_maker
from app.profiles.models import Profile


class ProfileDAO(BaseDAO):
    model = Profile


    @classmethod
    async def find_by_email(cls, email):
        async with async_session_maker() as session:
            query = select(Profile).where(
                Profile.email == email
            )
            result = await session.execute(query)
            return result.scalars().one_or_none()