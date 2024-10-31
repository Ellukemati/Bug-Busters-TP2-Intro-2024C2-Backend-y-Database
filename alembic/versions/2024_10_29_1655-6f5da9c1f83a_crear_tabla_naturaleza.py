"""Crear tabla naturaleza


Revision ID: 6f5da9c1f83a
Revises: 
Create Date: 2024-10-29 16:55:57.019779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f5da9c1f83a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Naturaleza',
        sa.Column('id', sa.INTEGER, primary_key=True),
        sa.Column('nombre', sa.TEXT, nullable=False),
        sa.Column('aumenta_estadistica', sa.TEXT, nullable=False),
        sa.Column('reduce_estadistica', sa.TEXT, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('Naturaleza')
