"""add_conference_dialaction

Revision ID: 1f533d5f5f51
Revises: 462b92a4f5d8

"""

# revision identifiers, used by Alembic.
revision = '1f533d5f5f51'
down_revision = '462b92a4f5d8'

from alembic import op
from sqlalchemy import Enum


dialaction_action = Enum(
    'none',
    'endcall:busy',
    'endcall:congestion',
    'endcall:hangup',
    'user',
    'group',
    'queue',
    'meetme',
    'voicemail',
    'trunk',
    'schedule',
    'extension',
    'outcall',
    'application:callbackdisa',
    'application:disa',
    'application:directory',
    'application:faxtomail',
    'application:voicemailmain',
    'application:password',
    'sound',
    'custom',
    'ivr',
    'conference',
    name='dialaction_action',
)


def upgrade():
    _modify_dialaction_action_type()


def _modify_dialaction_action_type():
    op.alter_column('schedule', 'fallback_action', server_default=None)
    _modify_type(dialaction_action,
                 ('dialaction', 'action'),
                 ('schedule', 'fallback_action'),
                 ('schedule_time', 'action'))
    op.alter_column('schedule', 'fallback_action', server_default='none')


def _modify_type(type_, *table_and_columns):
    op.execute('ALTER TYPE {type_name} RENAME TO tmp_{type_name}'.format(type_name=type_.name))
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute('ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {type_name} USING {column_name}::text::{type_name}'.format(
            type_name=type_.name, table_name=table, column_name=column))
    op.execute('DROP TYPE tmp_{type_name}'.format(type_name=type_.name))


def downgrade():
    pass
