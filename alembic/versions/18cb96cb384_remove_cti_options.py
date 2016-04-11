"""remove cti options

Revision ID: 18cb96cb384
Revises: 3b7b334edb5c

"""

# revision identifiers, used by Alembic.
revision = '18cb96cb384'
down_revision = '3b7b334edb5c'

from alembic import op

from sqlalchemy.types import Integer, String
from sqlalchemy.schema import Column
from sqlalchemy import sql

ctimain_table = sql.table('ctimain',
                          sql.column('cti_ip'),
                          sql.column('cti_port'),
                          sql.column('cti_active'),
                          sql.column('webi_ip'),
                          sql.column('webi_port'),
                          sql.column('webi_active'),
                          sql.column('info_ip'),
                          sql.column('info_port'),
                          sql.column('info_active'),
                          sql.column('login_timeout'),
                          sql.column('socket_timeout'))


def upgrade():
    for col in ['cti_ip', 'cti_port', 'cti_active',
                'webi_ip', 'webi_port', 'webi_active',
                'info_ip', 'info_port', 'info_active',
                'socket_timeout', 'login_timeout']:
        op.drop_column('ctimain', col)


def downgrade():
    for col in ['cti_active', 'webi_active', 'info_active']:
        op.add_column('ctimain', Column(col, Integer, nullable=False, server_default='1'))

    for col in ['cti_port', 'webi_port', 'info_port', 'socket_timeout', 'login_timeout']:
        op.add_column('ctimain', Column(col, Integer))

    for col in ['cti_ip', 'webi_ip', 'info_ip']:
        op.add_column('ctimain', Column(col, String(16)))

    op.execute(ctimain_table.update().values(cti_ip='0.0.0.0',
                                             cti_port=5003,
                                             cti_active=1,
                                             webi_ip='127.0.0.1',
                                             webi_port=5004,
                                             webi_active=1,
                                             info_ip='127.0.0.1',
                                             info_port=5005,
                                             info_active=1,
                                             socket_timeout=10,
                                             login_timeout=5))
