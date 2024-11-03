"""Crear tabla movimientos

Revision ID: bd7c89476a68
Revises: df4393b9cde7
Create Date: 2024-10-31 16:02:35.968141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd7c89476a68'
down_revision: Union[str, None] = 'df4393b9cde7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Movimiento",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.Text, nullable=False),
        sa.Column("tipo", sa.Text, nullable=False),
        sa.Column("power", sa.Integer),
        sa.Column("accuracy", sa.Integer),
        sa.Column("pp", sa.Integer),
        sa.Column("generacion", sa.Text, nullable=False),
        sa.Column("categoria", sa.Text, nullable=False),
        sa.Column("efecto", sa.Text, nullable=False),
        sa.Column("probabilidad_efecto", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("Movimiento")