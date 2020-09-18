"""remove-auth-from-insecure-trunks

Revision ID: 8e09c6fde62d
Revises: 69c55f395eb7

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e09c6fde62d'
down_revision = '69c55f395eb7'

user_sip_tbl = sa.sql.table(
    'usersip',
    sa.sql.column('name'),
    sa.sql.column('category'),
    sa.sql.column('insecure'),
)
endpoint_sip_tbl = sa.sql.table(
    'endpoint_sip',
    sa.sql.column('uuid'),
    sa.sql.column('name'),
)
endpoint_sip_section_tbl = sa.sql.table(
    'endpoint_sip_section',
    sa.sql.column('uuid'),
    sa.sql.column('type'),
    sa.sql.column('endpoint_sip_uuid'),
)


def find_insecure_trunks():
    query = sa.sql.select([
        user_sip_tbl.c.name,
    ]).where(sa.and_(
        user_sip_tbl.c.category == 'trunk',
        ~user_sip_tbl.c.insecure.is_(None)
    ))
    rows = op.get_bind().execute(query)
    return [row.name for row in rows]


def find_trunk_uuid(names):
    query = sa.sql.select([
        endpoint_sip_tbl.c.uuid,
    ]).where(endpoint_sip_tbl.c.name.in_(names))
    rows = op.get_bind().execute(query)
    return [row.uuid for row in rows]


def delete_auth_sections(endpoint_uuids):
    query = endpoint_sip_section_tbl.delete().where(
        endpoint_sip_section_tbl.c.endpoint_sip_uuid.in_(endpoint_uuids)
    )
    op.execute(query)


def upgrade():
    endpoint_names = find_insecure_trunks()
    if not endpoint_names:
        return

    endpoint_uuids = find_trunk_uuid(endpoint_names)
    if not endpoint_uuids:
        return

    delete_auth_sections(endpoint_uuids)


def downgrade():
    pass
