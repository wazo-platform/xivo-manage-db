"""add switchboard table

Revision ID: 1cc52186eb47
Revises: 8c21acf4e9e

"""

# revision identifiers, used by Alembic.
revision = '1cc52186eb47'
down_revision = '8c21acf4e9e'

from alembic import op
import sqlalchemy as sa


old_options = ('none',
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
               'conference')
new_options = sorted(old_options + ('switchboard',))

new_type = sa.Enum(*new_options, name='dialaction_action')
old_type = sa.Enum(*old_options, name='dialaction_action')
tmp_type = sa.Enum(*new_options, name='dialaction_action_being_replaced')

dialaction = sa.sql.table('dialaction',
                          sa.Column('action', new_type, nullable=False),
                          sa.Column('actionarg1', sa.String(255), nullable=False, server_default=''))


def upgrade():
    op.create_table(
        'switchboard',
        sa.Column('id', sa.String(38), nullable=False),
        sa.Column('name', sa.String(128), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'switchboard_member_user',
        sa.Column('switchboard_id', sa.String(38), nullable=False),
        sa.Column('user_uuid', sa.String(38), nullable=False),
        sa.PrimaryKeyConstraint('switchboard_id', 'user_uuid'),
    )
    _add_dialaction()


def downgrade():
    _remove_dialaction()
    op.drop_table('switchboard')


def _add_dialaction():
    op.execute('ALTER TYPE dialaction_action RENAME TO dialaction_action_being_replaced')

    new_type.create(op.get_bind())
    op.execute('ALTER TABLE dialaction ALTER COLUMN action TYPE dialaction_action USING action::text::dialaction_action')
    op.alter_column('schedule', 'fallback_action', server_default=None)
    op.execute('ALTER TABLE schedule ALTER COLUMN fallback_action TYPE dialaction_action USING fallback_action::text::dialaction_action')
    op.alter_column('schedule', 'fallback_action', server_default='none')
    op.execute('ALTER TABLE schedule_time ALTER COLUMN action TYPE dialaction_action USING action::text::dialaction_action')

    tmp_type.drop(op.get_bind(), checkfirst=False)


def _remove_dialaction():
    # Convert dialaction switchboard into dialaction none
    op.execute(dialaction
               .update()
               .where(dialaction.c.action == 'switchboard')
               .values(action='none', actionarg1='', actionarg2=''))

    op.execute('ALTER TYPE dialaction_action RENAME TO dialaction_action_being_replaced')

    old_type.create(op.get_bind())
    op.execute('ALTER TABLE dialaction ALTER COLUMN action TYPE dialaction_action USING action::text::dialaction_action')
    op.alter_column('schedule', 'fallback_action', server_default=None)
    op.execute('ALTER TABLE schedule ALTER COLUMN fallback_action TYPE dialaction_action USING fallback_action::text::dialaction_action')
    op.alter_column('schedule', 'fallback_action', server_default='none')
    op.execute('ALTER TABLE schedule_time ALTER COLUMN action TYPE dialaction_action USING action::text::dialaction_action')

    tmp_type.drop(op.get_bind(), checkfirst=False)
