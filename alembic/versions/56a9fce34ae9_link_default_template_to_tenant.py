"""link_default_template_to_tenant

Revision ID: 56a9fce34ae9
Revises: ee773d263d87

"""

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '56a9fce34ae9'
down_revision = 'ee773d263d87'


def upgrade():
    op.add_column(
        'tenant',
        sa.Column('sip_templates_generated', sa.Boolean, nullable=False, server_default='false'),
    )
    op.add_column(
        'tenant',
        sa.Column(
            'global_sip_template_uuid',
            UUID,
            sa.ForeignKey('endpoint_sip.uuid', ondelete='SET NULL'),
        ),
    )
    op.add_column(
        'tenant',
        sa.Column(
            'webrtc_sip_template_uuid',
            UUID,
            sa.ForeignKey('endpoint_sip.uuid', ondelete='SET NULL'),
        ),
    )
    op.add_column(
        'tenant',
        sa.Column(
            'global_trunk_sip_template_uuid',
            UUID,
            sa.ForeignKey('endpoint_sip.uuid', ondelete='SET NULL'),
        ),
    )
    op.add_column(
        'tenant',
        sa.Column(
            'twilio_trunk_sip_template_uuid',
            UUID,
            sa.ForeignKey('endpoint_sip.uuid', ondelete='SET NULL'),
        ),
    )


def downgrade():
    op.drop_column('tenant', 'sip_templates_generated')
    op.drop_column('tenant', 'global_sip_template_uuid')
    op.drop_column('tenant', 'webrtc_sip_template_uuid')
    op.drop_column('tenant', 'global_trunk_sip_template_uuid')
    op.drop_column('tenant', 'twilio_trunk_sip_template_uuid')
