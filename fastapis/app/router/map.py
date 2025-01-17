from datetime import date

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Template

from app.service.map import create_map, read_locations_from_excel

api = APIRouter()

# Excel 文件路径
EXCEL_FILE_PATH = "scripts/副本八打雁202307.xlsx"


@api.get("/", response_class=HTMLResponse)
async def get_map(target_date: date):
    # 从 Excel 文件读取位置(纬度、经度）数据
    locations = read_locations_from_excel(EXCEL_FILE_PATH)

    # 调用服务层生成地图
    map_html = create_map(locations, target_date)

    # 使用 Jinja2 模板渲染 HTML 页面
    template = Template("""
    <html>
        <head><title>Map for Date: {{ target_date }}</title></head>
        <body>
            <h2>Map for Date: {{ target_date }}</h2>
            {{ map_html|safe }}
        </body>
    </html>
    """)

    # 返回渲染后的 HTML 响应
    return HTMLResponse(content=template.render(map_html=map_html, target_date=target_date))
