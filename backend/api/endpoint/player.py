import fastapi

from backend.business.entity.player import PlayerInCreate, PlayerResponse
from backend.repository.player import PlayerRepository

router = fastapi.APIRouter(prefix="/player", tags=["player"])


@router.post(
    "/player",
    name="player:create",
    response_model=PlayerResponse,
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def create(
    player: PlayerInCreate,
    repo: PlayerRepository,
) -> PlayerResponse:

    new_player = await repo.create(new_player=player)
    return new_player
