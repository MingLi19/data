from pydantic import MySQLDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_dsn: MySQLDsn = "mysql+pymysql://root:111222@localhost/management_system"

    model_config = SettingsConfigDict(env_file=".env")
