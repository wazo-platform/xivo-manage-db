"""remove voicemail redundancy

Revision ID: 30564ea14542
Revises: 41f6ef3f00fe

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '30564ea14542'
down_revision = '41f6ef3f00fe'


def upgrade():
    op.drop_column('userfeatures', 'voicemailtype')
    op.drop_column('usersip', 'mailbox')
    op.drop_column('sccpdevice', 'voicemail')
    op.execute("DROP TYPE IF EXISTS userfeatures_voicemailtype")


def downgrade():
    op.add_column('userfeatures',
                  sa.Column('voicemailtype',
                            sa.Enum('asterisk', 'exchange',
                                    name='userfeatures_voicemailtype')))

    op.add_column('usersip', sa.Column('mailbox', sa.String(80)))
    op.add_column('sccpdevice',
                  sa.Column('voicemail',
                            sa.String(80), nullable=False, server_default=''))
