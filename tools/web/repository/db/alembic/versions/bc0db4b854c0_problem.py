"""problem

Revision ID: bc0db4b854c0
Revises: 7d4e700c3ef9
Create Date: 2024-02-23 17:41:53.640772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc0db4b854c0'
down_revision: Union[str, None] = '7d4e700c3ef9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
        
    op.create_table(
        'problem',
        sa.Column('id', sa.String(50), primary_key=True),
        sa.Column('list_name', sa.String(50), nullable=False),
        sa.Column('list_problem', sa.ARRAY(sa.String), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('slug', sa.String(50), nullable=False),
        sa.Column('comentary', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('problem')
