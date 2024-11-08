"""Creación de tabla de Pokemon y tabla intermedia entre Pokemon y Movimiento

Revision ID: 25d8e8b1052c
Revises: badc6a43c32f
Create Date: 2024-11-04 19:35:11.774815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "25d8e8b1052c"
down_revision: Union[str, None] = "badc6a43c32f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pokemon",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.Text, nullable=False),
        sa.Column("url_imagen", sa.Text, nullable=False),
        sa.Column("altura", sa.Integer, nullable=False),
        sa.Column("peso", sa.Integer, nullable=False),
        sa.Column("tipo_1", sa.Text, nullable=False),
        sa.Column("tipo_2", sa.Text, nullable=True),
        sa.Column("habilidad_1", sa.Text, nullable=False),
        sa.Column("habilidad_2", sa.Text, nullable=True),
        sa.Column("habilidad_3", sa.Text, nullable=True),
        sa.Column("estadistica_hp", sa.Integer, nullable=False),
        sa.Column("estadistica_attack", sa.Integer, nullable=False),
        sa.Column("estadistica_defense", sa.Integer, nullable=False),
        sa.Column("estadistica_special_attack", sa.Integer, nullable=False),
        sa.Column("estadistica_special_defense", sa.Integer, nullable=False),
        sa.Column("estadistica_speed", sa.Integer, nullable=False),
    )

    op.create_table(
        "pokemonMovimiento",
        sa.Column("pokemon_id", sa.Integer, sa.ForeignKey("pokemon.id"), primary_key=True),
        sa.Column("movimiento_id", sa.Integer, sa.ForeignKey("movimiento.id"), primary_key=True),
    )

def downgrade() -> None:
    op.drop_table("pokemon_movimiento")
    op.drop_table("pokemon")