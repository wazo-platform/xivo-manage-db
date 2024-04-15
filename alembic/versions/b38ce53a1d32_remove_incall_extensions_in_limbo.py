"""remove-extensions-in-limbo

remove extensions from table extensions from incall contexts associated with user 0,
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


context_table = sa.table(
    'context',
    sa.column('id'),
    sa.column('name'),
    sa.column('contexttype'),
)


def upgrade() -> None:
    delete_op = extensions_table.delete().where(
        sa.and_(
            extensions_table.c.context == context_table.c.name,
            extensions_table.c.type == 'user',
            extensions_table.c.typeval == '0',
            context_table.c.contexttype == 'incall'
        )
    )
    op.get_bind().execute(delete_op)


def downgrade() -> None:
    pass
