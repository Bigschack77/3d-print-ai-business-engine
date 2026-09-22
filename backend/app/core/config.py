from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "3D Print AI Business Engine"
    environment: str = "development"
    database_url: str = "sqlite:///./app.db"
    redis_url: str = "redis://localhost:6379/0"
    openai_api_key: str = ""
    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""
    app_url: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
