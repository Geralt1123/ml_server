from boto3 import resource
from boto3.session import Config as S3Config

from dependency_injector import containers, providers
from common.serialization import JsonDeserializer, JsonSerializer
from config.config import (
    json_serializer_config,
)
from common.app_lifespan import ApplicationLifeSpan

from web.api.containers import ControllersContainer as ApiControllersContainer


class ApplicationContainer(containers.DeclarativeContainer):
    """Общий контейнер сервиса"""

    config = providers.Configuration()

    json_serializer = providers.Singleton(JsonSerializer, **json_serializer_config.model_dump())
    json_deserializer = providers.Singleton(JsonDeserializer, **json_serializer_config.model_dump())

    web = providers.Container(
        ApiControllersContainer,
        json_serializer=json_serializer,
        json_deserializer=json_deserializer,
    )
