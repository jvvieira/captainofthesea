import datetime

from sqlmodel import Field, SQLModel
from sqlalchemy import text
from typing import Optional


class BaseDBModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)


class TrackingModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": text("current_timestamp(0)")},
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)"),
        },
    )
