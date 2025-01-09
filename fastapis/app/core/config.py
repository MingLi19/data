from pydantic import MySQLDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_dsn: MySQLDsn = "mysql+pymysql://root:123456@localhost:3306/management_system"

    model_config = SettingsConfigDict(env_file=".env")
