from pydantic import MongoDsn, MySQLDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_dsn: MySQLDsn | None = "mysql://root:root@localhost:3306/test"
    mongo_dsn: MongoDsn | None = "mongodb://localhost:27017"

    model_config = SettingsConfigDict(env_file=".env")
