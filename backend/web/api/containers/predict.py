from dependency_injector import containers, providers
from web.api.controllers import PredictController, PredictControllerTwo


class PredictControllerContainer(containers.DeclarativeContainer):
    """Заранее сконфигурированный контейнер для экспорта в Excel"""

    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=["web.api.views.predict"], auto_wire=False
    )

    predict_file_controller = providers.Factory(
        PredictController
    )

    predict_file_controller_2 = providers.Factory(
        PredictControllerTwo
    )
