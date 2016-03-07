"""remove_invalid_chars_from_label

Revision ID: 7f1c1c00662
Revises: 53ce4ff6ffe9

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '7f1c1c00662'
down_revision = '53ce4ff6ffe9'

fk_mapping = sql.table('func_key_mapping',
                       sql.column('label'))

dest_custom = sql.table('func_key_dest_custom',
                        sql.column('exten'))

dest_forward = sql.table('func_key_dest_forward',
                         sql.column('number'))


INVALID_CHARS = "\n\r\t;"


def upgrade():
    query = (fk_mapping
             .update()
             .values(
                 label=sql.func.translate(fk_mapping.c.label,
                                          INVALID_CHARS,
                                          ''))
             .where(
                 fk_mapping.c.label != None)  # noqa
             )
    op.execute(query)

    query = (dest_custom
             .update()
             .values(
                 exten=sql.func.translate(dest_custom.c.exten,
                                          INVALID_CHARS,
                                          ''))
             )
    op.execute(query)

    query = (dest_forward
             .update()
             .values(
                 number=sql.func.translate(dest_forward.c.number,
                                          INVALID_CHARS,
                                          ''))
             .where(
                 dest_forward.c.number != None)  # noqa
             )
    op.execute(query)


def downgrade():
    pass
