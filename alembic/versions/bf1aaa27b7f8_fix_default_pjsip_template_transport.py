"""fix-default-pjsip-template-transport

Revision ID: bf1aaa27b7f8
Revises: 73166af50deb

"""

from alembic import op
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = 'bf1aaa27b7f8'
down_revision = '73166af50deb'

transport_tbl = sql.table(
    'pjsip_transport',
    sql.column('uuid'),
    sql.column('name'),
)
sip_tbl = sql.table(
    'endpoint_sip',
    sql.column('uuid'),
    sql.column('transport_uuid'),
)
tenant_tbl = sql.table(
    'tenant',
    sql.column('uuid'),
    sql.column('global_sip_template_uuid'),
    sql.column('webrtc_sip_template_uuid'),
)


def upgrade():
    query = sql.select([transport_tbl.c.uuid]).where(transport_tbl.c.name == 'transport-udp')
    transport_udp = op.get_bind().execute(query).first()
    if transport_udp:
        query = (
            sip_tbl
            .update()
            .values(transport_uuid=transport_udp.uuid)
            .where(
                sip_tbl.c.uuid.in_(
                    sql.select([sip_tbl.c.uuid])
                    .select_from(
                        sip_tbl
                        .join(
                            tenant_tbl,
                            tenant_tbl.c.global_sip_template_uuid == sip_tbl.c.uuid,
                        )
                    )
                    .where(sip_tbl.c.transport_uuid.is_(None))
                )
            )
        )
        op.execute(query)

    query = sql.select([transport_tbl.c.uuid]).where(transport_tbl.c.name == 'transport-wss')
    transport_wss = op.get_bind().execute(query).first()
    if transport_wss:
        query = (
            sip_tbl
            .update()
            .values(transport_uuid=transport_wss.uuid)
            .where(
                sip_tbl.c.uuid.in_(
                    sql.select([sip_tbl.c.uuid])
                    .select_from(
                        sip_tbl
                        .join(
                            tenant_tbl,
                            tenant_tbl.c.webrtc_sip_template_uuid == sip_tbl.c.uuid,
                        )
                    )
                    .where(sip_tbl.c.transport_uuid.is_(None))
                )
            )
        )
        op.execute(query)


def downgrade():
    pass
