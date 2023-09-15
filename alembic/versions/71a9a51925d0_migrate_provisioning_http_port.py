"""migrate provisioning http port

Revision ID: 71a9a51925d0
Revises: 8005d5787610

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71a9a51925d0'
down_revision = '8005d5787610'


def _upgrade_provisioning_port(new_port):
    prov_tbl = sa.sql.table('provisioning', sa.sql.column('http_port'))
    query = prov_tbl.update().values(http_port=new_port)
    op.get_bind().execute(query)


def upgrade():
    _upgrade_provisioning_port(18667)


def downgrade():
    _upgrade_provisioning_port(8667)
