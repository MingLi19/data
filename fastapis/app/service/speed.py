import io

import matplotlib

matplotlib.use("Agg")  # 设置为Agg后端

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd
from fastapi.responses import StreamingResponse

LOCAL_FILE_PATH = "scripts/副本八打雁202307.xlsx"
# 设置matplotlib使用中文字体
font_path = "C:/Windows/Fonts/simsun.ttc"  # 中文字体路径
prop = fm.FontProperties(fname=font_path)

# 配置全局字体
plt.rcParams["font.family"] = prop.get_name()
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示为方块的问题


def load_speed_data(file_path: str):
    """加载航速数据并限制返回前 1000 行"""
    df = pd.read_excel(file_path)  # 加载 Excel 文件
    # 只返回前 1000 行，否则数据量太大加载很慢，后续改成读取数据库数据应该可以解决此问题
    return df.head(1000)


def generate_speed_histogram() -> StreamingResponse:
    """生成并返回航速直方图"""
    df = load_speed_data(LOCAL_FILE_PATH)
    speed_data = df["ShipSpd"]

    plt.figure(figsize=(6, 4))
    plt.hist(speed_data, bins=30, color="blue", alpha=0.7)
    plt.title("航速直方图")
    plt.xlabel("航速")
    plt.ylabel("频数")

    img_io = io.BytesIO()
    plt.savefig(img_io, format="png")
    img_io.seek(0)
    plt.close()

    return StreamingResponse(img_io, media_type="image/png")


def generate_speed_scatter() -> StreamingResponse:
    """生成并返回航速散点图"""
    df = load_speed_data(LOCAL_FILE_PATH)
    speed_data = df["ShipSpd"]
    time_data = df["PCTime"]

    # 采样每隔100个数据点
    sampled_speed_data = speed_data[::100]
    sampled_time_data = time_data[::100]

    plt.figure(figsize=(12, 4))
    plt.scatter(sampled_time_data, sampled_speed_data, color="green", alpha=0.5)
    plt.title("航速散点图")
    plt.xlabel("时间")
    plt.ylabel("航速")

    img_io = io.BytesIO()
    plt.savefig(img_io, format="png")
    img_io.seek(0)
    plt.close()

    return StreamingResponse(img_io, media_type="image/png")
