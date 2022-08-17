"""add-extension-cascade-on-line-extension

Revision ID: f1518ec4da82
Revises: e53b8ab083c0

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1518ec4da82'
down_revision = 'e53b8ab083c0'

FK_NAME = 'line_extension_extension_id_fkey'
SOURCE_TABLE_NAME = 'line_extension'
REF_TABLE_NAME = 'extensions'
SOURCE_COLUMN_NAME = 'extension_id'
REF_COLUMN_NAME = 'id'


def upgrade():
    op.drop_constraint(FK_NAME, SOURCE_TABLE_NAME)
    op.create_foreign_key(
        FK_NAME,
        SOURCE_TABLE_NAME,
        REF_TABLE_NAME,
        [SOURCE_COLUMN_NAME],
        [REF_COLUMN_NAME],
        ondelete='CASCADE',
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
