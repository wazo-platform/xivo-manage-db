"""pjsip transport migration

Revision ID: fb663a210806
Revises: edca430a8373

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql
from collections import namedtuple


# revision identifiers, used by Alembic.
revision = 'fb663a210806'
down_revision = 'edca430a8373'

# Special cases
# * multiple localnet/local_net can be specified
# * the "external_signaling_address" is "externhost" OR "externip"
# * "bind" for udp and wss = "udpbindaddr"[+"bindport"]
# * "externtcpport" becomes "external_signaling_port" for the tcp_transport
# * "tcpbindaddr" becomes "bind" for tcp transport
# * transport-tcp is only generated if tcpenabled is 1
# * transport-wss is only generated if websocket_enabled is 1

# Fields that are actually "translated" by wazo-confgend
# SIP_TO_PJSIP_MAPPING = {
#     'media_address': 'external_media_address',
# }

# zcat /usr/share/doc/asterisk-doc/json/pjsip.json.gz | jq .transport[].name | sort -u
# Commented options are managed individually
# TLS only options are ignored since tls transports are not managed in confgend and do not work at the moment
VERBATIM_PJSIP_TRANSPORT_OPTIONS = [
    "allow_reload",
    "async_operations",
    "cos",
    "domain",
    "external_signaling_port",
    "password",
    "symmetric_transport",
    "tos",
    "websocket_write_timeout",
    # "bind",
    # "ca_list_file", # TLS only
    # "ca_list_path", # TLS only
    # "cert_file", # TLS only
    # "cipher", # TLS only
    # "external_media_address",
    # "external_signaling_address",
    # "local_net",
    # "method", # TLS only
    # "priv_key_file", # TLS only
    # "protocol",
    # "require_client_cert", # TLS only
    # "verify_client", # TLS only
    # "verify_server", # TLS only
]
FALSY_VALUES = ('0', 'no', 'No', 'false', 'False')
TRANSPORT_MAP = {
    'udp': 'transport-udp',
    'wss': 'transport-wss',
    'tcp': 'transport-tcp',
}

static_sip_table = sa.sql.table(
    'staticsip',
    sa.sql.column('var_metric'),
    sa.sql.column('commented'),
    sa.sql.column('filename'),
    sa.sql.column('category'),
    sa.sql.column('var_name'),
    sa.sql.column('var_val'),
)
user_sip_table = sa.sql.table(
    'usersip',
    sa.sql.column('transport'),
)
transport_table = sa.sql.table(
    'pjsip_transport',
    sa.sql.column('uuid'),
    sa.sql.column('name'),
)
transport_option_table = sa.sql.table(
    'pjsip_transport_option',
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('pjsip_transport_uuid'),
)

KV = namedtuple('KV', ['key', 'value'])


def _get_static_sip():
    query = sql.select([
        static_sip_table.c.var_name,
        static_sip_table.c.var_val,
    ]).distinct(
        static_sip_table.c.var_metric,
        static_sip_table.c.var_name,
        static_sip_table.c.var_val,
    ).where(sql.and_(
        static_sip_table.c.filename == 'sip.conf',
        static_sip_table.c.category == 'general',
        static_sip_table.c.commented == '0',
    )).order_by(
        static_sip_table.c.var_metric,
    )
    rows = op.get_bind().execute(query)
    return [KV(row.var_name, row.var_val) for row in rows]


def _get_transport_wss_options(static_sip):
    websocket_enabled = None
    for key, value in static_sip:
        if key == 'websocket_enabled':
            websocket_enabled = value

    if not websocket_enabled or websocket_enabled in FALSY_VALUES:
        return None

    migrated_options = [KV('protocol', 'wss')]
    base_udp_options = _get_base_udp_options(static_sip)
    migrated_options.extend(base_udp_options)
    return migrated_options


def _get_transport_udp_options(static_sip):
    migrated_options = [KV('protocol', 'udp')]
    base_udp_options = _get_base_udp_options(static_sip)
    migrated_options.extend(base_udp_options)
    return migrated_options


def _get_base_transport_options(static_sip):
    for old, new in TRANSPORT_MAP.items():
        op.execute(
            static_sip_table.update().where(sa.and_(
                static_sip_table.c.var_name == 'transport',
                static_sip_table.c.var_val == old,
            )).values(var_val=new)
        )
        op.execute(
            user_sip_table.update().where(
                user_sip_table.c.transport == old,
            ).values(transport=new)
        )

    migrated_options = []
    local_nets = set()
    external_signaling_address = None
    external_media_address = None

    for key, value in static_sip:
        # localnet can have one or many values "1.1.1.0/24, 1.1.2.0/24"
        if key in ('localnet', 'local_net'):
            if ',' in value:
                for local_net in value.split(','):
                    local_nets.add(local_net.strip())
            else:
                local_nets.add(value)

        # external_signaling_address OR externhost OR externip
        elif key == 'external_signaling_address':
            external_signaling_address = value
        elif key == 'externhost' and not external_signaling_address:
            external_signaling_address = value
        elif key == 'externip' and not external_signaling_address:
            external_signaling_address = value

        # external_media_address or media_address
        elif key == 'external_media_address':
            external_media_address = value
        elif key == 'media_address' and not external_media_address:
            external_media_address = value

        elif key in VERBATIM_PJSIP_TRANSPORT_OPTIONS:
            migrated_options.append(KV(key, value))

    for local_net in local_nets:
        migrated_options.append(KV('local_net', local_net))

    if external_signaling_address:
        migrated_options.append(KV('external_signaling_address', external_signaling_address))

    if external_media_address:
        migrated_options.append(KV('external_media_address', external_media_address))

    return migrated_options


def _get_base_udp_options(static_sip):
    migrated_options = _get_base_transport_options(static_sip)
    bind = None
    bindaddr = None
    bindport = None

    for key, value in static_sip:
        if key == 'udpbindaddr':
            bindaddr = value
        elif key == 'bindport':
            bindport = value
        elif key == 'bind':
            bind = value

    if bind:
        migrated_options.append(KV('bind', bind))
    elif bindaddr and bindport:
        migrated_options.append(KV('bind', '{}:{}'.format(bindaddr, bindport)))
    elif bindaddr:
        migrated_options.append(KV('bind', bindaddr))
    else:
        migrated_options.append(KV('bind', '0.0.0.0:5060'))

    return migrated_options


def _get_transport_tcp_options(static_sip):
    tcp_enabled = None
    for key, value in static_sip:
        if key == 'tcpenabled':
            tcp_enabled = value

    if not tcp_enabled or tcp_enabled in FALSY_VALUES:
        return None

    migrated_options = [KV('protocol', 'tcp')]
    external_signaling_port = None
    for key, value in static_sip:
        if key == 'external_signaling_port':
            external_signaling_port = value
        elif key == 'externtcpport' and not external_signaling_port:
            external_signaling_port = value
        elif key == 'tcpbindaddr':
            migrated_options.append(KV('bind', value))

    if external_signaling_port:
        migrated_options.append(KV('external_signaling_port', external_signaling_port))

    return migrated_options


def upgrade():
    transports = {}
    static_sip = _get_static_sip()

    transport_udp_options = _get_transport_udp_options(static_sip)
    if transport_udp_options:
        transports['transport-udp'] = transport_udp_options

    transport_wss_options = _get_transport_wss_options(static_sip)
    if transport_wss_options:
        transports['transport-wss'] = transport_wss_options

    transport_tcp_options = _get_transport_tcp_options(static_sip)
    if transport_tcp_options:
        transports['transport-tcp'] = transport_tcp_options

    for name, options in transports.items():
        query = transport_table.insert().returning(transport_table.c.uuid).values(name=name)
        transport_uuid = op.get_bind().execute(query).scalar()
        for option in options:
            query = transport_option_table.insert().values(
                key=option.key,
                value=option.value,
                pjsip_transport_uuid=transport_uuid,
            )
            op.execute(query)


def downgrade():
    op.execute(transport_table.delete())
    for old, new in TRANSPORT_MAP.items():
        op.execute(
            user_sip_table.update().where(
                user_sip_table.c.transport == new,
            ).values(transport=old)
        )
        op.execute(
            static_sip_table.update().where(sa.and_(
                static_sip_table.c.var_name == 'transport',
                static_sip_table.c.var_val == new,
            )).values(var_val=old)
        )
