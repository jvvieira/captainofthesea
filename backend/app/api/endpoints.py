import fastapi

from app.api.routes.v1.player import player_router
from app.api.routes.health import router as health_router

router = fastapi.APIRouter()

router.include_router(router=player_router)
router.include_router(router=health_router)
