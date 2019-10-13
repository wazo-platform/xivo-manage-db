"""fix_invalid_extension_parking_lot

Revision ID: c3ecaf2f9e78
Revises: 732a9b6500da

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = 'c3ecaf2f9e78'
down_revision = '732a9b6500da'

parking_lot_table = sql.table(
    'parking_lot',
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
    ).where(extensions_table.c.type == 'parking')

    for extension in op.get_bind().execute(query):
        query = (
            sql.select([parking_lot_table.c.id])
            .where(sql.cast(parking_lot_table.c.id, sa.String) == extension.typeval)
        )
        if not op.get_bind().execute(query).scalar():
            op.execute(
                extensions_table.update()
                .where(extensions_table.c.id == extension.id)
                .values(type='user', typeval='0')
            )


def downgrade():
    pass
