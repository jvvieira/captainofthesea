import asyncio
import traceback

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from starlette.responses import Response

from app.repository.database import get_async_session

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    description="Description",
    summary="Check Application's health",
)
def healthcheck():
    return {"status": "ok", "message": "Captain of the sea api is up"}


@router.get(
    "/db",
    status_code=status.HTTP_200_OK,
    description="Description",
    summary="Check Application's health",
)
async def db_healthcheck(session: AsyncSession = Depends(get_async_session)):

    try:
        _ = await asyncio.wait_for(session.execute(text("SELECT 1")), timeout=5)
    except Exception:
        print(traceback.format_exc())

        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    content = {"status": "ok", "message": "Captain of the sea database is up"}
    return content
