import datetime

import pydantic

from app.models.schemas.base import BaseSchemaModel


class PlayerInCreate(BaseSchemaModel):
    name: str


class PlayerResponse(BaseSchemaModel):
    id: int
    name: str
