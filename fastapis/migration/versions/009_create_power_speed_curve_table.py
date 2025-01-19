"""create power_speed_curve table

Revision ID: 009
Revises: 008
Create Date: 2025-01-19 14:21:10.396333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '009'
down_revision: Union[str, None] = '008'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'power_speed_curve',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('speed_water', sa.Float(), nullable=False),
        sa.Column('me_power', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('vessel_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['vessel_id'], ['vessel.id'], ),
    )


def downgrade() -> None:
    op.drop_table('power_speed_curve')



