"""webi to dird ldap migration

Revision ID: 59feecbe8d13
Revises: 86511ef5d49

"""

# revision identifiers, used by Alembic.
revision = '59feecbe8d13'
down_revision = '86511ef5d49'

import json
import string

from alembic import op
from collections import namedtuple
from itertools import count
from sqlalchemy import sql, and_


cticontexts = sql.table('cticontexts',
                        sql.column('id'),
                        sql.column('directories'))
ctidirectories = sql.table('ctidirectories',
                           sql.column('id'),
                           sql.column('name'),
                           sql.column('uri'),
                           sql.column('delimiter'),
                           sql.column('match_direct'),
                           sql.column('match_reverse'),
                           sql.column('description'),
                           sql.column('deletable'))
ctidirectoryfields = sql.table('ctidirectoryfields',
                               sql.column('dir_id'),
                               sql.column('fieldname'),
                               sql.column('value'))
ldapfilter = sql.table('ldapfilter',
                       sql.column('id'),
                       sql.column('name'),
                       sql.column('attrdisplayname'),
                       sql.column('attrphonenumber'),
                       sql.column('additionaltype'),
                       sql.column('additionaltext'),
                       sql.column('commented'))
serverfeatures = sql.table('serverfeatures',
                           sql.column('serverid'),
                           sql.column('type'),
                           sql.column('feature'))

alphanum = string.ascii_letters + string.digits


def upgrade():
    ldap_filters = get_active_ldap_filters()
    directories = get_ldap_directories()
    profiles = get_profiles()

    directory_name_to_add_to_profiles = set()
    for ldap_filter in ldap_filters:
        if ldap_filter.additional_type == 'fax':
            continue
        directory = find_directory_by_ldap_filter_name(directories, ldap_filter.name)
        if not directory:
            directory = ldap_filter.build_directory(directories)
            directory.insert_db()
            directories.append(directory)
            directory_name_to_add_to_profiles.add(directory.name)
        else:
            ldap_filter.update_directory(directory)
            directory.update_db()
            directory_name_to_add_to_profiles.add(directory.name)

    for profile in profiles:
        profile.add_directories(directory_name_to_add_to_profiles)
        profile.update_db()


DirectoryField = namedtuple('DirectoryField', ['name', 'value'])


class LDAPFilter(object):

    def __init__(self):
        self.id = None
        self.name = ''
        self.display_names = []
        self.phone_numbers = []
        self.additional_type = ''
        self.additional_text = ''

    def build_directory(self, directories):
        # generate unique name
        directory_names = [directory.name for directory in directories]
        base_name = ''.join(c for c in self.name if c in alphanum)
        name = base_name
        for i in count(1):
            if name not in directory_names:
                break
            name = '{}{}'.format(base_name, i)

        directory = LDAPDirectory()
        directory.name = name
        directory.ldap_filter_name = self.name
        directory.match_direct = self._build_directory_match_direct()
        directory.fields = self._build_directory_fields()
        directory.description = 'Automatically created during upgrade'
        return directory

    def update_directory(self, directory):
        directory.add_match_direct(self._build_directory_match_direct())
        directory.add_fields(self._build_directory_fields())

    def _build_directory_match_direct(self):
        return self.display_names + self.phone_numbers

    def _build_directory_fields(self):
        fields = []
        for i, display_name in enumerate(self.display_names):
            field_name = 'display_name{}'.format(i if i else '')
            field_value = '{{{}}}'.format(display_name)
            fields.append(DirectoryField(field_name, field_value))

        if self.additional_type == 'custom':
            print 'warning: LDAP filter {}: ignoring custom phone number type "{}"'.format(
                                                            self.name, self.additional_text)
            phone_suffix = ''
        else:
            phone_suffix = '_{}'.format(self.additional_type)

        for i, phone_number in enumerate(self.phone_numbers):
            field_name = 'phone{}{}'.format(phone_suffix, i if i else '')
            field_value = '{{{}}}'.format(phone_number)
            fields.append(DirectoryField(field_name, field_value))
        return fields

    @classmethod
    def new_from_db(cls, row):
        ldap_filter = cls()
        ldap_filter.id = row.id
        ldap_filter.name = row.name
        if row.attrdisplayname:
            ldap_filter.display_names = row.attrdisplayname.split(',')
        if row.attrphonenumber:
            ldap_filter.phone_numbers = row.attrphonenumber.split(',')
        ldap_filter.additional_type = row.additionaltype
        ldap_filter.additional_text = row.additionaltext
        return ldap_filter


def get_active_ldap_filters():
    query = (sql.select([ldapfilter])
             .where(and_(ldapfilter.c.commented == 0,
                         ldapfilter.c.id == serverfeatures.c.serverid,
                         serverfeatures.c.type == 'ldap',
                         serverfeatures.c.feature == 'phonebook')))
    rows = op.get_bind().execute(query).fetchall()
    return [LDAPFilter.new_from_db(row) for row in rows]


class LDAPDirectory(object):

    def __init__(self):
        self.id = None
        self.name = ''
        self.ldap_filter_name = ''
        self.match_direct = []
        self.description = ''
        self.fields = []

    def add_match_direct(self, new_match_direct):
        for item in new_match_direct:
            if item not in self.match_direct:
                self.match_direct.append(item)

    def add_fields(self, new_fields):
        for new_field in new_fields:
            for existing_field in self.fields:
                if new_field.name == existing_field.name:
                    if new_field.value != existing_field.value:
                        print 'warning: directory {}: can\'t set field "{}" to "{}"; already defined as "{}"'.format(
                                                    self.name, new_field.name, new_field.value, existing_field.value)
                    break
            else:
                self.fields.append(new_field)

    def insert_db(self):
        uri = 'ldapfilter://{}'.format(self.ldap_filter_name)
        match_direct = self._convert_obj_match_direct(self.match_direct)
        query = (ctidirectories
                 .insert()
                 .returning(ctidirectories.c.id)
                 .values(name=self.name,
                         uri=uri,
                         delimiter='',
                         match_direct=match_direct,
                         match_reverse='',
                         description=self.description,
                         deletable=1))
        self.id = op.get_bind().execute(query).scalar()

        rows = [{'dir_id': self.id, 'fieldname': field.name, 'value': field.value} for field in self.fields]
        op.bulk_insert(ctidirectoryfields, rows)

    def update_db(self):
        match_direct = self._convert_obj_match_direct(self.match_direct)
        query = (ctidirectories
                 .update()
                 .where(ctidirectories.c.id == self.id)
                 .values(match_direct=match_direct))
        op.execute(query)

        query = (ctidirectoryfields
                 .delete()
                 .where(ctidirectoryfields.c.dir_id == self.id))
        op.execute(query)

        rows = [{'dir_id': self.id, 'fieldname': field.name, 'value': field.value} for field in self.fields]
        op.bulk_insert(ctidirectoryfields, rows)

    @classmethod
    def new_from_db(cls, ctidirectories_row, ctidirectoryfields_rows):
        directory = cls()
        directory.id = ctidirectories_row.id
        directory.name = ctidirectories_row.name
        directory.ldap_filter_name = ctidirectories_row.uri[len('ldapfilter://'):]
        directory.match_direct = cls._convert_db_match_direct(ctidirectories_row.match_direct)
        directory.fields = [DirectoryField(row.fieldname, row.value) for row in ctidirectoryfields_rows]
        return directory

    @classmethod
    def _convert_db_match_direct(cls, db_match_direct):
        if not db_match_direct:
            return []
        return json.loads(db_match_direct)

    @classmethod
    def _convert_obj_match_direct(cls, obj_match_direct):
        if not obj_match_direct:
            return ''
        return json.dumps(obj_match_direct)


def get_ldap_directories():
    query = (sql.select([ctidirectories])
            .where(ctidirectories.c.uri.like('ldapfilter://%')))
    ctidirectories_rows = op.get_bind().execute(query).fetchall()

    results = []
    for ctidirectories_row in ctidirectories_rows:
        query = (sql.select([ctidirectoryfields])
                 .where(ctidirectoryfields.c.dir_id == ctidirectories_row.id))
        ctidirectoryfields_rows = op.get_bind().execute(query).fetchall()
        results.append(LDAPDirectory.new_from_db(ctidirectories_row, ctidirectoryfields_rows))
    return results


class Profile(object):

    def __init__(self):
        self.id = None
        self.directories = []

    def add_directories(self, directories):
        for directory in directories:
            if directory not in self.directories:
                self.directories.append(directory)

    def update_db(self):
        directories = ','.join(self.directories)
        op.execute(cticontexts
                   .update()
                   .where(cticontexts.c.id == self.id)
                   .values(directories=directories))

    @classmethod
    def new_from_db(cls, row):
        profile = cls()
        profile.id = row.id
        if row.directories:
            profile.directories = row.directories.split(',')
        return profile


def get_profiles():
    query = (sql.select([cticontexts]))
    rows = op.get_bind().execute(query).fetchall()
    return [Profile.new_from_db(row) for row in rows]


def find_directory_by_ldap_filter_name(directories, filter_name):
    for directory in directories:
        if directory.ldap_filter_name == filter_name:
            return directory
    return None


def downgrade():
    pass
