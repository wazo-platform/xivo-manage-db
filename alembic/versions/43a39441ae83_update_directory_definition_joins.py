"""update directory definition joins

Revision ID: 43a39441ae83
Revises: 5712e7a66baa

"""

# revision identifiers, used by Alembic.
revision = '43a39441ae83'
down_revision = '5712e7a66baa'

import json

from alembic import op
from sqlalchemy import sql

directories = sql.table('directories',
                        sql.column('id'),
                        sql.column('dirtype'))
cti_contexts = sql.table('cticontexts',
                         sql.column('id'),
                         sql.column('name'),
                         sql.column('directories'))
context = sql.table('context',
                    sql.column('name'),
                    sql.column('entity'))
cti_directories = sql.table('ctidirectories',
                            sql.column('id'),
                            sql.column('name'),
                            sql.column('directory_id'))
cti_reverse = sql.table('ctireversedirectories',
                        sql.column('id'),
                        sql.column('directories'))


def upgrade():
    conn = op.get_bind()

    definitions = list_directory_definitions(conn)
    cticontexts = list_cti_contexts(conn)
    ctireverse = list_cti_reverse(conn)
    context_to_entity = get_context_entity_map(conn)

    update_cti_context(cticontexts, definitions, context_to_entity)
    update_cti_reverse(ctireverse, definitions)


def update_cti_reverse(ctireverse, definitions):
    for r in ctireverse:
        if r.directories == '[]':
            continue
        new_directories = []
        for name in json.loads(r.directories):
            if is_phonebook(definitions, name):
                for definition in definitions:
                    if definition.name.endswith('-{}'.format(name)):
                        new_directories.append(definition.name)
            else:
                new_directories.append(name)
        op.execute(cti_reverse.update()
                              .where(cti_reverse.c.id == r.id)
                              .values({'directories': json.dumps(new_directories)}))


def update_cti_context(cticontexts, definitions, context_to_entity):
    for c in cticontexts:
        entity = context_to_entity.get(c.name)
        if not entity:
            continue
        new_directories = []
        for name in c.directories.split(','):
            if is_phonebook(definitions, name):
                new_name = new_phonebook_name(definitions, entity, name)
                if new_name:
                    new_directories.append(new_name)
            else:
                new_directories.append(name)
        op.execute(cti_contexts.update()
                               .where(cti_contexts.c.id == c.id)
                               .values({'directories': ','.join(new_directories)}))


def downgrade():
    pass


def new_phonebook_name(definitions, entity, name):
    expected_name = '{}-{}'.format(entity, name)
    for definition in definitions:
        if definition.name == expected_name:
            return definition.name


def is_phonebook(definitions, name):
    for definition in definitions:
        if definition.name == name:
            return definition.dirtype == 'phonebook'


def get_context_entity_map(conn):
    query = sql.select([context])
    return {c.name: c.entity for c in conn.execute(query)}


def list_cti_contexts(conn):
    query = sql.select([cti_contexts])
    return [c for c in conn.execute(query)]


def list_cti_reverse(conn):
    query = sql.select([cti_reverse])
    return [r for r in conn.execute(query)]


def list_directory_definitions(conn):
    query = sql.select([
        cti_directories.c.id,
        cti_directories.c.name,
        cti_directories.c.directory_id,
        directories.c.dirtype
    ]).where(cti_directories.c.directory_id == directories.c.id)
    return [definition for definition in conn.execute(query)]
