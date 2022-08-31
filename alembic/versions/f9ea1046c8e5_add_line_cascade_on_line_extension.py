"""add-line-cascade-on-line-extension

Revision ID: f9ea1046c8e5
Revises: f1518ec4da82

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9ea1046c8e5'
down_revision = 'f1518ec4da82'

FK_NAME = 'line_extension_line_id_fkey'
SOURCE_TABLE_NAME = 'line_extension'
REF_TABLE_NAME = 'linefeatures'
SOURCE_COLUMN_NAME = 'line_id'
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
