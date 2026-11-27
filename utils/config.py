from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс конфигурации тестового фреймворка."""

    base_url: str
    api_url: str
    headless: bool = True
    timeout: int = 10000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
