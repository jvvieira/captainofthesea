from pydantic import BaseModel


class PlayerInCreate(BaseModel):
    name: str
    email: str


class PlayerResponse(BaseModel):
    id: int
    name: str
    email: str
