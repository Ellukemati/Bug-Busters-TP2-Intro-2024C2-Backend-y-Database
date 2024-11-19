"""Crear tabla naturaleza

Revision ID: badc6a43c32f
Revises: a82e39b2db28
Create Date: 2024-11-04 11:14:59.972662

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "badc6a43c32f"
down_revision: Union[str, None] = "a82e39b2db28"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "naturaleza",
        sa.Column("id", sa.INTEGER, primary_key=True),
        sa.Column("nombre", sa.TEXT, nullable=False),
        sa.Column("aumenta_estadistica", sa.TEXT, nullable=False),
        sa.Column("reduce_estadistica", sa.TEXT, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("naturaleza")