"""configure the dhcp interface

Revision ID: 1192e6bfd226
Revises: 700711f75ee6

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1192e6bfd226'
down_revision = '700711f75ee6'

netiface_table = sa.sql.table(
    'netiface',
    sa.sql.column('ifname'),
    sa.sql.column('networktype'),
)

dhcp_table = sa.sql.table(
    'dhcp',
    sa.sql.column('extra_ifaces'),
)


def upgrade():
    query = sa.sql.select(
        [netiface_table.c.ifname]
    ).where(
        netiface_table.c.networktype == 'voip'
    )

    ifname = None
    for netiface in op.get_bind().execute(query):
        ifname = netiface.ifname

    if not ifname:
        return

    query = sa.sql.select([dhcp_table.c.extra_ifaces])
    current_ifaces = ''
    for dhcp in op.get_bind().execute(query):
        current_ifaces = dhcp.extra_ifaces

    new_ifaces = f'{ifname} {current_ifaces}'
    op.execute(dhcp_table.update().values(extra_ifaces=new_ifaces.strip()))


def downgrade():
    pass
