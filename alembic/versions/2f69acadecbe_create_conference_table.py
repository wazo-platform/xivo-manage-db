"""create_conference_table

Revision ID: 2f69acadecbe
Revises: 176660b8b2c3

"""

# revision identifiers, used by Alembic.
revision = '2f69acadecbe'
down_revision = '176660b8b2c3'

from alembic import op
from sqlalchemy import Column, Boolean, Integer, PrimaryKeyConstraint, String


def upgrade():
    op.create_table(
        'conference',
        Column('id', Integer),
        Column('name', String(128)),
        Column('preprocess_subroutine', String(39)),
        Column('max_users', Integer, nullable=False, server_default='50'),
        Column('record', Boolean, nullable=False, server_default='False'),
        Column('pin', String(80)),
        Column('admin_pin', String(80)),
        Column('quiet_join_leave', Boolean, nullable=False, server_default='False'),
        Column('announce_join_leave', Boolean, nullable=False, server_default='False'),
        Column('announce_user_count', Boolean, nullable=False, server_default='False'),
        Column('announce_only_user', Boolean, nullable=False, server_default='True'),
        Column('music_on_hold', String(128)),
        PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('conference')
