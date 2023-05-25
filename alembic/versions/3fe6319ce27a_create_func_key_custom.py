"""create func key custom

Revision ID: 3fe6319ce27a
Revises: 234745874c55

"""

# revision identifiers, used by Alembic.
revision = '3fe6319ce27a'
down_revision = '234745874c55'

from alembic import op
import sqlalchemy as sa


CUSTOM_TYPE_ID = 10
CUSTOM_TYPE_NAME = 'custom'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    service_type_row = {'id': CUSTOM_TYPE_ID, 'name': CUSTOM_TYPE_NAME}
    op.bulk_insert(destination_type_table, [service_type_row])

    op.create_table(
        'func_key_dest_custom',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint(f'destination_type_id = {CUSTOM_TYPE_ID}'),
                  server_default=str(CUSTOM_TYPE_ID)),
        sa.Column('exten', sa.String(40), nullable=False),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
    )


def downgrade():
    op.drop_table('func_key_dest_custom')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == CUSTOM_TYPE_ID))
    op.execute(delete_query)
