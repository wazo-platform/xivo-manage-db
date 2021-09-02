"""add the meeting table

Revision ID: 706a7655606e
Revises: 3edd3b3aac7d

"""

from sqlalchemy.sql.schema import ForeignKey
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '706a7655606e'
down_revision = '3edd3b3aac7d'


def upgrade():
    op.create_table(
        'meeting',
        sa.Column('uuid', UUID, server_default=sa.text('uuid_generate_v4()'), primary_key=True),
        sa.Column('name', sa.Text),
        sa.Column(
            'guest_endpoint_sip_uuid',
            UUID,
            sa.ForeignKey('endpoint_sip.uuid', ondelete='SET NULL'),
        ),
        sa.Column(
            'tenant_uuid',
            sa.String(36),
            sa.ForeignKey('tenant.uuid', ondelete='CASCADE'),
            nullable=False,
        )
    )

    op.create_table(
        'meeting_owner',
        sa.Column(
            'meeting_uuid',
            UUID,
            sa.ForeignKey('meeting.uuid', ondelete='CASCADE'),
            primary_key=True,
        ),
        sa.Column(
            'user_uuid',
            sa.String(38),  # 38 is the length of the userfeatures.uuid field
            sa.ForeignKey('userfeatures.uuid', ondelete='CASCADE'),
            primary_key=True,
        ),
    )


def downgrade():
    op.drop_table('meeting_owner')
    op.drop_table('meeting')
