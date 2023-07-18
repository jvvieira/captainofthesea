import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from backend.crud.base import BaseCRUDRepository

from backend.models.db.player import Player
from backend.models.schemas.player import PlayerInCreate


class PlayerCRUDRepository(BaseCRUDRepository):
    async def create(self, player_create: PlayerInCreate) -> Player:
        new_player = Player(username=player_create.name)

        self.async_session.add(instance=new_player)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_player)

        return new_player

    async def read_all(self) -> typing.Sequence[Player]:
        stmt = sqlalchemy.select(Player)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_by_id(self, id: int) -> Player:
        stmt = sqlalchemy.select(Player).where(Player.id == id)
        query = await self.async_session.execute(statement=stmt)

        return query.scalar()  # type: ignore
