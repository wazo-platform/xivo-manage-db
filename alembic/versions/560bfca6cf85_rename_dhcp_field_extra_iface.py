"""rename dhcp field extra_iface

Revision ID: 560bfca6cf85
Revises: 62c5befaa8cf

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '560bfca6cf85'
down_revision = '62c5befaa8cf'


def upgrade():
    op.alter_column('dhcp', 'extra_ifaces', new_column_name='network_interfaces')


def downgrade():
    op.alter_column('dhcp', 'network_interfaces', new_column_name='extra_ifaces')
