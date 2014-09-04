"""create forward func keys

Revision ID: 4ce50bcf2a0e
Revises: 379d2e0c5e51
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '4ce50bcf2a0e'
down_revision = '379d2e0c5e51'

from alembic import op
import sqlalchemy as sa


FORWARD_TYPE_ID = 6
FORWARD_TYPE_NAME = 'forward'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    service_type_row = {'id': FORWARD_TYPE_ID, 'name': FORWARD_TYPE_NAME}
    op.bulk_insert(destination_type_table, [service_type_row])

    op.create_table(
        'func_key_dest_forward',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint('destination_type_id = %d' % FORWARD_TYPE_ID),
                  server_default=str(FORWARD_TYPE_ID)),
        sa.Column('extension_id', sa.Integer),
        sa.Column('number', sa.String(40)),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id', 'extension_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['extension_id'], ['extensions.id'])
    )


def downgrade():
    op.drop_table('func_key_dest_forward')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == FORWARD_TYPE_ID))
    op.execute(delete_query)
