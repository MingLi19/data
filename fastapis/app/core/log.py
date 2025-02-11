import logging
import sqlite3

from asgi_correlation_id import CorrelationIdFilter


class DatabaseHandler(logging.Handler):
    def __init__(self, db_file):
        super().__init__()
        self.db_file = db_file
        # 创建数据库表（如果不存在）
        conn = sqlite3.connect(self.db_file)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level TEXT,
            message TEXT
        )
        """)
        conn.commit()
        conn.close()

    def emit(self, record):
        conn = sqlite3.connect("self.db_file")
        conn.execute(
            """
        INSERT INTO logs (level,correlation_id,asctime, message) VALUES (?, ?, ?, ?)
        """,
            (record.levelname, record.correlation_id, record.asctime, record.getMessage()),
        )
        conn.commit()
        conn.close()


# Configure logging
def configure_logging():
    cid_filter = CorrelationIdFilter(uuid_length=8)
    console_handler = logging.StreamHandler()
    console_handler.addFilter(cid_filter.filter)
    file_handler = logging.FileHandler("app.log")
    file_handler.addFilter(cid_filter.filter)
    database_handler = DatabaseHandler("logs.db")
    database_handler.addFilter(cid_filter.filter)

    logging.basicConfig(
        level=logging.INFO,
        handlers=[console_handler, file_handler],
        format="%(levelname)s: \t [%(correlation_id)s] %(asctime)s | %(message)s",
    )
    logging.basicConfig(
        level=logging.ERROR,
        handlers=[database_handler],
        format="%(levelname)s: \t [%(correlation_id)s] %(asctime)s | %(message)s",
    )
