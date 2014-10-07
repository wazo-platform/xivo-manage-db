"""fix func key type ids

Revision ID: 27d9ea4b21d0
Revises: f485ac649eb

"""

# revision identifiers, used by Alembic.
revision = '27d9ea4b21d0'
down_revision = '18e40e519e1b'

from alembic import op
from sqlalchemy import sql


func_key_table = sql.table('func_key',
                           sql.column('id'),
                           sql.column('type_id'),
                           sql.column('destination_type_id'))

func_key_type_table = sql.table('func_key_type',
                                sql.column('id'),
                                sql.column('name'))


def upgrade():
    connection = op.get_bind()
    func_key_ids = memorize_func_key_ids()

    op.drop_constraint('func_key_type_id_fkey', 'func_key')
    fix_ids('speeddial', 1, func_key_ids['speeddial'])
    fix_ids('transfer', 2, func_key_ids['transfer'])
    connection.execute("SELECT setval('func_key_type_id_seq', (SELECT MAX(id) FROM func_key_type))")
    op.create_foreign_key('func_key_type_id_fkey', 'func_key', 'func_key_type', ['type_id'], ['id'])


def memorize_func_key_ids():
    func_key_ids = {}

    columns = (func_key_type_table.c.name,
               func_key_table.c.id)

    join_condition = (func_key_table
                      .join(func_key_type_table,
                            func_key_type_table.c.id == func_key_table.c.type_id)
                      )

    query = sql.select(columns, from_obj=[join_condition])

    for row in op.get_bind().execute(query):
        func_key_ids.setdefault(row.name, []).append(row.id)

    return func_key_ids


def fix_ids(fk_type, type_id, func_key_ids):
    query = (func_key_table
             .update()
             .values(type_id=type_id)
             .where(func_key_table.c.id.in_(func_key_ids))
             )

    op.get_bind().execute(query)

    query = (func_key_type_table
             .update()
             .values(id=type_id)
             .where(func_key_type_table.c.name == fk_type)
             )

    op.get_bind().execute(query)


def downgrade():
    pass
