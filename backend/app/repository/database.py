from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings.base import settings


async_engine = create_async_engine(settings.DB_POSTGRES_URI, echo=True, future=True)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=True
    )

    async with async_session() as session:
        yield session
