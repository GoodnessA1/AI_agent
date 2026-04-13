from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Setting(BaseSettings):
    model_config = SettingsConfigDict(
            env_file='.en.env',
            env_file_encoding='utf-8',
            case_sensitive=True
            )

    name: str = Field(min_length=5)
    password: str = Field(min_length=8)
    url: str
