"""Crear tabla integrante_pokemon

Revision ID: 32a30a156131
Revises: badc6a43c32f
Create Date: 2024-11-04 11:15:45.442217

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
#25d8e8b1052c

# revision identifiers, used by Alembic.
revision: str = "32a30a156131"
down_revision: Union[str, None] = "5ca761c0bc01"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "integrante_pokemon",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("pokemon_id", sa.Integer(), nullable=False),
        sa.Column("naturaleza_id", sa.Integer(), nullable=False),
        sa.Column("naturaleza", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pokemon_id"],
            ["pokemon.id_repetido"],
        ),
        sa.ForeignKeyConstraint(
            ["naturaleza_id"],
            ["naturaleza.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("integrante_pokemon")