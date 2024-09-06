"""gerate activity

Revision ID: 3172221d2fdb
Revises: 4e8b319b62fb
Create Date: 2024-03-07 21:48:47.759918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3172221d2fdb'
down_revision: Union[str, None] = '4e8b319b62fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'activity',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('category', sa.String(), nullable=False),
        sa.Column('time', sa.DateTime(), nullable=False),
        sa.Column('availability', sa.Boolean(), nullable=False, default=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('list_problem', sa.ARRAY(sa.String()), nullable=False),
        sa.Column('problem_id', sa.String(), nullable=False),
        sa.Column('problem_name', sa.String(), nullable=False),
        sa.Column('problem_slug', sa.String(), nullable=False),
        sa.Column('classroom_id', sa.String(), sa.ForeignKey('classroom.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('activity')
