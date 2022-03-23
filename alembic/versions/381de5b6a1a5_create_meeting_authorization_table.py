"""create meeting authorization table

Revision ID: 381de5b6a1a5
Revises: 21b72c41eb6a

"""

import datetime
import sqlalchemy as sa

from alembic import op
from sqlalchemy.types import DateTime

from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '381de5b6a1a5'
down_revision = '21b72c41eb6a'


def upgrade():
    op.create_table(
        'meeting_authorization',
        sa.Column(
            'uuid',
            UUID,
            server_default=sa.text('uuid_generate_v4()'),
            primary_key=True
        ),
        sa.Column(
            'meeting_uuid',
            UUID,
            sa.ForeignKey('meeting.uuid', ondelete='CASCADE'),
            nullable=False,
        ),
        sa.Column(
            'guest_uuid',
            UUID,
            nullable=False,
        ),
        sa.Column('guest_name', sa.Text),
        sa.Column('status', sa.Text),
        sa.Column(
            'created_at',
            DateTime(timezone=True),
            default=datetime.datetime.utcnow,
            server_default=sa.text("(now() at time zone 'utc')")
        )
    )


def downgrade():
    op.drop_table('meeting_authorization')
