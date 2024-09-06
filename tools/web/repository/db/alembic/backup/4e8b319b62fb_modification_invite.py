"""modification invite

Revision ID: 4e8b319b62fb
Revises: 15637e2b92c2
Create Date: 2024-03-06 21:18:22.576347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e8b319b62fb'
down_revision: Union[str, None] = '15637e2b92c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('invite_student', sa.Column('active', sa.Boolean(), nullable=True, default=False))

    # Atualiza os valores existentes para terem um valor padrão de False
    op.execute("UPDATE invite_student SET active = FALSE WHERE active IS NULL")

    # Altera a coluna para não permitir valores nulos
    op.alter_column('invite_student', 'active', nullable=False)

def downgrade() -> None:
    pass
