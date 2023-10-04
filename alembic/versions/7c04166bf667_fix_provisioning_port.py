"""fix provisioning port

Revision ID: 7c04166bf667
Revises: 30c3152833be

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c04166bf667'
down_revision = '30c3152833be'


def _upgrade_provisioning_port(new_port):
    prov_tbl = sa.sql.table('provisioning', sa.sql.column('http_port'))
    query = prov_tbl.update().values(http_port=new_port)
    op.get_bind().execute(query)


def upgrade():
    _upgrade_provisioning_port(8667)


def downgrade():
    _upgrade_provisioning_port(18667)
