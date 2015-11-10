"""fix-default-display-personal

Revision ID: 498f0570ffef
Revises: 320d05ebad29

"""

# revision identifiers, used by Alembic.
revision = '498f0570ffef'
down_revision = '320d05ebad29'

import json

from alembic import op
from sqlalchemy import sql

cti_displays = sql.table('ctidisplays',
                         sql.column('id'),
                         sql.column('name'),
                         sql.column('data'))

DISPLAY_COLUMN_TYPE_INDEX = 1


def upgrade():
    conn = op.get_bind()
    _fix_personal_typos(conn)


def downgrade():
    pass


def _fix_personal_typos(conn):
    display_rows = conn.execute(sql.select([cti_displays]))
    for display_row in display_rows:
        display_config = _get_display_config(display_row)
        display_config = _fix_display_config(display_config)
        op.execute(cti_displays
                   .update()
                   .where(cti_displays.c.id == display_row.id)
                   .values(data=json.dumps(display_config)))


def _fix_display_config(display_config):
    display_config = dict(display_config)
    for display_priority in display_config:
        if len(display_config[display_priority]) < (DISPLAY_COLUMN_TYPE_INDEX + 1):
            continue
        if display_config[display_priority][DISPLAY_COLUMN_TYPE_INDEX] == 'personnal':
            display_config[display_priority][DISPLAY_COLUMN_TYPE_INDEX] = 'personal'
    return display_config


def _get_display_config(display):
    return json.loads(display.data) if display.data else {}
