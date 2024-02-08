from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    bot_token: SecretStr
    payment_token_test: SecretStr
    database_connector: SecretStr
    oxapay_merchant_key: SecretStr
    admin_id: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

config = Settings()