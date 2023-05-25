"""add_application_dialaction

Revision ID: 47920341f392
Revises: 5013b66e26d2

"""

from alembic import op
from sqlalchemy import sql, Enum

# revision identifiers, used by Alembic.
revision = '47920341f392'
down_revision = '5013b66e26d2'

dialaction = sql.table('dialaction', sql.column('action'))

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
    'switchboard',
    'application:custom',
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
    op.execute(f'ALTER TYPE {type_.name} RENAME TO tmp_{type_.name}')
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute(f'ALTER TABLE {table} ALTER COLUMN {column} TYPE {type_.name} USING {column}::text::{type_.name}')
    op.execute(f'DROP TYPE tmp_{type_.name}')


def downgrade():
    pass
