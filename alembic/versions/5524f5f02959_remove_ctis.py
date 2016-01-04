"""remove ctis

Revision ID: 5524f5f02959
Revises: 1d4b487e4d1f

"""

# revision identifiers, used by Alembic.
revision = '5524f5f02959'
down_revision = '1d4b487e4d1f'

from alembic import op


def upgrade():
    op.drop_column('ctimain', 'commandset')
    op.drop_column('ctimain', 'ctis_port')
    op.drop_column('ctimain', 'ctis_ip')


def downgrade():
    pass
