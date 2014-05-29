"""create_func_key_destination_extension

Revision ID: 55f3c86885c5
Revises: 146ddf6c4b36
Create Date: 2014-05-14 14:39:41.329649
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '55f3c86885c5'
down_revision = '3196befc4753'

from alembic import op
import sqlalchemy as sa


EXTENSION_TYPE_ID = 5
EXTENSION_TYPE_NAME = 'extension'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    extension_type_row = {'id': EXTENSION_TYPE_ID, 'name': EXTENSION_TYPE_NAME}
    op.bulk_insert(destination_type_table, [extension_type_row])

    op.create_table(
        'func_key_dest_extension',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint('destination_type_id = %d' % EXTENSION_TYPE_ID),
                  server_default=str(EXTENSION_TYPE_ID)),
        sa.Column('extension_id', sa.Integer),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id', 'extension_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['extension_id'], ['extensions.id'])
    )


def downgrade():
    op.drop_table('func_key_dest_extension')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == EXTENSION_TYPE_ID))
    op.execute(delete_query)
