"""add default sccp provisioning values

Revision ID: 6a08e32fadba
Revises: 34748356e196

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a08e32fadba'
down_revision = '34748356e196'

TABLE_NAME = 'sccpgeneralsettings'
SCCP_GENERAL_SETTINGS_TABLE = sa.sql.table(
    TABLE_NAME,
    sa.sql.column('option_name'),
    sa.sql.column('option_value'),
)
DEFAULT_CONFIG = {
    'guest': 'no',
    'max_guests': '100',
}


def upgrade():
    values = [{'option_name': name, 'option_value': value} for name, value in DEFAULT_CONFIG.iteritems()]
    op.bulk_insert(SCCP_GENERAL_SETTINGS_TABLE, values)


def downgrade():
    query = SCCP_GENERAL_SETTINGS_TABLE.delete().where(
        SCCP_GENERAL_SETTINGS_TABLE.c.option_name.in_(DEFAULT_CONFIG.keys())
    )
    op.execute(query)
