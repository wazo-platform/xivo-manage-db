"""remove outbound-auth key

Revision ID: 330b1c94980d
Revises: c1d845eb61b4

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '330b1c94980d'
down_revision = 'c1d845eb61b4'

endpoint_sip_section_option_tbl = sa.sql.table(
    'endpoint_sip_section_option',
    sa.sql.column('key'),
)

def upgrade():
    query = endpoint_sip_section_option_tbl.delete().where(
        endpoint_sip_section_option_tbl.c.key == 'outbound_auth',
    )
    op.execute(query)


def downgrade():
    pass
