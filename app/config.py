import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "local"
    DATABASE_URL: str | None = None
    OPENAI_API_KEY: str | None = None  # pour plus tard si tu veux un LLM

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

# Fallback local si pas de DATABASE_URL définie
if not settings.DATABASE_URL:
    settings.DATABASE_URL = "sqlite:///./local.db"
