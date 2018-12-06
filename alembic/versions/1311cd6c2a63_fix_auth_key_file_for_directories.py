"""fix-auth-key-file-for-directories

Revision ID: 1311cd6c2a63
Revises: 71c41130380e

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '1311cd6c2a63'
down_revision = '71c41130380e'

directories = sa.sql.table(
    'directories',
    sa.sql.column('dirtype'),
    sa.sql.column('xivo_username'),
    sa.sql.column('xivo_password'),
    sa.sql.column('auth_key_file'),
)


def _set_default_auth_key_file():
    query = (
        directories.update()
        .where(
            sql.and_(
                directories.c.dirtype == 'xivo',
                directories.c.xivo_username == 'wazo-dird-xivo-backend',
            )
        )
        .values(
            auth_key_file='/var/lib/wazo-auth-keys/wazo-dird-xivo-backend-key.yml',
            xivo_password=None,
        )
    )
    op.execute(query)


def upgrade():
    _set_default_auth_key_file()


def downgrade():
    pass
