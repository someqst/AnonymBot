from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr

    DBHOST: SecretStr
    DBUSER: SecretStr
    DBPASS: SecretStr
    DBNAME: SecretStr

    model_config = SettingsConfigDict(
        env_file = '.env',
        env_file_endcoding = 'utf-8'
    )

admins_id = [
    539937958,
]

config = Settings()