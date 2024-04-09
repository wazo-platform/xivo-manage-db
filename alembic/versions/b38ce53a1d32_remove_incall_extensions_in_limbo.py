"""remove-extensions-in-limbo

remove extensions from table extensions in *from-extern contexts associated with user 0
which are incall extensions disassociated from a real destination but not available for new assignments
Revision ID: b38ce53a1d32
Revises: 7a7f7c44f943

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b38ce53a1d32'
down_revision = '7a7f7c44f943'

extensions_table = sa.table(
    'extensions',
    sa.column('id'),
    sa.column('context'),
    sa.column('exten'),
    sa.column('type'),
    sa.column('typeval'),
)


def upgrade() -> None:
    query = sa.sql.select([extensions_table.c.id]).where(
        sa.and_(
            extensions_table.c.type == 'user',
            extensions_table.c.typeval == '0',
            extensions_table.c.context.ilike('%from-extern')
        )
    )
    delete_op = extensions_table.delete().where(
        extensions_table.c.id.in_(query.alias())
    )
    op.get_bind().execute(delete_op)


def downgrade() -> None:
    pass
