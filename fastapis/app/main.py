from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from routers import company, meta, user, vessel

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


app.include_router(meta.api, prefix="/meta", tags=["元数据"])
app.include_router(company.api, prefix="/company", tags=["公司"])
app.include_router(user.api, prefix="/user", tags=["用户"])
app.include_router(vessel.api, prefix="/vessel", tags=["船舶"])
