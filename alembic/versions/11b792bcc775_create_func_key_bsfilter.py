"""create func key bsfilter

Revision ID: 11b792bcc775
Revises: 3d22f40558d1

"""

# revision identifiers, used by Alembic.
revision = '11b792bcc775'
down_revision = '3d22f40558d1'

from alembic import op
import sqlalchemy as sa


DESTINATION_ID = 12
DESTINATION_NAME = 'bsfilter'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    destination_type_row = {'id': DESTINATION_ID, 'name': DESTINATION_NAME}
    op.bulk_insert(destination_type_table, [destination_type_row])

    op.create_table(
        'func_key_dest_bsfilter',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint('destination_type_id = %d' % DESTINATION_ID),
                  server_default=str(DESTINATION_ID)),
        sa.Column('filtermember_id',
                  sa.Integer,
                  nullable=False),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id', 'filtermember_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['filtermember_id'], ['callfiltermember.id'])
    )


def downgrade():
    op.drop_table('func_key_dest_bsfilter')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == DESTINATION_ID))
    op.execute(delete_query)
