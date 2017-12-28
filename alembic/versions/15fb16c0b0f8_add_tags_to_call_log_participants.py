"""add_tags_to_call_log_participants

Revision ID: 15fb16c0b0f8
Revises: 27801f8c2a80

"""

# revision identifiers, used by Alembic.
revision = '15fb16c0b0f8'
down_revision = '27801f8c2a80'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('call_log_participant',
                  sa.Column('tags',
                            sa.dialects.postgresql.ARRAY(sa.String(128)),
                            nullable=False,
                            server_default='{}'))


def downgrade():
    op.drop_column('call_log_participant', 'tags')
