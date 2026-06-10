import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    service_name: str = "service"
    service_version: str = "0.0.1"
    debug: bool = False

    db_dsn: str = "sqlite+aiosqlite:///app/db/service.db"
    test_db_dsn: str = "sqlite+aiosqlite:///app/db/service.db"


settings = Settings()
