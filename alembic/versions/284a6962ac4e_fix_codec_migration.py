"""fix-codec-migration

Revision ID: 284a6962ac4e
Revises: 6fc79e30e8bf

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284a6962ac4e'
down_revision = '6fc79e30e8bf'

endpoint_sip_tbl = sa.sql.table(
    'endpoint_sip',
    sa.sql.column('uuid'),
    sa.sql.column('name'),
)
endpoint_sip_section_tbl = sa.sql.table(
    'endpoint_sip_section',
    sa.sql.column('uuid'),
    sa.sql.column('endpoint_sip_uuid'),
)
endpoint_sip_section_option_tbl = sa.sql.table(
    'endpoint_sip_section_option',
    sa.sql.column('uuid'),
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('endpoint_sip_section_uuid'),
)
user_sip_tbl = sa.sql.table(
    'usersip',
    sa.sql.column('name'),
    sa.sql.column('options'),
)


class NoSuchEndpoint(Exception):
    pass


def find_broken_endpoints():
    query = sa.sql.select(
        [endpoint_sip_tbl.c.name],
    ).select_from(
        endpoint_sip_tbl.join(
            endpoint_sip_section_tbl,
            endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_sip_tbl.c.uuid,
        ).join(
            endpoint_sip_section_option_tbl,
            endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == endpoint_sip_section_tbl.c.uuid,
        )
    ).where(
        endpoint_sip_section_option_tbl.c.key == 'allow',
    ).where(
        endpoint_sip_section_option_tbl.c.value == '!all,ulaw',
    )
    return [endpoint.name for endpoint in op.get_bind().execute(query)]


def get_merged_codecs(endpoint_name):
    query = sa.sql.select([
        user_sip_tbl.c.options,
    ]).where(
        user_sip_tbl.c.name == endpoint_name,
    )

    usersip = op.get_bind().execute(query).first()
    if not usersip:
        raise NoSuchEndpoint()

    codecs = []
    for key, value in usersip.options:
        if key == 'allow':
            for codec in value.split(','):
                if not codec:
                    continue

                if codec == '!all':
                    codecs = ['!all']
                else:
                    codecs.append(codec)
        elif key == 'disallow':
            for codec in value.split(','):
                if not codec:
                    continue

                if codec == 'all':
                    codecs.append('!all')
                else:
                    while codec in codecs:
                        codecs.remove(codec)

    return codecs


def update_codecs(endpoint_name, original_codecs):
    query = sa.sql.select(
        [endpoint_sip_section_option_tbl.c.uuid],
    ).select_from(
        endpoint_sip_tbl.join(
            endpoint_sip_section_tbl,
            endpoint_sip_section_tbl.c.endpoint_sip_uuid == endpoint_sip_tbl.c.uuid,
        ).join(
            endpoint_sip_section_option_tbl,
            endpoint_sip_section_option_tbl.c.endpoint_sip_section_uuid == endpoint_sip_section_tbl.c.uuid,
        )
    ).where(
        endpoint_sip_section_option_tbl.c.key == 'allow',
    ).where(
        endpoint_sip_tbl.c.name == endpoint_name,
    )
    option_uuid = op.get_bind().execute(query).first().uuid

    filter_ = endpoint_sip_section_option_tbl.c.uuid == option_uuid
    if original_codecs:
        query = endpoint_sip_section_option_tbl.update().where(filter_).values(value=','.join(original_codecs))
    else:
        query = endpoint_sip_section_option_tbl.delete().where(filter_)
    op.execute(query)


def upgrade():
    potentially_broken_endpoint_names = find_broken_endpoints()
    for endpoint_name in potentially_broken_endpoint_names:
        try:
            original_codecs = get_merged_codecs(endpoint_name)
        except NoSuchEndpoint:
            continue

        if original_codecs == '!all,ulaw':
            continue

        update_codecs(endpoint_name, original_codecs)


def downgrade():
    pass
