import fastapi

from app.api.dependencies.repository import get_repository
from app.models.schemas.player import PlayerInCreate, PlayerResponse
from app.crud.player import PlayerCRUDRepository

player_router = fastapi.APIRouter(prefix="/player", tags=["player"])


@player_router.post(
    "/create",
    name="player:create",
    response_model=PlayerResponse,
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def create(
    player_create: PlayerInCreate,
    player_repo: PlayerCRUDRepository = fastapi.Depends(
        get_repository(repo_type=PlayerCRUDRepository)
    ),
) -> PlayerResponse:

    new_player = await player_repo.create(player_create=player_create)

    return PlayerResponse(id=new_player.id, name=new_player.name)
