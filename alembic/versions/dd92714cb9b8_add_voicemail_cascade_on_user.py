"""add-voicemail-cascade-on-user

Revision ID: dd92714cb9b8
Revises: 495accfabe9f

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd92714cb9b8'
down_revision = '495accfabe9f'

FK_NAME = 'userfeatures_voicemailid_fkey'
SOURCE_TABLE_NAME = 'userfeatures'
REF_TABLE_NAME = 'voicemail'
SOURCE_COLUMN_NAME = 'voicemailid'
REF_COLUMN_NAME = 'uniqueid'


def upgrade():
    op.drop_constraint(FK_NAME, SOURCE_TABLE_NAME)
    op.create_foreign_key(
        FK_NAME,
        SOURCE_TABLE_NAME,
        REF_TABLE_NAME,
        [SOURCE_COLUMN_NAME],
        [REF_COLUMN_NAME],
        ondelete='SET NULL',
    )


def downgrade():
    op.drop_constraint(FK_NAME, SOURCE_TABLE_NAME)
    op.create_foreign_key(
        FK_NAME,
        SOURCE_TABLE_NAME,
        REF_TABLE_NAME,
        [SOURCE_COLUMN_NAME],
        [REF_COLUMN_NAME],
    )
