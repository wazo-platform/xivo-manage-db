"""remove dead forward func keys

Revision ID: e0fd01d4c2a
Revises: 5a02fde67132

"""

# revision identifiers, used by Alembic.
revision = 'e0fd01d4c2a'
down_revision = '5a02fde67132'

from alembic import op
from sqlalchemy import sql

FORWARD_DESTINATION_ID = 6

func_key_table = sql.table('func_key',
                           sql.column('id'),
                           sql.column('type_id'),
                           sql.column('destination_type_id'))

func_key_mapping_table = sql.table('func_key_mapping',
                                   sql.column('template_id'),
                                   sql.column('func_key_id'),
                                   sql.column('destination_type_id'),
                                   sql.column('label'),
                                   sql.column('position'),
                                   sql.column('blf'))

destination_forward_table = sql.table('func_key_dest_forward',
                                      sql.column('func_key_id'),
                                      sql.column('destination_type_id'),
                                      sql.column('extension_id'),
                                      sql.column('number'))


def upgrade():
    all_forwards = (sql.select(
        [func_key_mapping_table.c.func_key_id])
        .where(
            func_key_mapping_table.c.destination_type_id == FORWARD_DESTINATION_ID)
        .alias()
    )

    query = (destination_forward_table
             .delete()
             .where(
                 destination_forward_table.c.func_key_id.notin_(all_forwards))
             )

    op.execute(query)

    query = (func_key_table
             .delete()
             .where(
                 sql.and_(
                     func_key_table.c.destination_type_id == FORWARD_DESTINATION_ID,
                     func_key_table.c.id.notin_(all_forwards)))
             )

    op.execute(query)


def downgrade():
    pass
