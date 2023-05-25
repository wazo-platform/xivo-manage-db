"""add ivr support

Revision ID: 9142f0403c8
Revises: 2072c1e66aa9

"""

# revision identifiers, used by Alembic.
revision = '9142f0403c8'
down_revision = '2072c1e66aa9'

from alembic import op
from sqlalchemy import sql, Column, Enum, ForeignKey, Integer, PrimaryKeyConstraint, String, Text

dialaction = sql.table('dialaction',
                       sql.column('action'))

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
    name='dialaction_action',
)

dialaction_category = Enum(
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
    _add_ivr_table()
    _add_ivr_choice_table()
    _modify_dialaction_action_type()
    _modify_dialaction_category_type()


def _add_ivr_table():
    op.create_table(
        'ivr',
        Column('id', Integer),
        Column('name', String(128), nullable=False),
        Column('greeting_sound', Text),
        Column('menu_sound', Text, nullable=False),
        Column('invalid_sound', Text),
        Column('abort_sound', Text),
        Column('timeout', Integer, nullable=False, server_default='5'),
        Column('max_tries', Integer, nullable=False, server_default='3'),
        Column('description', Text),
        PrimaryKeyConstraint('id'),
    )


def _add_ivr_choice_table():
    op.create_table(
        'ivr_choice',
        Column('id', Integer),
        Column('ivr_id', Integer, ForeignKey('ivr.id'), nullable=False),
        Column('exten', String(40), nullable=False),
        PrimaryKeyConstraint('id'),
    )

def _modify_dialaction_action_type():
    op.execute(dialaction.delete().where(dialaction.c.action == 'voicemenu'))
    op.alter_column('schedule', 'fallback_action', server_default=None)
    _modify_type(dialaction_action,
                 ('dialaction', 'action'),
                 ('schedule', 'fallback_action'),
                 ('schedule_time', 'action'))
    op.alter_column('schedule', 'fallback_action', server_default='none')


def _modify_dialaction_category_type():
    _modify_type(dialaction_category,
                 ('dialaction', 'category'))


def _modify_type(type_, *table_and_columns):
    op.execute(f'ALTER TYPE {type_.name} RENAME TO tmp_{type_.name}')
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute(f'ALTER TABLE {table} ALTER COLUMN {column} TYPE {type_.name} USING {column}::text::{type_.name}')
    op.execute(f'DROP TYPE tmp_{type_.name}')


def downgrade():
    pass
