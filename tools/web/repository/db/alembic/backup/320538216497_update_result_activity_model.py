"""update result activity model

Revision ID: 320538216497
Revises: b70901558751
Create Date: 2024-03-19 08:56:02.984612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '320538216497'
down_revision: Union[str, None] = 'b70901558751'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('result_activity_model', sa.Column('activity_category', sa.String(), nullable=True, default=False))


    # Altera a coluna para não permitir valores nulos


def downgrade() -> None:
    pass
