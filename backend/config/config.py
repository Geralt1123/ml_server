from config.settings import (
    ApplicationSettings,
    UvicornSettings,
    JsonSerializerSettings
)

uvicorn_config = UvicornSettings()
application_config = ApplicationSettings()
json_serializer_config = JsonSerializerSettings()