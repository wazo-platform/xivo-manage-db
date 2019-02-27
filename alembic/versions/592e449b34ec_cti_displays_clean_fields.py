"""cti_displays clean fields

Revision ID: 592e449b34ec
Revises: 2bb6543883a6

"""

# revision identifiers, used by Alembic.
revision = '592e449b34ec'
down_revision = '2bb6543883a6'

import re

from alembic import op
from sqlalchemy import sql
from functools import partial

t = sql.table('ctidisplays',
              sql.column('id'),
              sql.column('data'))


def sub_all(pattern, repl, string):
    r = re.compile(pattern)
    while True:
        string, n = r.subn(repl, string)
        if not n:
            return string


def upgrade():
    conn = op.get_bind()
    rows = conn.execute(sql.select([t]))

    f = partial(sub_all, r'(.*)\{\w+-(\w+)\}(.*)', r'\1\2\3')
    to_upgrade = {row.id: f(row.data) for row in rows}

    for id_, value in to_upgrade.items():
        op.execute(t.update()
                   .where(t.c.id == id_)
                   .values(data=value))


def downgrade():
    pass
