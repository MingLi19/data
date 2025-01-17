import pandas as pd


def load_speed_data(file_path: str) -> pd.DataFrame:
    """从本地路径加载 Excel 文件"""
    df = pd.read_excel(file_path)
    return df[["PCTime", "ShipSpd"]].dropna()
