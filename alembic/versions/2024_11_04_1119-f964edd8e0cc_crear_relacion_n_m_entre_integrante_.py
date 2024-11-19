
"""Crear relacion N M entre integrante pokemon y movimientos

Revision ID: f964edd8e0cc
Revises: 32a30a156131
Create Date: 2024-11-04 11:19:16.570662

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f964edd8e0cc"
down_revision: Union[str, None] = "32a30a156131"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "integrante_movimiento_link",
        sa.Column("integrante_id", sa.Integer(), nullable=False),
        sa.Column("movimiento_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["integrante_id"],
            ["integrante_pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["movimiento_id"],
            ["movimiento.id"],
        ),
        sa.PrimaryKeyConstraint("integrante_id", "movimiento_id"),
    )


def downgrade() -> None:
    op.drop_table("integrante_movimiento_link")