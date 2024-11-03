"""Crear tabla equipos

Revision ID: 4dab2591f953
Revises: 
Create Date: 2024-10-31 12:42:20.823854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4dab2591f953'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Equipo',
        sa.Column('id_equipo', sa.INTEGER, primary_key=True),
        sa.Column('nombre', sa.TEXT, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('Equipo')
