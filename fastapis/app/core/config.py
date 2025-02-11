from pydantic import MongoDsn, MySQLDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_dsn: MySQLDsn
    mongo_dsn: MongoDsn

    model_config = SettingsConfigDict(env_file=".env")
