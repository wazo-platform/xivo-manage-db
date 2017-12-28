"""fix the reverse directory

Revision ID: 672a6918b7f9
Revises: 438cb372df48

"""

# revision identifiers, used by Alembic.
revision = '672a6918b7f9'
down_revision = '438cb372df48'

from sqlalchemy import sql
from alembic import op

cti_reverse = sql.table(
    'ctireversedirectories',
    sql.column('id'),
    sql.column('directories'),
)

BROKEN = '[wazophonebook]'
FIXED = '["wazophonebook"]'


def upgrade():
    _update_directories(BROKEN, FIXED)


def downgrade():
    _update_directories(FIXED, BROKEN)


def _update_directories(old, new):
    op.execute(
        cti_reverse
        .update()
        .where(cti_reverse.c.directories == old)
        .values({'directories': new}))
