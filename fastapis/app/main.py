import logging
import sqlite3
from contextlib import asynccontextmanager
from http import HTTPStatus

from asgi_correlation_id import CorrelationIdFilter, CorrelationIdMiddleware
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse

from app.core.config import Settings
from app.core.error import IntegrityException, NotFoundException
from app.model.response import ResponseModel
from app.router import company, meta, upload, user, vessel, power_speed_curve

settings = Settings()
logger = logging.getLogger(__name__)


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


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    configure_logging()

    yield
    # Shutdown


app = FastAPI(docs_url=None, redoc_url=None, lifespan=lifespan)

app.add_middleware(CorrelationIdMiddleware, header_name="X-ID", transformer=lambda x: x[:8])

# 配置 CORS
origins = ["http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


@app.exception_handler(NotFoundException)
async def not_found_error_handler(request: Request, exc: NotFoundException) -> ResponseModel:
    logger.error(f"Not-Found error: request={request}, exc={exc}")
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={
            "code": HTTPStatus.NOT_FOUND,
            "data": None,
            "message": exc.detail,
        },
    )


@app.exception_handler(IntegrityException)
async def integrity_error_handler(request: Request, exc: IntegrityException) -> ResponseModel:
    logger.error(f"Integrity error: request={request}, exc={exc}")
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={
            "code": HTTPStatus.BAD_REQUEST,
            "data": None,
            "message": exc.detail,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"Validation error: request={request}, exc={exc}")
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={
            "code": HTTPStatus.BAD_REQUEST,
            "data": None,
            "message": exc.errors(),
        },
    )


app.include_router(meta.api, prefix="/meta", tags=["元数据"])
app.include_router(company.api, prefix="/company", tags=["公司"])
app.include_router(user.api, prefix="/user", tags=["用户"])
app.include_router(vessel.api, prefix="/vessel", tags=["船舶"])
app.include_router(upload.api, prefix="/upload", tags=["上传"])
app.include_router(power_speed_curve.api, prefix="/power-speed-curve", tags=["功率-速度曲线"])
