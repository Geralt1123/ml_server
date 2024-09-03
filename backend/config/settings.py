from abc import ABC

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseEnvSettings(BaseSettings):
    """Базовый класс для чтения с поддержкой чтения переменных из окружения"""

    model_config = SettingsConfigDict(case_sensitive=True, env_file_encoding="utf-8")


class UvicornSettings(BaseEnvSettings):
    """параметры запуска сервера"""

    app: str = Field("config.asgi:application")
    port: int = Field(8005, validation_alias="PORT")
    host: str = Field("127.0.0.1", validation_alias="HOST")
    reload: bool = Field(False, validation_alias="DEBUG")
    use_colors: bool = Field(False, validation_alias="DEBUG")


class ApplicationSettings(BaseEnvSettings):
    """Параметры запуска приложения"""

    title: str = Field("SiriusService")
    debug: bool = Field(False, validation_alias="APP_DEBUG")
    prefix: str = Field("/yolo")


class JsonSerializerSettings(BaseEnvSettings):
    date_format: str = Field("%d.%m.%Y")
