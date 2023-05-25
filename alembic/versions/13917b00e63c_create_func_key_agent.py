"""create func key agent

Revision ID: 13917b00e63c
Revises: 3096b11582cf

"""

# revision identifiers, used by Alembic.
revision = '13917b00e63c'
down_revision = '3096b11582cf'

from alembic import op
import sqlalchemy as sa

DESTINATION_ID = 11
DESTINATION_NAME = 'agent'

destination_type_table = sa.sql.table('func_key_destination_type',
                                      sa.sql.column('id'),
                                      sa.sql.column('name'))


def upgrade():
    destination_type_row = {'id': DESTINATION_ID, 'name': DESTINATION_NAME}
    op.bulk_insert(destination_type_table, [destination_type_row])

    op.create_table(
        'func_key_dest_agent',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint(f'destination_type_id = {DESTINATION_ID}'),
                  server_default=str(DESTINATION_ID)),
        sa.Column('agent_id',
                  sa.Integer,
                  nullable=False),
        sa.Column('action',
                  sa.String(10),
                  sa.CheckConstraint("action IN ('login', 'logoff', 'toggle')"),
                  nullable=False
                  ),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id'),
        sa.UniqueConstraint('agent_id', 'action'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['agent_id'], ['agentfeatures.id'])
    )


def downgrade():
    op.drop_table('func_key_dest_agent')

    delete_query = (destination_type_table
                    .delete()
                    .where(destination_type_table.c.id == DESTINATION_ID))
    op.execute(delete_query)
