"""<message>

Revision ID: c4424b3c5e05
Revises: 2012288dffc4
Create Date: 2025-01-16 16:30:55.689253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4424b3c5e05'
down_revision: Union[str, None] = '2012288dffc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
