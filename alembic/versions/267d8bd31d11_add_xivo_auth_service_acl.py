"""add_xivo_auth_service_acl

Revision ID: 267d8bd31d11
Revises: 379ed6d9a62

"""

# revision identifiers, used by Alembic.
revision = '267d8bd31d11'
down_revision = '379ed6d9a62'

from alembic import op
from sqlalchemy import (Column,
                        String,
                        sql)
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY


webservice = sql.table('accesswebservice',
                       sql.column('name'),
                       sql.column('login'),
                       sql.column('passwd'),
                       sql.column('acl'),
                       sql.column('description'))


def upgrade():
    op.add_column('accesswebservice',
                  Column('acl',
                         ARRAY(String),
                         nullable=False,
                         server_default='{}'))

    op.alter_column('accesswebservice', 'description', server_default='')

    _insert_web_service('xivo-agentd-cli',
                        'xivo-agentd-cli',
                        '{agentd.#}',
                        'Automatically created during upgrade')

    _insert_web_service('xivo-agid',
                        'xivo-agid',
                        '{dird.directories.reverse.*.*}',
                        'Automatically created during upgrade')

    _insert_web_service('xivo-ctid',
                        'xivo-ctid',
                        '{dird.#, agentd.#}',
                        'Automatically created during upgrade')

    _insert_web_service('xivo-ctid-ng',
                        'xivo-ctid-ng',
                        '{confd.#}',
                        'Automatically created during upgrade')

    _insert_web_service('xivo-dird-phoned',
                        'xivo-dird-phoned',
                        '{dird.directories.menu.*.*, dird.directories.input.*.*, dird.directories.lookup.*.*}',
                        'Automatically created during upgrade')


def _insert_web_service(name, login, acl, description):
    op.execute(webservice
               .insert()
               .values(name=name,
                       login=login,
                       passwd=func.substring(func.gen_salt('bf', 4), 8),
                       acl=acl,
                       description=description))


def downgrade():
    op.drop_column('accesswebservice', 'acl')
    _delete_web_service('xivo-agentd-cli')
    _delete_web_service('xivo-agid')
    _delete_web_service('xivo-ctid')
    _delete_web_service('xivo-ctid-ng')
    _delete_web_service('xivo-dird-phoned')


def _delete_web_service(name):
    op.execute(webservice
               .delete()
               .where(webservice.c.name == name))
