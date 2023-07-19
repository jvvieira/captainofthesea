from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.repository.database import get_async_session


class BaseCRUDRepository:
    def __init__(self, async_session: AsyncSession = Depends(get_async_session)):
        self.async_session = async_session
