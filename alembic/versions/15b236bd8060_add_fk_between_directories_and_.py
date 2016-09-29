"""add fk between directories and ctidirectories

Revision ID: 15b236bd8060
Revises: 5270d317f8fd

"""

# revision identifiers, used by Alembic.
revision = '15b236bd8060'
down_revision = '5270d317f8fd'

from alembic import op
import sqlalchemy as sa

cti_directories_table = sa.sql.table('ctidirectories',
                                     sa.Column('id'),
                                     sa.Column('uri'),
                                     sa.Column('directory_id'))
ldapfilter_table = sa.sql.table('ldapfilter',
                                sa.Column('id'),
                                sa.Column('name'))
directory_table = sa.sql.table('directories',
                               sa.Column('id'),
                               sa.Column('dirtype'),
                               sa.Column('uri'),
                               sa.Column('ldapfilter_id'))
ldap_prefix = 'ldapfilter://'


def list_associations(conn):
    query = sa.sql.select([cti_directories_table])
    return [(row.id, row.uri) for row in conn.execute(query)]

def list_ldap_filters(conn):
    query = sa.sql.select([ldapfilter_table])
    return {row.name: row.id for row in conn.execute(query)}

def list_directories(conn):
    query = sa.sql.select([directory_table])
    return [directory for directory in conn.execute(query)]


def set_directory_id(cti_directory_id, directory_id):
    query = cti_directories_table.update().where(
        cti_directories_table.c.id == cti_directory_id
    ).values(directory_id=directory_id)
    op.execute(query)

def upgrade():
    op.add_column('ctidirectories',
                  sa.Column('directory_id',
                            sa.Integer(),
                            sa.ForeignKey('directories.id')))
    conn = op.get_bind()

    ldap_filters = list_ldap_filters(conn)
    cti_directories = list_associations(conn)
    directories = list_directories(conn)

    ldap_cti_directories = []
    normal_cti_directories = []

    for id_, uri in cti_directories:
        if uri.startswith(ldap_prefix):
            ldap_cti_directories.append((id_, uri))
        else:
            normal_cti_directories.append((id_, uri))

    for id_, uri in normal_cti_directories:
        for d in directories:
            if d.uri != uri:
                continue
            set_directory_id(id_, d.id)

    for id_, uri in ldap_cti_directories:
        name = uri.replace(ldap_prefix, '')
        ldap_filter_id = ldap_filters.get(name)
        if not ldap_filter_id:
            continue
        for d in directories:
            if d.dirtype == 'ldapfilter' and d.ldapfilter_id == ldap_filter_id:
                set_directory_id(id_, d.id)

    delete_orphans = cti_directories_table.delete().where(cti_directories_table.c.directory_id == None)
    op.execute(delete_orphans)

    op.drop_column('ctidirectories', 'uri')


def downgrade():
    pass
