from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


if settings.MODE == 'TEST':
    DATABASE_URL = settings.TEST_DATABASE_URL
else:
    DATABASE_URL = settings.DATABASE_URL


engine = create_async_engine(DATABASE_URL)


async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass