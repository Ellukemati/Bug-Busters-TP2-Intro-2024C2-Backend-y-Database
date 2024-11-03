"""crear relacion entre equipo e integrante pokemon

Revision ID: 512ee31d45a7
Revises: 4dab2591f953
Create Date: 2024-11-03 16:12:52.467763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '512ee31d45a7'
down_revision: Union[str, None] = '4dab2591f953'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('integrante_pokemon') as batch_op:
        batch_op.add_column(sa.Column('Equipo_id', sa.Integer))
        batch_op.create_foreign_key('fk_equipo_integrante', 'Equipo', ['equipo_id'], ['id_equipo'])


def downgrade() -> None:
    with op.batch_alter_table('integrante_pokemon') as batch_op:
        batch_op.drop_constraint(
            'fk_equipo_integrante', type_='foreignhey')
        batch_op.drop_column(
            'equipo_id'
        )
