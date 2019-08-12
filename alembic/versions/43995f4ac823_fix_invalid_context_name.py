"""fix-invalid-context-name

Revision ID: 43995f4ac823
Revises: 126c8c1fddb7

"""

import re

from alembic import op
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '43995f4ac823'
down_revision = '126c8c1fddb7'

NOT_CONTEXT_REGEX = r"[^a-zA-Z0-9-_]"
INVALID_NAME = (
    'authentication',
    'general',
    'global',
    'globals',
    'parkedcalls',
    'xivo-features',
    'zonemessages',
)

context_tbl = sql.table(
    'context',
    sql.column('name'),
)

extensions_tbl = sql.table(
    'extensions',
    sql.column('context'),
)


def find_next_available_name(name):
    query = context_tbl.select().where(context_tbl.c.name == name)
    context_exists = op.get_bind().execute(query).scalar()
    if context_exists:
        next_name = '{}_'.format(name)
        return find_next_available_name(next_name)
    return name


def upgrade():
    query = context_tbl.select()
    for context in op.get_bind().execute(query):
        clean_name = re.sub(NOT_CONTEXT_REGEX, '_', context.name)
        if clean_name == context.name and context.name not in INVALID_NAME:
            continue
        old_name = context.name
        new_name = find_next_available_name(clean_name)
        op.execute(
            context_tbl
            .update()
            .where(context_tbl.c.name == old_name)
            .values(name=new_name)
        )

        # Fix associations
        tables_name = [
            'agent_login_status',
            'agentfeatures',
            'contextinclude',
            'contextmember',
            'contextnumbers',
            'extensions',
            'groupfeatures',
            'incall',
            'linefeatures',
            'meetmefeatures',
            'outcall',
            'queue',
            'queuefeatures',
            'sccpline',
            'trunkfeatures',
            'usercustom',
            'useriax',
            'usersip',
            'voicemail',
        ]
        for table_name in tables_name:
            table = sql.table(
                table_name,
                sql.column('context'),
            )
            op.execute(
                table
                .update()
                .where(table.c.context == old_name)
                .values(context=new_name)
            )


def downgrade():
    pass
