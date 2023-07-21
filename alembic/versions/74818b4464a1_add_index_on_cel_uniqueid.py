"""add index on cel.uniqueid

Revision ID: 74818b4464a1
Revises: 77b84b162634

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74818b4464a1'
down_revision = '77b84b162634'


TABLE_NAME = 'cel'
ON_COLUMN = 'uniqueid'
INDEX_NAME = f'{TABLE_NAME}__idx__{ON_COLUMN}'


def _check_index_exists(index_name):
    conn = op.get_bind()
    result = conn.execute(
        "SELECT exists(SELECT 1 from pg_indexes where indexname = '{}') as ix_exists;".format(
            index_name
        )
    ).first()
    return result.ix_exists


def upgrade():
    if not _check_index_exists(INDEX_NAME):
        op.create_index(
            index_name=INDEX_NAME,
            table_name=TABLE_NAME,
            columns=[ON_COLUMN],
        )


def downgrade():
    op.drop_index(INDEX_NAME)
