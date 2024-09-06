"""create account table


Revision ID: 2cd4a457c7d8
Revises: 
Create Date: 2024-02-22 17:28:45.410807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cd4a457c7d8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'account',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(50), nullable=False),
    sa.Column('description', sa.Unicode(200)),
)


def downgrade() -> None:
    op.drop_table('account')
