"""create equipment table

Revision ID: 006
Revises: 005
Create Date: 2025-01-11 09:53:35.971473

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "006"
down_revision: Union[str, None] = "005"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "equipment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("type", sa.Enum("me", "dg", "blr", name="equipmenttype"), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("vessel_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["vessel_id"],
            ["vessel.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("equipment")
    # ### end Alembic commands ###
