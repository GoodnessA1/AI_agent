from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Annotated

class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
            env_file = ".env",
            env_file_encoding = "utf-8",
            case_sensitive = True,
            extra="forbid"
            )

    username: str = Field(min_length = 5)
    password: str = Field(min_length = 8)
