"""create new dird phonebooks

Revision ID: f721d0482a3
Revises: 15b236bd8060

"""

# revision identifiers, used by Alembic.
revision = 'f721d0482a3'
down_revision = '4fa0a41c0327'

from alembic import op
from sqlalchemy import and_, sql

directories = sql.table('directories',
                        sql.column('id'),
                        sql.column('name'),
                        sql.column('uri'),
                        sql.column('dirtype'),
                        sql.column('description'),
                        sql.column('dird_tenant'),
                        sql.column('dird_phonebook'))
entity = sql.table('entity',
                   sql.column('name'),
                   sql.column('disable'))

old_local_phonebook_uri = 'http://localhost/service/ipbx/json.php/private/pbx_services/phonebook'
new_dird_phonebook_uri = 'postgresql://asterisk:proformatique@localhost/asterisk'
default_dird_phonebook = 'xivo'


def upgrade():
    conn = op.get_bind()

    entities = list_entities(conn)
    phonebooks = list_phonebooks(conn)

    add_phonebooks(entities, phonebooks)


def add_phonebooks(entities, phonebooks):
    rows = []

    for entity in entities:
        for phonebook in phonebooks:
            directory = {'uri': new_dird_phonebook_uri,
                         'dirtype': 'dird_phonebook',
                         'name': '{}-{}'.format(entity, phonebook.name),
                         'description': phonebook.description,
                         'dird_tenant': entity,
                         'dird_phonebook': default_dird_phonebook}
            rows.append(directory)

    op.bulk_insert(directories, rows)


def list_entities(conn):
    entity_qry = sql.select([entity.c.name]).where(entity.c.disable == 0)
    return [e.name for e in conn.execute(entity_qry)]


def list_phonebooks(conn):
    phonebook_qry = sql.select(
        [directories.c.id,
         directories.c.name,
         directories.c.description]).where(
             and_(directories.c.uri == old_local_phonebook_uri,
                  directories.c.dirtype == 'phonebook'))
    return [phonebook for phonebook in conn.execute(phonebook_qry)]


def downgrade():
    pass
