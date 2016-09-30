"""add ldapfilter directories

Revision ID: 5270d317f8fd
Revises: 394edc522e4a

"""

# revision identifiers, used by Alembic.
revision = '5270d317f8fd'
down_revision = '394edc522e4a'

from alembic import op
import sqlalchemy as sa

ldapfilter_table = sa.sql.table('ldapfilter',
                                sa.Column('id'),
                                sa.Column('name'))
directory_table = sa.sql.table('directories',
                               sa.Column('name'),
                               sa.Column('dirtype'),
                               sa.Column('ldapfilter_id'),
                               sa.Column('description'))

def list_ldap_filters():
    conn = op.get_bind()
    query = sa.sql.select([ldapfilter_table])
    return [{'id': row.id, 'name': row.name} for row in conn.execute(query)]


def upgrade():
    ldapfilters = list_ldap_filters()
    directories = [{'name': filter['name'],
                    'dirtype': 'ldapfilter',
                    'ldapfilter_id': filter['id'],
                    'description': ''} for filter in ldapfilters]
    op.bulk_insert(directory_table, directories)


def downgrade():
    op.execute(directory_table.delete().where(directory_table.c.dirtype=='ldapfilter'))
