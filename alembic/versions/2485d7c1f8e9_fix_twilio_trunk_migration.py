"""fix-twilio-trunk-migration

Revision ID: 2485d7c1f8e9
Revises: 8e09c6fde62d

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2485d7c1f8e9'
down_revision = '8e09c6fde62d'


tenant_tbl = sa.sql.table(
    'tenant',
    sa.sql.column('uuid'),
    sa.sql.column('twilio_trunk_sip_template_uuid'),
    sa.sql.column('sip_templates_generated'),
)
trunk_tbl = sa.sql.table(
    'trunkfeatures',
    sa.sql.column('endpoint_sip_uuid'),
    sa.sql.column('twilio_incoming'),
)
endpoint_sip_template_tbl = sa.sql.table(
    'endpoint_sip_template',
    sa.sql.column('child_uuid'),
    sa.sql.column('parent_uuid'),
)


def find_twilio_template_uuid():
    query = sa.sql.select(
        [tenant_tbl.c.twilio_trunk_sip_template_uuid]
    ).where(
        tenant_tbl.c.sip_templates_generated.is_(True),
    )
    return [row.twilio_trunk_sip_template_uuid for row in op.get_bind().execute(query)]


def find_twilio_endpoints():
    query = sa.sql.select(
        [trunk_tbl.c.endpoint_sip_uuid],
    ).where(
        trunk_tbl.c.twilio_incoming.is_(True)
    )
    return [row.endpoint_sip_uuid for row in op.get_bind().execute(query)]


def dissociate_non_twilio_trunks(twilio_endpoint_uuids, twilio_templates):
    query = endpoint_sip_template_tbl.delete().where(sa.and_(
        endpoint_sip_template_tbl.c.parent_uuid.in_(twilio_templates),
        ~endpoint_sip_template_tbl.c.child_uuid.in_(twilio_endpoint_uuids),
    ))
    op.execute(query)


def upgrade():
    twilio_template_uuids = find_twilio_template_uuid()
    twilio_endpoint_uuids = find_twilio_endpoints()
    dissociate_non_twilio_trunks(twilio_endpoint_uuids, twilio_template_uuids)


def downgrade():
    pass
