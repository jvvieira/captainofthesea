import logging
import pathlib

from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, SecretStr, validator, BaseConfig
from app.config.settings.environment import Environment

ROOT_DIR: pathlib.Path = pathlib.Path(
    __file__
).parent.parent.parent.parent.parent.resolve()


class Settings(BaseSettings):
    TITLE: str = "Captain of the Sea"
    DESCRIPTION: str = "Captain of the sea backend"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""
    ENVIRONMENT: Environment = Environment.DEVELOPMENT

    DB_POSTGRES_HOST: str
    DB_POSTGRES_PASSWORD: SecretStr
    DB_POSTGRES_PORT: int
    DB_POSTGRES_USENRAME: str
    DB_POSTGRES_SCHEMA: str

    DB_POSTGRES_URI: Optional[PostgresDsn] = None

    @validator("DB_POSTGRES_URI", pre=True)
    def validate_postgres_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> str:
        if isinstance(v, str):
            return v

        password: SecretStr = values.get("DB_POSTGRES_PASSWORD", SecretStr(""))

        return "{scheme}://{user}:{password}@{host}:{port}/{db}".format(
            scheme="postgresql+asyncpg",
            user=values.get("DB_POSTGRES_USENRAME"),
            password=password.get_secret_value(),
            host=values.get("DB_POSTGRES_HOST"),
            port=values.get("DB_POSTGRES_PORT"),
            db=values.get("DB_POSTGRES_SCHEMA"),
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
