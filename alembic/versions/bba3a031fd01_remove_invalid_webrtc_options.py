"""remove-invalid-webrtc-options

Revision ID: bba3a031fd01
Revises: f98e74435092

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'bba3a031fd01'
down_revision = 'f98e74435092'

sip_template_tbl = sa.sql.table(
    'endpoint_sip_template',
    sa.sql.column('child_uuid'),
    sa.sql.column('parent_uuid'),
)
sip_tbl = sa.sql.table(
    'endpoint_sip',
    sa.sql.column('uuid'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('template'),
)
sip_section_tbl = sa.sql.table(
    'endpoint_sip_section',
    sa.sql.column('uuid'),
    sa.sql.column('type'),
    sa.sql.column('endpoint_sip_uuid'),
)
sip_section_option_tbl = sa.sql.table(
    'endpoint_sip_section_option',
    sa.sql.column('uuid'),
    sa.sql.column('key'),
    sa.sql.column('endpoint_sip_section_uuid'),
)
tenant_tbl = sa.sql.table(
    'tenant',
    sa.sql.column('uuid'),
    sa.sql.column('webrtc_sip_template_uuid'),
)


def upgrade():
    delete_keys = ['dtls_verify', 'dtls_cert_file', 'dtls_private_key']
    query = (
        sip_section_option_tbl
        .delete()
        .where(
            sa.sql.and_(
                sip_section_option_tbl.c.key.in_(delete_keys),
                sip_section_option_tbl.c.endpoint_sip_section_uuid.in_(
                    sa.sql.select([sip_section_tbl.c.uuid])
                    .select_from(
                        sip_section_tbl
                        .join(
                            sip_tbl,
                            sip_tbl.c.uuid == sip_section_tbl.c.endpoint_sip_uuid,
                        )
                        .join(
                            sip_template_tbl,
                            sip_tbl.c.uuid == sip_template_tbl.c.child_uuid,
                        )
                        .join(
                            tenant_tbl,
                            tenant_tbl.c.webrtc_sip_template_uuid == sip_template_tbl.c.parent_uuid,
                        )
                    )
                    .where(
                        sa.sql.and_(
                            sip_tbl.c.template.is_(False),
                            sip_section_tbl.c.type == 'endpoint',
                        )
                    )
                )
            )
        )
    )
    op.execute(query)


def downgrade():
    pass
