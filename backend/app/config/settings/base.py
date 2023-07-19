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

    POSTGRES_HOST: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_DB: str

    DB_POSTGRES_URI: Optional[PostgresDsn] = None

    @validator("DB_POSTGRES_URI", pre=True)
    def validate_postgres_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> str:
        if isinstance(v, str):
            return v

        password: SecretStr = values.get("POSTGRES_PASSWORD", SecretStr(""))

        return "{scheme}://{user}:{password}@{host}:{port}/{db}".format(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=password.get_secret_value(),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            db=values.get("POSTGRES_DB"),
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
