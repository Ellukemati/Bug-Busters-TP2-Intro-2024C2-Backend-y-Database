"""Crear tabla Movimientos

Revision ID: cbbe9b73afda
Revises: 
Create Date: 2024-10-29 12:04:22.075826

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cbbe9b73afda"
down_revision: Union[str, None] = None
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
        sa.Column("pp", sa.Integer, nullable=False),
        sa.Column("generacion", sa.Text, nullable=False),
        sa.Column("categoria", sa.Text, nullable=False),
        sa.Column("efecto", sa.Text, nullable=False),
        sa.Column("probabilidad_efecto", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("Movimiento")
