import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions
from backend.business.entity.player import PlayerInCreate
from backend.repository import BaseRepository


class PlayerRepository(BaseRepository):
    async def create(self, new_player: PlayerInCreate) -> Player:

        self.async_session.add(instance=new_player)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_player)

        return new_player
