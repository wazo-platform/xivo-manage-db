"""create func key park position

Revision ID: a3e7fd7b670
Revises: 5450dd40916e

"""

# revision identifiers, used by Alembic.
revision = 'a3e7fd7b670'
down_revision = '5450dd40916e'

from alembic import op
import sqlalchemy as sa


PARKING_TYPE_ID = 7
PARKING_TYPE_NAME = 'park_position'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    parking_type_row = {'id': PARKING_TYPE_ID, 'name': PARKING_TYPE_NAME}
    op.bulk_insert(destination_type_table, [parking_type_row])

    op.create_table(
        'func_key_dest_park_position',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint('destination_type_id = %d' % PARKING_TYPE_ID),
                  server_default=str(PARKING_TYPE_ID)),
        sa.Column('park_position',
                  sa.String(40),
                  sa.CheckConstraint("park_position ~ '^[0-9]+$'"),
                  nullable=False),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id'])
    )


def downgrade():
    op.drop_table('func_key_dest_park_position')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == PARKING_TYPE_ID))
    op.execute(delete_query)
