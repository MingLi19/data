from sqlmodel import Session, create_engine

from .config import Settings

settings = Settings()

if settings.mysql_dsn is not None:
    engine = create_engine(settings.mysql_dsn.unicode_string(), echo=True)
else:
    raise ValueError("Database URL is not provided.")


class MySQLManger:
    def __init__(self, engine):
        self.engine = Session(engine)

    def __enter__(self):
        return self.engine

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.engine.close()


def get_mysql_db_session():
    with MySQLManger(engine) as session:
        yield session
