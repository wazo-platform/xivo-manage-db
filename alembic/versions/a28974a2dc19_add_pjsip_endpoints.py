"""add pjsip endpoints

Revision ID: a28974a2dc19
Revises: d47f295009dd

"""

from alembic import op
from sqlalchemy import Boolean, Column, Text, ForeignKey as FK, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = 'a28974a2dc19'
down_revision = 'd47f295009dd'

UUID_GEN = 'uuid_generate_v4()'
RANDOM_NAME = 'substring(md5(random()::text), 0, 9)'


def upgrade():
    op.create_table(
        'endpoint_sip_section',
        Column('uuid', UUID, server_default=text(UUID_GEN), primary_key=True),
    )
    op.create_table(
        'endpoint_sip_section_option',
        Column('uuid', UUID, server_default=text(UUID_GEN), primary_key=True),
        Column('key', Text, nullable=False),
        Column('value', Text, nullable=False),
        Column(
            'endpoint_sip_section_uuid',
            UUID,
            FK('endpoint_sip_section.uuid', ondelete='CASCADE'),
            nullable=False
        ),
    )
    op.create_table(
        'endpoint_sip',
        Column('uuid', UUID, server_default=text(UUID_GEN), primary_key=True),
        Column('display_name', Text),
        Column('name', Text, server_default=text(RANDOM_NAME), nullable=False),
        Column('asterisk_id', Text),
        Column('tenant_uuid', String(36), FK('tenant.uuid', ondelete='CASCADE'), nullable=False),
        Column('aor_section_uuid', UUID, FK('endpoint_sip_section.uuid')),
        Column('auth_section_uuid', UUID, FK('endpoint_sip_section.uuid')),
        Column('endpoint_section_uuid', UUID, FK('endpoint_sip_section.uuid')),
        Column('identify_section_uuid', UUID, FK('endpoint_sip_section.uuid')),
        Column('registration_section_uuid', UUID, FK('endpoint_sip_section.uuid')),
        Column('registration_outbound_auth_section_uuid', UUID, FK('endpoint_sip_section.uuid')),
        Column('outbound_auth_section_uuid', UUID, FK('endpoint_sip_section.uuid')),
        Column('transport_uuid', UUID, FK('pjsip_transport.uuid')),
        Column('context_id', Integer, FK('context.id')),
        Column('template', Boolean, server_default=text('false')),
    )
    op.create_table(
        'endpoint_sip_parent',
        Column('child_uuid', UUID, FK('endpoint_sip.uuid', ondelete='CASCADE'), primary_key=True),
        Column('parent_uuid', UUID, FK('endpoint_sip.uuid', ondelete='CASCADE'), primary_key=True),
    )
    op.add_column(
        'linefeatures',
        Column('endpoint_sip_uuid', UUID, FK('endpoint_sip.uuid', ondelete='SET NULL')),
    )
    op.add_column(
        'trunkfeatures',
        Column('endpoint_sip_uuid', UUID, FK('endpoint_sip.uuid', ondelete='SET NULL')),
    )


def downgrade():
    op.drop_column('trunkfeatures', 'endpoint_sip_uuid')
    op.drop_column('linefeatures', 'endpoint_sip_uuid')
    op.drop_table('endpoint_sip_parent')
    op.drop_table('endpoint_sip')
    op.drop_table('endpoint_sip_section_option')
    op.drop_table('endpoint_sip_section')
