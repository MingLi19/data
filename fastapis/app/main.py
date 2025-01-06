import logging
from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse

from app.core.error import IntegrityException, NotFoundException
from app.model.response import ResponseModel
from app.router import company, meta, user, vessel

app = FastAPI(docs_url=None, redoc_url=None)

logger = logging.getLogger(__name__)


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
