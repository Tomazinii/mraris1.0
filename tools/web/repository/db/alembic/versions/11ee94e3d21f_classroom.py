"""classroom

Revision ID: 11ee94e3d21f
Revises: 1c6e7f655ae1
Create Date: 2024-03-04 16:36:30.522276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11ee94e3d21f'
down_revision: Union[str, None] = '1c6e7f655ae1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'classroom',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('class_name', sa.String(), nullable=False),
        sa.Column('teacher_name', sa.String(), nullable=False),
        sa.Column('teacher_id', sa.String(), nullable=False),
        sa.Column('teacher_created', sa.DateTime(), nullable=False),
        sa.Column('teacher_updated', sa.DateTime(), nullable=False),
        sa.Column('teacher_email', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('classroom')
