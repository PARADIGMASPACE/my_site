import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    DEBUG: bool = os.getenv("DEBUG")
    HOST: str = os.getenv("HOST")
    PORT: int = os.getenv("PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
