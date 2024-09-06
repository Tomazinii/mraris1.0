"""create link password table

Revision ID: 2f30ec871c37
Revises: 320538216497
Create Date: 2024-05-11 23:24:43.669605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f30ec871c37'
down_revision: Union[str, None] = '320538216497'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'link_password',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('to', sa.String(), nullable=False),
        sa.Column('time_expires', sa.DateTime(), nullable=False),
        sa.Column('active', sa.Boolean(), nullable=False, default=False),
    )



def downgrade() -> None:
    pass
