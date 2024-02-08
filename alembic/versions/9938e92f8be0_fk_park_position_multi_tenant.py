"""fk-park-position-multi-tenant

Revision ID: 9938e92f8be0
Revises: 5022e9450437

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9938e92f8be0'
down_revision = '5022e9450437'


def upgrade():
    # NOTE(fblackburn): We assume that all func_key_dest_park_position have been deleted
    # from previous iteration script
    op.add_column(
        'func_key_dest_park_position',
        sa.Column(
            'parking_lot_id',
            sa.Integer,
            sa.ForeignKey('parking_lot.id'),
            nullable=False,
        )
    )
    op.create_unique_constraint(
        'func_key_dest_park_position_parking_lot_id_park_position_key',
        'func_key_dest_park_position',
        ['parking_lot_id', 'park_position'],
    )


def downgrade():
    op.drop_constraint(
        'func_key_dest_park_position_parking_lot_id_park_position_key',
        'func_key_dest_park_position',
    )
    op.drop_column('func_key_dest_park_position', 'parking_lot_id')
