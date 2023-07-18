import fastapi

from backend.api.dependencies.repository import get_repository
from backend.models.schemas.player import PlayerInCreate, PlayerResponse
from backend.crud.player import PlayerCRUDRepository

# from src.securities.authorizations.jwt import jwt_generator
# from src.utilities.exceptions.database import EntityAlreadyExists
# from src.utilities.exceptions.http.exc_400 import (
#     http_exc_400_credentials_bad_signin_request,
#     http_exc_400_credentials_bad_signup_request,
# )

router = fastapi.APIRouter(prefix="/player", tags=["player"])


@router.post(
    "/create",
    name="player:create",
    response_model=PlayerResponse,
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def signup(
    player_create: PlayerInCreate,
    player_repo: PlayerCRUDRepository = fastapi.Depends(
        get_repository(repo_type=PlayerCRUDRepository)
    ),
) -> PlayerResponse:

    new_player = await player_repo.create(player_create=player_create)

    return PlayerResponse(id=new_player.id, name=new_player.name)
