"""add_voicemail_foreign_key

Revision ID: 1d4b487e4d1f
Revises: 3a0ace87fc76

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '1d4b487e4d1f'
down_revision = '3a0ace87fc76'


def upgrade():
    op.execute("UPDATE userfeatures SET voicemaild = NULL WHERE voicemailid = 0")
    op.create_foreign_key('userfeatures_voicemailid_fkey',
                          'userfeatures', 'voicemail',
                          ['voicemailid'], ['uniqueid'])


def downgrade():
    op.drop_constraint('userfeatures_voicemailid_fkey', 'userfeatures')
