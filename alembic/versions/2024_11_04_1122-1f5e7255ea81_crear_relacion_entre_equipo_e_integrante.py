"""Crear relacion entre equipo e integrante

Revision ID: 1f5e7255ea81
Revises: 5ca761c0bc01
Create Date: 2024-11-04 11:22:11.766632

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f5e7255ea81"
down_revision: Union[str, None] = "f964edd8e0cc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("integrante_pokemon") as batch_op:
        batch_op.add_column(sa.Column("equipo_id", sa.Integer))
        batch_op.create_foreign_key(
            "fk_equipo_integrante", "equipo", ["equipo_id"], ["id_equipo"]
        )


def downgrade() -> None:
    with op.batch_alter_table("integrante_pokemon") as batch_op:
        batch_op.drop_constraint("fk_Equipo_integrante", type_="foreignkey")
        batch_op.drop_column("equipo_id")