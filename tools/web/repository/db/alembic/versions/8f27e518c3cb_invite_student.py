"""invite student

Revision ID: 8f27e518c3cb
Revises: 11ee94e3d21f
Create Date: 2024-03-04 16:41:01.715461

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f27e518c3cb'
down_revision: Union[str, None] = '11ee94e3d21f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
        op.create_table(
        'invite_student',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('to', sa.String(), nullable=False),
        sa.Column('time_expires', sa.DateTime(), nullable=False),
        sa.Column('active', sa.Boolean(), nullable=False, default=False),
        sa.Column('classroom_id', sa.String(), sa.ForeignKey('classroom.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('invite_student')

