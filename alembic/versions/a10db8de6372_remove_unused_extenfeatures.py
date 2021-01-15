"""remove-unused-extenfeatures

Revision ID: a10db8de6372
Revises: dfd6c02443cc

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a10db8de6372'
down_revision = 'dfd6c02443cc'

DEPRECATED_FEATURES = [
    'callconference',
    'callgroup',
    'callqueue',
    'calluser',
]

extensions_tbl = sa.sql.table(
    'extensions',
    sa.sql.column('context'),
    sa.sql.column('type'),
    sa.sql.column('typeval'),
)


def upgrade():
    query = (
        extensions_tbl.delete()
        .where(extensions_tbl.c.context == 'xivo-features')
        .where(extensions_tbl.c.type == 'extenfeatures')
        .where(extensions_tbl.c.typeval.in_(DEPRECATED_FEATURES))
    )
    op.execute(query)


def downgrade():
    pass
