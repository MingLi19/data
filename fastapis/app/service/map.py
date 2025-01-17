from datetime import date
from typing import List

import folium
import pandas as pd

from app.model.location import Location


# 解析带方向的经纬度字符串，返回数字
def parse_lat_lon(value: str) -> float:
    """解析经纬度字符串，将方向转为数字"""
    if isinstance(value, str):
        # 提取数字和方向
        direction = value[-1]
        value = value[:-1].strip()  # 获取数字部分

        try:
            # 转换为浮动数值
            num_value = float(value)
            # 根据方向调整符号
            if direction in ["S", "W"]:
                num_value = -num_value
            return num_value
        except ValueError:
            raise ValueError(f"Invalid latitude/longitude value: {value}")
    else:
        raise ValueError(f"Invalid input type for latitude/longitude: {value}")


def read_locations_from_excel(file_path: str) -> List[Location]:
    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 将 PCDate 转换为日期类型
    df["PCDate"] = pd.to_datetime(df["PCDate"]).dt.date

    # 解析经纬度
    df["latitude"] = df["Latitude"].apply(parse_lat_lon)
    df["longitude"] = df["Longitude"].apply(parse_lat_lon)

    # 转换为 Location 对象列表
    locations = [
        Location(PCDate=row["PCDate"], latitude=row["latitude"], longitude=row["longitude"]) for _, row in df.iterrows()
    ]

    return locations


def create_map(locations: List[Location], target_date: date) -> str:
    # 根据日期过滤数据，确保每个日期有一个唯一的点
    filtered_locations = [loc for loc in locations if loc.PCDate == target_date]

    if not filtered_locations:
        return "<h3>No data available for the selected date</h3>"

    # 选择当天的第一个位置（如果有多个）
    location = filtered_locations[0]

    # 创建 folium 地图对象，设置初始视角
    m = folium.Map(location=[location.latitude, location.longitude], zoom_start=10)

    # 在地图上添加当天的标记
    folium.Marker(
        location=[location.latitude, location.longitude],
        popup=f"Date: {location.PCDate}",
    ).add_to(m)

    # 将 folium 地图保存为 HTML 字符串
    return m._repr_html_()
