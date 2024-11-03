"""Crear tabla integrante pokemon

Revision ID: d8a0547e92d2
Revises: cbbe9b73afda
Create Date: 2024-10-31 11:03:24.924653

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d8a0547e92d2"
down_revision: Union[str, None] = "cbbe9b73afda"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear tabla para Integrante_pokemon
    op.create_table(
        "integrante_pokemon",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("pokemon_id", sa.Integer(), nullable=False),
        sa.Column("naturaleza_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pokemon_id"],
            ["pokemon.pokemon_id"],
        ),
        sa.ForeignKeyConstraint(
            ["naturaleza_id"],
            ["Naturaleza.id"],
        ),
    )

    # Crear tabla de relación para movimientos de Integrante_pokemon (si no existe)
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
    op.drop_table("integrante_pokemon")
