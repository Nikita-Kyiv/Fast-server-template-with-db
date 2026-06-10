import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.main import create_app
from app.db.database import db
from app.db.schemas import models


@pytest_asyncio.fixture(scope="session")
async def app():
    app = create_app()
    async with db.engine.begin() as conn:
        await conn.run_sync(models.metadata.create_all)
    yield app
    await db.close_as_engine()


@pytest_asyncio.fixture
async def async_client(app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
