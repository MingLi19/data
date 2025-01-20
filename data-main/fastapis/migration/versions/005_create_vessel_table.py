"""create vessel table

Revision ID: 005
Revises: 004
Create Date: 2025-01-11 09:52:55.367186

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "005"
down_revision: Union[str, None] = "004"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "vessel",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("mmsi", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("build_date", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("gross_tone", sa.Float(), nullable=False),
        sa.Column("dead_weight", sa.Float(), nullable=False),
        sa.Column("new_vessel", sa.Boolean(), nullable=False),
        sa.Column("hull_clean_date", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("engine_overhaul_date", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("newly_paint_date", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("propeller_polish_date", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=True),
        sa.Column("ship_type_id", sa.Integer(), nullable=True),
        sa.Column("time_zone_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["company_id"],
            ["company.id"],
        ),
        sa.ForeignKeyConstraint(
            ["ship_type_id"],
            ["ship_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["time_zone_id"],
            ["time_zone.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("mmsi"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("vessel")
    # ### end Alembic commands ###
