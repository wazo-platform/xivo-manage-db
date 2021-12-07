"""add the meetingjoin extenfeatures

Revision ID: 2b51ff81d388
Revises: 55cd08a0dae2

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b51ff81d388'
down_revision = '55cd08a0dae2'

extensions_table = sa.sql.table(
    'extensions',
    sa.sql.column('context'),
    sa.sql.column('exten'),
    sa.sql.column('type'),
    sa.sql.column('typeval'),
)
FEATURE_NAME = 'meetingjoin'


def upgrade():
    insert_query = extensions_table.insert().values(
        context='xivo-features',
        exten='_*41.',
        type='extenfeatures',
        typeval=FEATURE_NAME,
    )
    op.get_bind().execute(insert_query)


def downgrade():
    query = (extensions_table
        .delete()
        .where(
            sa.sql.and_(
                extensions_table.c.type == 'extenfeatures',
                extensions_table.c.typeval == FEATURE_NAME,
            )
        )
    )
    op.get_bind().execute(query)
