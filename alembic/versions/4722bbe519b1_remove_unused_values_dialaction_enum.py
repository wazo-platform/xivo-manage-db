"""remove-unused-values-dialaction-enum

Revision ID: 4722bbe519b1
Revises: b536a68f5505

"""

from alembic import op
from sqlalchemy import sql, Enum

# revision identifiers, used by Alembic.
revision = '4722bbe519b1'
down_revision = 'b536a68f5505'

dialaction_tbl = sql.table(
    'dialaction',
    sql.column('action'),
    sql.column('category'),
)

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
dialaction_category = Enum(
    'callfilter',
    'group',
    'incall',
    'queue',
    'user',
    'ivr',
    'ivr_choice',
    name='dialaction_category',
)
dialaction_action_old = Enum(
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
dialaction_category_old = Enum(
    'callfilter',
    'group',
    'incall',
    'queue',
    'schedule',
    'user',
    'outcall',
    'ivr',
    'ivr_choice',
    name='dialaction_category',
)


def upgrade():
    query = dialaction_tbl.delete().where(dialaction_tbl.c.action == 'schedule')
    op.get_bind().execute(query)
    query = dialaction_tbl.delete().where(dialaction_tbl.c.action == 'trunk')
    op.get_bind().execute(query)
    query = dialaction_tbl.delete().where(dialaction_tbl.c.category == 'schedule')
    op.get_bind().execute(query)
    query = dialaction_tbl.delete().where(dialaction_tbl.c.category == 'outcall')
    op.get_bind().execute(query)

    op.alter_column('schedule', 'fallback_action', server_default=None)
    _modify_type(
        dialaction_action,
        ('dialaction', 'action'),
        ('schedule', 'fallback_action'),
        ('schedule_time', 'action')
    )
    op.alter_column('schedule', 'fallback_action', server_default='none')
    _modify_type(dialaction_category, ('dialaction', 'category'))


def _modify_type(type_, *table_and_columns):
    op.execute(f'ALTER TYPE {type_.name} RENAME TO tmp_{type_.name}')
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute(f'ALTER TABLE {table} ALTER COLUMN {column} TYPE {type_.name} USING {column}::text::{type_.name}')
    op.execute(f'DROP TYPE tmp_{type_.name}')


def downgrade():
    op.alter_column('schedule', 'fallback_action', server_default=None)
    _modify_type(
        dialaction_action_old,
        ('dialaction', 'action'),
        ('schedule', 'fallback_action'),
        ('schedule_time', 'action')
    )
    op.alter_column('schedule', 'fallback_action', server_default='none')
    _modify_type(dialaction_category_old, ('dialaction', 'category'))
