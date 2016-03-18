"""add_foreignkey_on_rightcallexten

Revision ID: 4a1c2a87321
Revises: 198cf8fda9a4

"""

# revision identifiers, used by Alembic.
revision = '4a1c2a87321'
down_revision = '198cf8fda9a4'

from alembic import op


def upgrade():
    op.execute("DELETE FROM rightcallexten WHERE rightcallid = 0")
    op.create_foreign_key('rightcallexten_rightcallid_fkey',
                          'rightcallexten', 'rightcall',
                          ['rightcallid'], ['id'])


def downgrade():
    op.drop_constraint('rightcallexten_rightcallid_fkey', 'rightcallexten')
