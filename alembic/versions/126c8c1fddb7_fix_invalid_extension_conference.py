"""fix-invalid-extension-conference

Revision ID: 126c8c1fddb7
Revises: 0a7363700618

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '126c8c1fddb7'
down_revision = '0a7363700618'

conference_table = sql.table(
    'conference',
    sql.column('id'),
)

extensions_table = sql.table(
    'extensions',
    sql.column('id'),
    sql.column('type'),
    sql.column('typeval'),
)


def upgrade():
    query = sql.select(
        [extensions_table.c.id, extensions_table.c.typeval]
    ).where(extensions_table.c.type == 'conference')

    for extension in op.get_bind().execute(query):
        query = (
            sql.select([conference_table.c.id])
            .where(sql.cast(conference_table.c.id, sa.String) == extension.typeval)
        )
        if not op.get_bind().execute(query).scalar():
            op.execute(
                extensions_table.update()
                .where(extensions_table.c.id == extension.id)
                .values(type='user', typeval='0')
            )


def downgrade():
    pass
