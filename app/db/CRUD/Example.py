from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db.database import db
import app.db.schemas

class ExampleCRUD:
    @staticmethod
    async def create_example(example_data: dict, session: AsyncSession = Depends(db.get_session)) -> app.db.schemas.Example:
        stmt = insert(app.db.schemas.Example).values(**example_data).returning(app.db.schemas.Example)
        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one()

    @staticmethod
    async def get_example_by_id(example_id: int, session: AsyncSession = Depends(db.get_session)) -> app.db.schemas.Example:
        stmt = select(app.db.schemas.Example).where(app.db.schemas.Example.id == example_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()