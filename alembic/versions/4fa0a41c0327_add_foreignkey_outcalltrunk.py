"""add_foreignkey_outcalltrunk

Revision ID: 4fa0a41c0327
Revises: 4fd0315a61fc

"""

# revision identifiers, used by Alembic.
revision = '4fa0a41c0327'
down_revision = '4fd0315a61fc'

from alembic import op


def upgrade():
    op.create_foreign_key('outcalltrunk_outcallid_fkey',
                          'outcalltrunk', 'outcall',
                          ['outcallid'], ['id'])
    op.create_foreign_key('outcalltrunk_trunkfeaturesid_fkey',
                          'outcalltrunk', 'trunkfeatures',
                          ['trunkfeaturesid'], ['id'])
    op.alter_column('outcalltrunk', 'outcallid', server_default=None)
    op.alter_column('outcalltrunk', 'trunkfeaturesid', server_default=None)


def downgrade():
    op.drop_constraint('outcalltrunk_outcallid_fkey', 'outcalltrunk')
    op.drop_constraint('outcalltrunk_trunkfeaturesid_fkey', 'outcalltrunk')
    op.alter_column('outcalltrunk', 'outcallid', server_default='0')
    op.alter_column('outcalltrunk', 'trunkfeaturesid', server_default='0')
