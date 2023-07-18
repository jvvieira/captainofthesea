from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, SecretStr, validator

from app import _version_


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Account API"
    APP_VERSION: str = _version_
    APP_DESCRIPTION: str = "Account service"

    # Database
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_URI: Optional[PostgresDsn] = None

    # Logging
    # ELASTIC_APM_ENVIRONMENT: str = 'uat'
    # ELASTIC_APM_SERVER_URL: HttpUrl
    # ELASTIC_APM_API_KEY: SecretStr

    @validator("POSTGRES_URI", pre=True)
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
