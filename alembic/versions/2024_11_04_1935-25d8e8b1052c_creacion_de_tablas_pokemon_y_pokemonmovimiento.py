"""Creación de tablas Pokemon y PokemonMovimiento

Revision ID: 25d8e8b1052c
Revises: 1f5e7255ea81
Create Date: 2024-11-04 19:35:11.774815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "1"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "Pokemon",
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
        sa.Column("evolucion_anterior", sa.Integer, nullable=True),
        sa.Column("evolucion_siguiente", sa.Integer, nullable=True),
    )

    op.create_table(
        "PokemonMovimiento",
        sa.Column("pokemon_id", sa.Integer, primary_key=True),
        sa.Column("movimiento_id", sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(
            ["pokemon_id"],
            ["pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["movimiento_id"],
            ["movimiento.id"],
        ),
    )

def downgrade() -> None:
    op.drop_table("PokemonMovimiento")
    op.drop_table("Pokemon")