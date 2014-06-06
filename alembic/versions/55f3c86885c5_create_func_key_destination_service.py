"""create_func_key_destination_service

Revision ID: 55f3c86885c5
Revises: 146ddf6c4b36
Create Date: 2014-05-14 14:39:41.329649
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '55f3c86885c5'
down_revision = '5073b1fa473e'

from alembic import op
import sqlalchemy as sa


SERVICE_TYPE_ID = 5
SERVICE_TYPE_NAME = 'service'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    service_type_row = {'id': SERVICE_TYPE_ID, 'name': SERVICE_TYPE_NAME}
    op.bulk_insert(destination_type_table, [service_type_row])

    op.create_table(
        'func_key_dest_service',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint('destination_type_id = %d' % SERVICE_TYPE_ID),
                  server_default=str(SERVICE_TYPE_ID)),
        sa.Column('extension_id', sa.Integer),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id', 'extension_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['extension_id'], ['extensions.id'])
    )


def downgrade():
    op.drop_table('func_key_dest_service')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == SERVICE_TYPE_ID))
    op.execute(delete_query)
