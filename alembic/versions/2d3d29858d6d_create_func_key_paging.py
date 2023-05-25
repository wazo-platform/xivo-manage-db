"""create func key paging


Revision ID: 2d3d29858d6d
Revises: e0fd01d4c2a

"""

# revision identifiers, used by Alembic.
revision = '2d3d29858d6d'
down_revision = 'e0fd01d4c2a'

from alembic import op
import sqlalchemy as sa


PAGING_TYPE_ID = 9
PAGING_TYPE_NAME = 'paging'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    parking_type_row = {'id': PAGING_TYPE_ID, 'name': PAGING_TYPE_NAME}
    op.bulk_insert(destination_type_table, [parking_type_row])

    op.create_table(
        'func_key_dest_paging',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint(f'destination_type_id = {PAGING_TYPE_ID}'),
                  server_default=str(PAGING_TYPE_ID)),
        sa.Column('paging_id', sa.Integer),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id', 'paging_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['paging_id'], ['paging.id'])
    )


def downgrade():
    op.drop_table('func_key_dest_paging')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == PAGING_TYPE_ID))
    op.execute(delete_query)
