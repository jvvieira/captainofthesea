import datetime

from sqlmodel import Field, SQLModel

from backend.repository.table import BaseDBModel, TrackingModel


class PlayerBase(BaseDBModel):
    name: str = Field(max_length=120, nullable=False)


class PlayerModel(PlayerBase, TrackingModel, table=True):
    __tablename__ = "player"
