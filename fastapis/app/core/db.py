from sqlmodel import Session, create_engine

from .config import Settings

settings = Settings()

DATABASE_URL = settings.mysql_dsn.unicode_string()

if DATABASE_URL is not None:
    engine = create_engine(DATABASE_URL, echo=True)
else:
    raise ValueError("Database URL is not provided.")


def get_db_session():
    with Session(engine) as session:
        yield session
