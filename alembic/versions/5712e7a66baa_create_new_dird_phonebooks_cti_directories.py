"""create new dird phonebooks cti directories

Revision ID: 5712e7a66baa
Revises: f721d0482a3

"""

# revision identifiers, used by Alembic.
revision = '5712e7a66baa'
down_revision = 'f721d0482a3'

from alembic import op
from sqlalchemy import and_, sql


directories = sql.table('directories',
                        sql.column('id'),
                        sql.column('name'),
                        sql.column('uri'),
                        sql.column('dirtype'),
                        sql.column('description'))
entity = sql.table('entity',
                   sql.column('name'),
                   sql.column('disable'))
cti_directories = sql.table('ctidirectories',
                            sql.column('id'),
                            sql.column('name'),
                            sql.column('match_direct'),
                            sql.column('match_reverse'),
                            sql.column('deletable'),
                            sql.column('directory_id'),
                            sql.column('description'))


class DefinitionGenerator(object):

    def __init__(self, entities, current_definitions, directories):
        self.entities = entities
        self.definitions = current_definitions
        self.directories = directories

    def generate(self):
        new = []
        for entity in self.entities:
            for definition in self.definitions:
                new_directory_id = self._find_directory_id(entity, definition.directory_id)
                if not new_directory_id:
                    continue
                new.append({'name': '{}-{}'.format(entity, definition.name),
                            'match_direct': definition.match_direct,
                            'match_reverse': definition.match_reverse,
                            'deletable': definition.deletable,
                            'directory_id': new_directory_id,
                            'description': definition.description})
        return new

    def _find_directory_id(self, entity, directory_id):
        for directory in self.directories:
            if directory.id == directory_id:
                expected_name = '{}-{}'.format(entity, directory.name)
                for directory in self.directories:
                    if directory.name == expected_name:
                        return directory.id


def upgrade():
    conn = op.get_bind()

    entities = list_entities(conn)
    cti_phonebook_directories = list_cti_phonebook_directories(conn)
    directories = get_directories(conn)

    generator = DefinitionGenerator(entities, cti_phonebook_directories, directories)
    op.bulk_insert(cti_directories, generator.generate())


def downgrade():
    pass


def get_directories(conn):
    query = sql.select([directories])
    return [d for d in conn.execute(query)]


def list_cti_phonebook_directories(conn):
    query = sql.select(
        [cti_directories]
    ).where(and_(cti_directories.c.directory_id == directories.c.id,
                 directories.c.dirtype == 'phonebook'))
    return [directory for directory in conn.execute(query)]


def list_entities(conn):
    query = sql.select([entity])
    return [e.name for e in conn.execute(query)]
