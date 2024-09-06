"""result activity model

Revision ID: b70901558751
Revises: 3172221d2fdb
Create Date: 2024-03-18 09:46:26.694299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b70901558751'
down_revision: Union[str, None] = '3172221d2fdb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'result_activity_model',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('classroom_id', sa.String(), nullable=False),
        sa.Column('activity_id', sa.String(), nullable=False),
        sa.Column('student_name', sa.String(), nullable=False),
        sa.Column('student_id', sa.String(), nullable=False),
        sa.Column('student_enrollment', sa.String(), nullable=False),
        sa.Column('student_email', sa.String(), nullable=False),
        sa.Column('time_mrplato', sa.Interval(), nullable=False),
        sa.Column('num_attempts', sa.Integer(), nullable=False),
        sa.Column('num_backs', sa.Integer(), nullable=False),
        sa.Column('num_errors', sa.Integer(), nullable=False),
        sa.Column('problem_id', sa.Integer(), nullable=False),
        sa.Column('problem', sa.String(), nullable=False),
        sa.Column('solution', sa.ARRAY(sa.String()), nullable=False),
        sa.Column('activity_category', sa.String(), nullable=True, default=False),
        sa.Column('time_activity_expires', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
        op.drop_table('result_activity_model')

