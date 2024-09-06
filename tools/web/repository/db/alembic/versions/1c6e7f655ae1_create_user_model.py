"""create user model

Revision ID: 1c6e7f655ae1
Revises: bc0db4b854c0
Create Date: 2024-02-29 20:52:00.462664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c6e7f655ae1'
down_revision: Union[str, None] = 'bc0db4b854c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.String(50), primary_key=True),
        sa.Column('username', sa.String(200), nullable=False),
        sa.Column('password', sa.String(200), nullable=False),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('is_super_user', sa.Boolean(), nullable=False),
        sa.Column('is_authenticated', sa.Boolean(), nullable=False),
        sa.Column('is_admin', sa.Boolean(), nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('user_type', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
