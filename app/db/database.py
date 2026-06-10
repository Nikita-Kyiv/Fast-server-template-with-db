from typing import Optional
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)

from app.settings import settings


class db:
    engine: Optional[AsyncEngine] = None
    session_maker: Optional[async_sessionmaker] = None

    @classmethod
    def create_as_engine(cls):
        cls.engine = create_async_engine(
            settings.db_dsn, echo=settings.debug, future=True
        )
        return cls.engine

    @classmethod
    async def close_as_engine(cls):
        await cls.engine.dispose()

    @classmethod
    def create_as_session_maker(cls):
        cls.session_maker = async_sessionmaker(
            cls.engine, expire_on_commit=False, class_=AsyncSession
        )
        return cls.session_maker

    # @classmethod
    # async def close_as_session_maker(cls):
    #     await cls.session_maker.close_all()
