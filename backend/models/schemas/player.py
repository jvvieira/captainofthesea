import datetime

import pydantic

from backend.models.schemas.base import BaseSchemaModel


class PlayerInCreate(BaseSchemaModel):
    name: str


class PlayerResponse(BaseSchemaModel):
    id: int
    name: str
