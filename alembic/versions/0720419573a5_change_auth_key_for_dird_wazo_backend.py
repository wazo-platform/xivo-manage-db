"""change auth key for dird wazo backend

Revision ID: 0720419573a5
Revises: 02361b8a4b7c

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0720419573a5'
down_revision = '02361b8a4b7c'

directories_table = sa.sql.table(
    'directories',
    sa.sql.column('dirtype'),
    sa.sql.column('auth_key_file'),
)


def upgrade():
    op.execute(
        directories_table
        .update()
        .where(directories_table.c.dirtype == 'wazo')
        .values(auth_key_file='/var/lib/wazo-auth-keys/wazo-dird-wazo-backend-key.yml')
    )


def downgrade():
    op.execute(
        directories_table
        .update()
        .where(directories_table.c.dirtype == 'wazo')
        .values(auth_key_file='/var/lib/wazo-auth-keys/wazo-dird-xivo-backend-key.yml')
    )
