"""rename_xivo_agentd_to_wazo_agentd

Revision ID: 35898c88f637
Revises: 4fe20686380b

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35898c88f637'
down_revision = '4fe20686380b'


webservice = sa.sql.table('accesswebservice',
                          sa.sql.column('name'),
                          sa.sql.column('login'))

OLD_NAME = 'xivo-agentd-cli'
NEW_NAME = 'wazo-agentd-cli'


def rename_webservice_access(old_name, new_name):
    op.execute(
        webservice.update(
        ).values(
            name=new_name,
            login=new_name,
        ).where(
            webservice.c.name == old_name,
        )
    )


def upgrade():
    rename_webservice_access(OLD_NAME, NEW_NAME)


def downgrade():
    rename_webservice_access(NEW_NAME, OLD_NAME)
