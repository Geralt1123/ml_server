from dependency_injector import containers, providers
from common.serialization import JsonSerializer, JsonDeserializer
from web.api.containers.predict import PredictControllerContainer


class ControllersContainer(containers.DeclarativeContainer):
    """Заранее сконфигурированный контейнер контроллеров"""

    config = providers.Configuration()
    json_serializer = providers.Dependency(instance_of=JsonSerializer)
    json_deserializer = providers.Dependency(instance_of=JsonDeserializer)

    sub_containers = providers.Dict(
        files=providers.Container(
            PredictControllerContainer),
    )
