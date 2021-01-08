"""add-user-specific-recording-options

Revision ID: 2fe87e2b9580
Revises: 203f6f2cf0a0

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fe87e2b9580'
down_revision = '203f6f2cf0a0'

user_tbl = sa.sql.table(
    'userfeatures',
    sa.sql.column('callrecord'),
    sa.sql.column('call_record_outgoing_external_enabled'),
    sa.sql.column('call_record_outgoing_internal_enabled'),
    sa.sql.column('call_record_incoming_external_enabled'),
    sa.sql.column('call_record_incoming_internal_enabled'),
)


def upgrade():
    _add_user_bool_column('call_record_outgoing_external_enabled')
    _add_user_bool_column('call_record_outgoing_internal_enabled')
    _add_user_bool_column('call_record_incoming_external_enabled')
    _add_user_bool_column('call_record_incoming_internal_enabled')
    call_record = sa.sql.cast(user_tbl.c.callrecord, sa.Boolean)
    query = (
        user_tbl.update()
        .values(
            call_record_outgoing_external_enabled=call_record,
            call_record_outgoing_internal_enabled=call_record,
            call_record_incoming_external_enabled=call_record,
            call_record_incoming_internal_enabled=call_record,
        )
    )
    op.execute(query)
    op.drop_column('userfeatures', 'callrecord')


def _add_user_bool_column(name):
    op.add_column(
        'userfeatures',
        sa.Column(name, sa.Boolean, nullable=False, server_default='false')
    )


def downgrade():
    op.add_column(
        'userfeatures',
        sa.Column('callrecord', sa.Integer, nullable=False, server_default='0')
    )
    op.drop_column('userfeatures', 'call_record_outgoing_external_enabled')
    op.drop_column('userfeatures', 'call_record_outgoing_internal_enabled')
    op.drop_column('userfeatures', 'call_record_incoming_external_enabled')
    op.drop_column('userfeatures', 'call_record_incoming_internal_enabled')
