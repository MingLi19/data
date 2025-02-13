import logging
from contextlib import asynccontextmanager
from http import HTTPStatus

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse

from app.core.config import Settings
from app.core.doc import tags_metadata
from app.core.error import IntegrityException, NotFoundException
from app.core.log import configure_logging
from app.model.response import ResponseModel
from app.router import company, meta, power_speed_curve, upload, user, vessel

settings = Settings()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    configure_logging()

    yield
    # Shutdown


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan,
    openapi_tags=tags_metadata,
)

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
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
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
app.include_router(company.api, prefix="/companies", tags=["公司"])
app.include_router(user.api, prefix="/users", tags=["用户"])
app.include_router(vessel.api, prefix="/vessel", tags=["船舶"])
app.include_router(upload.api, prefix="/upload", tags=["上传"])
app.include_router(power_speed_curve.api, prefix="/power-speed-curve", tags=["功率-速度曲线"])
