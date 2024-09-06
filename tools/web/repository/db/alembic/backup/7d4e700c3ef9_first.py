"""first

Revision ID: 7d4e700c3ef9
Revises: 2cd4a457c7d8
Create Date: 2024-02-23 11:19:00.807958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d4e700c3ef9'
down_revision: Union[str, None] = '2cd4a457c7d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'article',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),

    )


def downgrade() -> None:
    op.drop_table('article')
