"""insert meta data

Revision ID: 792c57a87730
Revises: f92875c2b496
Create Date: 2024-12-22 10:35:15.932156

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "792c57a87730"
down_revision: Union[str, None] = "f92875c2b496"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO fuel_type (name_cn, name_en, name_abbr, cf) VALUES
            ('重燃油 (HFO) 硫含量高于0.5% m/m', 'HFO, S>0.5% m/m', 'HFO-HS', 3.114),
            ('重燃油 (HFO) 硫含量不高于0.1% m/m, 但不高于0.5% m/m', 'HFO, 0.1% m/m<=S<=0.5% m/m', 'HFO-LS', 3.114),
            ('重燃油 (HFO) 硫含量不高于0.1% m/m', 'HFO, S<=0.1% m/m', 'HFO-ULS', 3.114),
            ('轻燃油 (LFO) 硫含量高于0.5% m/m', 'LFO, S>0.5% m/m', 'LFO-HS', 3.151),
            ('轻燃油 (LFO) 硫含量不高于0.1% m/m, 但不高于0.5% m/m', 'LFO, 0.1% m/m<=S<=0.5% m/m', 'LFO-LS', 3.151),
            ('轻燃油 (LFO) 硫含量不高于0.1% m/m', 'LFO, S<=0.1% m/m', 'LFO-ULS', 3.151),
            ('船用柴油', 'MDO/MGO', 'MDO/MGO', 3.206),
            ('内河船用燃料油', 'MDO/MGO for River Boat', 'MDO/MGO', 3.206),
            ('液化石油气 (LPG) 丙烷', 'LPG-Propane', 'LPG-Propane', 3.000),
            ('液化石油气 (LPG) 丁烷', 'LPG-Butane', 'LPG-Butane', 3.030),
            ('液化天然气 (LNG)', 'Liquefied Natural Gas (LNG)', 'LNG', 2.750),
            ('甲醇', 'Methanol', 'Methanol', 1.375),
            ('乙醇', 'Ethanol', 'Ethanol', 1.913),
            ('乙烷', 'Ethane', 'Ethane', 2.927),
            ('氨', 'Ammonia', 'Ammonia', 0),
            ('氢', 'Hydrogen', 'Hydrogen', 0);
        """
    )

    op.execute(
        """
        INSERT INTO ship_type (code, name_cn, name_en) VALUES 
            ('I001', '散货船', 'Bulk carrier'),
            ('I002', '气体运输船', 'Gas carrier'),
            ('I003', '液货船', 'Tanker'),
            ('I004', '集装箱船', 'Container ship'),
            ('I005', '杂货船', 'General cargo ship'),
            ('I006', '冷藏货船', 'Refrigerated cargo carrier'),
            ('I007', '兼用船', 'Combination carrier'),
            ('I008', 'LNG运输船', 'LNG carrier'),
            ('I009', '滚装货船（车辆运输船）', 'Ro-ro cargo ship (vehicle carrier)'),
            ('I010', '滚装货船', 'Ro-ro cargo ship'),
            ('I011', '客滚船', 'Ro-ro passenger ship'),
            ('I011.1', '客滚船(高速)', 'Ro-ro passenger ship (high-speed craft)'),
            ('I012', '豪华邮轮', 'Cruise passenger ship');
        """
    )

    op.execute(
        """
        INSERT INTO time_zone (name_cn, name_en, explaination) VALUES
            ('零时区', 'UTC+0', '零时区 7.5° W～7.5° E 0°'),
            ('东一区', 'UTC+1', '东一区 7.5° E～22.5° E 15° E'),
            ('东二区', 'UTC+2', '东二区 22.5° E～37.5° E 30° E'),
            ('东三区', 'UTC+3', '东三区 37.5° E～52.5° E 45° E'),
            ('东四区', 'UTC+4', '东四区 52.5° E～67.5° E 60° E'),
            ('东五区', 'UTC+5', '东五区 67.5° E～82.5° E 75° E'),
            ('东六区', 'UTC+6', '东六区 82.5° E～97.5° E 90° E'),
            ('东七区', 'UTC+7', '东七区 97.5° E～112.5° E 105° E'),
            ('东八区', 'UTC+8', '东八区 112.5° E～127.5° E 120° E'),
            ('东九区', 'UTC+9', '东九区 127.5° E～142.5° E 135° E'),
            ('东十区', 'UTC+10', '东十区 142.5° E～157.5° E 150° E'),
            ('东十一区', 'UTC+11', '东十一区 157.5° E～172.5° E 165° E'),
            ('东十二区', 'UTC+12', '东十二区 172.5° E～180° E 180°'),
            ('西一区', 'UTC-1', '西一区 7.5° W～22.5° W 15° W'),
            ('西二区', 'UTC-2', '西二区 22.5° W～37.5° W 30° W'),
            ('西三区', 'UTC-3', '西三区 37.5° W～52.5° W 45° W'),
            ('西四区', 'UTC-4', '西四区 52.5° W～67.5° W 60° W'),
            ('西五区', 'UTC-5', '西五区 67.5° W～82.5° W 75° W'),
            ('西六区', 'UTC-6', '西六区 82.5° W～97.5° W 90° W'),
            ('西七区', 'UTC-7', '西七区 97.5° W～112.5° W 105° W'),
            ('西八区', 'UTC-8', '西八区 112.5° W～127.5° W 120° W'),
            ('西九区', 'UTC-9', '西九区 127.5° W～142.5° W 135° W'),
            ('西十区', 'UTC-10', '西十区 142.5° W～157.5° W 150° W'),
            ('西十一区', 'UTC-11', '西十一区 157.5° W～172.5° W 165° W'),
            ('西十二区', 'UTC-12', '西十二区 172.5° W～180° W 180°');
            """
    )


def downgrade() -> None:
    pass
