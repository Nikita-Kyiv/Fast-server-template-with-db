from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

import app.db.schemas

class ExampleCRUD:
    @staticmethod
    async def create_example(session: AsyncSession, example_data: dict) -> app.db.schemas.models:
        stmt = insert(app.db.schemas.models).values(**example_data).returning(app.db.schemas.models)
        result = await session.execute(stmt)
        await session.commit()
        return result.scalar_one()

    @staticmethod
    async def get_example_by_id(session: AsyncSession, example_id: int) -> app.db.schemas.models:
        stmt = select(app.db.schemas.models).where(app.db.schemas.models.id == example_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()