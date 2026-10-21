from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    """application loaded from env variable"""

    app_name: str = "EduMore"
    version:str = "0.1.0"
    debug:bool = False

    database_url:str= Field(
        "",
        description="Secrets used sign action token"
    )
    access_token_expire_minute:int = Field(default=15, gt = 0)
    refresh_token_expire_days:int = Field(default=15, gt = 0)

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


@lru_cache
def get_settings()-> Settings:
    return Settings()
