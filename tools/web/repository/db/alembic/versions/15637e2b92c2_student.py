"""student

Revision ID: 15637e2b92c2
Revises: 8f27e518c3cb
Create Date: 2024-03-06 18:31:36.749528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15637e2b92c2'
down_revision: Union[str, None] = '8f27e518c3cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'student',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('enrollment', sa.String(), nullable=False),
        sa.Column('classroom_id', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
    op.drop_table('student')
