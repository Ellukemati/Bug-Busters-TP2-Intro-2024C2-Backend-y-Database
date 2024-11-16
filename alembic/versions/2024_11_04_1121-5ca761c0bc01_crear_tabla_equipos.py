"""Crear tabla Equipos

Revision ID: 5ca761c0bc01
Revises: f964edd8e0cc
Create Date: 2024-11-04 11:21:11.211410

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
#f964edd8e0cc

# revision identifiers, used by Alembic.
revision: str = "5ca761c0bc01"
down_revision: Union[str, None] = "25d8e8b1052c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "equipo",
        sa.Column("id_equipo", sa.INTEGER, primary_key=True),
        sa.Column("nombre", sa.TEXT, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("equipo")