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
    pass

    # Atualiza os valores existentes para terem um valor padrão de False

    # Altera a coluna para não permitir valores nulos

def downgrade() -> None:
    pass
