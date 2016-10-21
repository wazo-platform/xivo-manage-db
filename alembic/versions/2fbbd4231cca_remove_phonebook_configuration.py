"""remove phonebook configuration

Revision ID: 2fbbd4231cca
Revises: 56a9a83c26b3

"""

# revision identifiers, used by Alembic.
revision = '2fbbd4231cca'
down_revision = '56a9a83c26b3'

import json

from alembic import op
from sqlalchemy import sql, and_


directories = sql.table('directories',
                        sql.column('id'),
                        sql.column('dirtype'))
cti_directories = sql.table('ctidirectories',
                            sql.column('id'),
                            sql.column('name'),
                            sql.column('directory_id'))
cti_contexts = sql.table('cticontexts',
                         sql.column('id'),
                         sql.column('name'),
                         sql.column('directories'))
cti_reverse = sql.table('ctireversedirectories',
                        sql.column('id'),
                        sql.column('directories'))


def list_cti_directories(conn, type_):
    query = sql.select(
        [cti_directories]
    ).where(and_(cti_directories.c.directory_id == directories.c.id,
                 directories.c.dirtype == type_))
    return [directory for directory in conn.execute(query)]


def remove_from_direct_directories(conn, name):
    query = sql.select([cti_contexts]).where(cti_contexts.c.directories.ilike('%{}%'.format(name)))
    for context in conn.execute(query):
        directories = context.directories.split(',')
        if name not in directories:
            continue
        directories.remove(name)
        op.execute(cti_contexts
                   .update()
                   .where(cti_contexts.c.id == context.id)
                   .values({'directories': ','.join(directories)}))


def remove_from_reverse_directories(conn, name):
    query = sql.select([cti_reverse]).where(cti_reverse.c.directories.ilike('%{}%'.format(name)))
    for reverse in conn.execute(query):
        directories = json.loads(reverse.directories)
        if name not in directories:
            continue
        directories.remove(name)
        op.execute(cti_reverse
                   .update()
                   .where(cti_reverse.c.id == reverse.id)
                   .values({'directories': json.dumps(directories)}))


def upgrade():
    conn = op.get_bind()

    names = [d.name for d in list_cti_directories(conn, 'phonebook')]
    for name in names:
        remove_from_direct_directories(conn, name)
        remove_from_reverse_directories(conn, name)

    op.execute(directories.delete().where(directories.c.dirtype == 'phonebook'))


def downgrade():
    pass
