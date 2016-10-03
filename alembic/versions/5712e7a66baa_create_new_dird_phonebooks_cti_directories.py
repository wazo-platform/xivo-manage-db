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
directory_fields = sql.table('ctidirectoryfields',
                             sql.column('dir_id'),
                             sql.column('fieldname'),
                             sql.column('value'))


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
                            'match_direct': format_fieldname(definition.match_direct),
                            'match_reverse': format_fieldname(definition.match_reverse),
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


class FieldGenerator(object):

    def __init__(self, entities, phonebook_definitions, dird_definitions, directories, fields):
        self.entities = entities
        self.phonebook_definitions = phonebook_definitions
        self.dird_definitions = dird_definitions
        self.directories = directories
        self.fields = fields

    def generate(self):
        new = []
        for phonebook in self.phonebook_definitions:
            for dird in self.dird_definitions:
                if not dird.name.endswith('-{}'.format(phonebook.name)):
                    continue
                for field in self.fields:
                    if field.dir_id != phonebook.id:
                        continue
                    new.append({'dir_id': dird.id,
                                'fieldname': field.fieldname,
                                'value': format_fieldname(field.value)})
        return new


def format_fieldname(fieldname):
    # {phonebook.firstname} => {firstname}
    fieldname = fieldname.replace('phonebook.', '')

    # {phonebooknumber.office.number} => {number_office}
    fieldname = fieldname.replace('phonebooknumber.', 'number_')
    fieldname = fieldname.replace('.number', '')

    # {phonebookaddress.office.*} => {address_office_*}
    fieldname = fieldname.replace('phonebookaddress.', 'address_')
    for type_ in ['office', 'home', 'other']:
        fieldname = fieldname.replace('address_{}.'.format(type_),
                                      'address_{}_'.format(type_))

    return fieldname


def upgrade():
    conn = op.get_bind()

    entities = list_entities(conn)
    cti_phonebook_directories = list_cti_directories(conn, 'phonebook')
    directories = get_directories(conn)

    generator = DefinitionGenerator(entities, cti_phonebook_directories, directories)
    op.bulk_insert(cti_directories, generator.generate())

    cti_dird_phonebook_directories = list_cti_directories(conn, 'dird_phonebook')
    fields = list_fields(conn)

    generator = FieldGenerator(entities,
                               cti_phonebook_directories,
                               cti_dird_phonebook_directories,
                               directories,
                               fields)

    op.bulk_insert(directory_fields, generator.generate())


def downgrade():
    pass


def get_directories(conn):
    query = sql.select([directories])
    return [d for d in conn.execute(query)]


def list_cti_directories(conn, type_):
    query = sql.select(
        [cti_directories]
    ).where(and_(cti_directories.c.directory_id == directories.c.id,
                 directories.c.dirtype == type_))
    return [directory for directory in conn.execute(query)]


def list_entities(conn):
    query = sql.select([entity])
    return [e.name for e in conn.execute(query)]


def list_fields(conn):
    query = sql.select([directory_fields])
    return [f for f in conn.execute(query)]
