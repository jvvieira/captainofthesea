import fastapi

from app.api.routes.v1.player import player_router

router = fastapi.APIRouter()

router.include_router(router=player_router)
