"""rename xivo-auth to wazo-auth

Revision ID: 412b6135f650
Revises: 5c8dc069cfd7

"""

# revision identifiers, used by Alembic.
revision = '412b6135f650'
down_revision = '5c8dc069cfd7'

from alembic import op
import sqlalchemy as sa

webservice = sa.sql.table('accesswebservice',
                          sa.sql.column('name'),
                          sa.sql.column('login'))

OLD_NAME = 'xivo-auth'
NEW_NAME = 'wazo-auth'


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
