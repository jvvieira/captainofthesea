import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import router as api_endpoint_router

from app.config.settings.base import settings


def initialize_backend_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION + " " + settings.ENVIRONMENT,
        openapi_url=settings.OPENAPI_URL,
    )

    origins = ["*"]

    # Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)

    return app


app: fastapi.FastAPI = initialize_backend_application()
