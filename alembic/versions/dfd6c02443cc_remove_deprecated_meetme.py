"""remove-deprecated-meetme

Revision ID: dfd6c02443cc
Revises: 2fe87e2b9580

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfd6c02443cc'
down_revision = '2fe87e2b9580'

func_key_tbl = sa.sql.table(
    'func_key',
    sa.sql.column('destination_type_id'),
)

func_key_mapping_tbl = sa.sql.table(
    'func_key_mapping',
    sa.sql.column('destination_type_id'),
)

func_key_dest_conference_tbl = sa.sql.table(
    'func_key_dest_conference',
)

dialaction_tbl = sa.sql.table(
    'dialaction',
    sa.sql.column('action'),
)
schedule_tbl = sa.sql.table(
    'schedule',
    sa.sql.column('fallback_action'),
)
schedule_time_tbl = sa.sql.table(
    'schedule_time',
    sa.sql.column('action'),
)
extensions_tbl = sa.sql.table(
    'extensions',
    sa.sql.column('type'),
    sa.sql.column('typeval'),
)

dialaction_action = sa.Enum(
    'none',
    'endcall:busy',
    'endcall:congestion',
    'endcall:hangup',
    'user',
    'group',
    'queue',
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

extenumbers_type = sa.Enum(
    'extenfeatures',
    'featuremap',
    'generalfeatures',
    'group',
    'incall',
    'outcall',
    'queue',
    'user',
    'voicemenu',
    'conference',
    'parking',
    name='extenumbers_type',
)

contextnumbers_type = sa.Enum(
    'user',
    'group',
    'queue',
    'conference',
    'incall',
    name='contextnumbers_type',
)


def upgrade():
    # Remove funckeys and use table to map to confbridge object
    query = func_key_dest_conference_tbl.delete()
    op.execute(query)
    query = func_key_mapping_tbl.delete().where(func_key_mapping_tbl.c.destination_type_id == '4')
    op.execute(query)
    query = func_key_tbl.delete().where(func_key_tbl.c.destination_type_id == '4')
    op.execute(query)

    constraint_name = 'func_key_dest_conference_conference_id_fkey'
    op.drop_constraint(constraint_name, 'func_key_dest_conference')
    op.create_foreign_key(
        constraint_name,
        'func_key_dest_conference',
        'conference',
        ['conference_id'],
        ['id'],
    )

    # Rename callmeetme to callconference
    query = (
        extensions_tbl.update()
        .where(
            sa.sql.and_(
                extensions_tbl.c.type == 'extenfeatures',
                extensions_tbl.c.typeval == 'callmeetme',
            )
        )
        .values(typeval='callconference')
    )
    op.execute(query)

    # Remove meetmetables
    op.drop_table('staticmeetme')
    op.drop_table('meetmeguest')
    op.drop_table('meetmefeatures')
    op.execute('DROP TYPE meetmefeatures_admin_typefrom;')
    op.execute('DROP TYPE meetmefeatures_admin_identification;')
    op.execute('DROP TYPE meetmefeatures_mode;')
    op.execute('DROP TYPE meetmefeatures_announcejoinleave;')
    op.drop_table('phonefunckey')

    # Remove meetme from enums
    query = dialaction_tbl.delete().where(dialaction_tbl.c.action == 'meetme')
    op.get_bind().execute(query)
    query = schedule_tbl.delete().where(schedule_tbl.c.fallback_action == 'meetme')
    op.get_bind().execute(query)
    query = schedule_time_tbl.delete().where(schedule_time_tbl.c.action == 'meetme')
    op.get_bind().execute(query)
    query = extensions_tbl.delete().where(extensions_tbl.c.type == 'meetme')
    op.get_bind().execute(query)

    op.alter_column('schedule', 'fallback_action', server_default=None)
    _modify_type(
        dialaction_action,
        ('dialaction', 'action'),
        ('schedule', 'fallback_action'),
        ('schedule_time', 'action')
    )
    op.alter_column('schedule', 'fallback_action', server_default='none')
    _modify_type(extenumbers_type, ('extensions', 'type'))


def _modify_type(type_, *table_and_columns):
    op.execute('ALTER TYPE {type_name} RENAME TO tmp_{type_name}'.format(type_name=type_.name))
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute(
            'ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {type_name} USING {column_name}::text::{type_name}'.format(
                type_name=type_.name, table_name=table, column_name=column
            )
        )
    op.execute('DROP TYPE tmp_{type_name}'.format(type_name=type_.name))


def downgrade():
    pass
