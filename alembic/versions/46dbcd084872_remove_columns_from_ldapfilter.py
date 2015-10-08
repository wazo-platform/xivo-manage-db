"""remove columns from ldapfilter

Revision ID: 46dbcd084872
Revises: 1493335e754b

"""

# revision identifiers, used by Alembic.
revision = '46dbcd084872'
down_revision = '1493335e754b'

from alembic import op


def upgrade():
    op.drop_column('ldapfilter', 'attrdisplayname')
    op.drop_column('ldapfilter', 'attrphonenumber')
    op.drop_column('ldapfilter', 'additionaltype')
    op.drop_column('ldapfilter', 'additionaltext')
    op.execute('DROP TYPE ldapfilter_additionaltype')


def downgrade():
    pass
