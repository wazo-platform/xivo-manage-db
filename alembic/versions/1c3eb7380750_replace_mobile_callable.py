"""number types migration

Revision ID: 1c3eb7380750
Revises: 30564ea14542

"""

# revision identifiers, used by Alembic.
revision = '1c3eb7380750'
down_revision = '30564ea14542'

import json

from alembic import op
from sqlalchemy import sql

cti_displays = sql.table('ctidisplays',
                         sql.column('id'),
                         sql.column('data'))


def _get_display_config(display):
    return json.loads(display.data) if display.data else {}


def upgrade():
    rows = op.get_bind().execute(sql.select([cti_displays]))
    for row in rows:
        id_, config = row.id, _get_display_config(row)
        new_config = {}
        number_count = 0
        for key, value in config.items():
            new_value = list(value)

            # the type phone did not do anything but it was in the old default display
            if new_value[1] == 'phone':
                new_value[1] = 'number'

            # the mobile type is now callable
            if new_value[1] == 'mobile':
                new_value[1] = 'callable'

            # if there is more than one number, make the others callable
            if new_value[1] == 'number':
                number_count += 1
                if number_count > 1:
                    new_value[1] = 'callable'

            new_config[key] = new_value

        if new_config != config:
            op.execute(cti_displays
                       .update()
                       .values(data=json.dumps(new_config))
                       .where(cti_displays.c.id == id_))


def downgrade():
    pass
