"""fix-register-transports

Revision ID: 4c660492b365
Revises: 86c17bf55b92

"""

import re
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c660492b365'
down_revision = '86c17bf55b92'

# Regex copied from wazo-confd
REGISTER_REGEX = re.compile(
    r'''^
    (?:(?P<transport>.*)://)?
    (?P<sip_username>[^:/]*)
    (?::(?P<auth_password>[^:/]*))?
    (?::(?P<auth_username>[^:/]*))?
    @
    (?P<remote_host>[^:~/]*)
    (?::(?P<remote_port>\d*))?
    (?:/(?P<callback_extension>[^~]*))?
    (?:~(?P<expiration>\d*))?
    $''',
    re.VERBOSE,
)

static_sip_table = sa.sql.table(
    'staticsip',
    sa.sql.column('id'),
    sa.sql.column('filename'),
    sa.sql.column('category'),
    sa.sql.column('var_name'),
    sa.sql.column('var_val'),
)

transport_table = sa.sql.table(
    'pjsip_transport',
    sa.sql.column('name'),
)

def _get_existing_transport_names():
    query = sa.sql.select([transport_table.c.name])
    rows = op.get_bind().execute(query)
    return [row[0] for row in rows]


def _get_registers():
    query = sa.sql.select(
        [static_sip_table.c.id, static_sip_table.c.var_val]
    ).where(sa.sql.and_(
        static_sip_table.c.filename == 'sip.conf',
        static_sip_table.c.category == 'general',
        static_sip_table.c.var_name == 'register',
    ))
    rows = op.get_bind().execute(query)
    return [(row[0], row[1]) for row in rows]


def upgrade():
    configured_transport_names = _get_existing_transport_names()
    registers = _get_registers()
    for id_, url in registers:
        matches = REGISTER_REGEX.match(url)
        result = matches.groupdict()
        transport_name = result['transport']
        if not transport_name:
            continue

        if transport_name in configured_transport_names:
            continue

        new_name = 'transport-{}'.format(transport_name)
        if new_name not in configured_transport_names:
            raise Exception(
                'cannot migrate the SIP register {} no matching transport {}'.format(
                    url, configured_transport_names
                )
            )

        new_url = url.replace(transport_name, new_name, 1)
        op.execute(
            static_sip_table.update().where(
                static_sip_table.c.id == id_
            ).values(var_val=new_url)
        )


def downgrade():
    pass
