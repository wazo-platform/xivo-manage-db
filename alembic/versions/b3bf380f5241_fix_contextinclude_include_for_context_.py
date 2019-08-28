"""fix contextinclude include for context renames

Revision ID: b3bf380f5241
Revises: 34b2b6ca345e

"""

import re

from alembic import op
from sqlalchemy import (
    and_,
    sql,
)


# revision identifiers, used by Alembic.
revision = 'b3bf380f5241'
down_revision = '34b2b6ca345e'

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

context_include_tbl = sql.table(
    'contextinclude',
    sql.column('context'),
    sql.column('include'),
    sql.column('priority'),
)


def upgrade():
    available_context_query = context_tbl.select()
    contexts = op.get_bind().execute(available_context_query)
    existing_names = [context.name for context in contexts]

    query = context_include_tbl.select()
    for include in op.get_bind().execute(query):
        new_name = re.sub(NOT_CONTEXT_REGEX, '_', include.include)
        if new_name == include.include and include.include not in INVALID_NAME:
            continue

        if new_name not in existing_names:
            continue

        old_name = include.include
        op.execute(
            context_include_tbl
            .update()
            .where(and_(
                context_include_tbl.c.context == include.context,
                context_include_tbl.c.priority == include.priority,
            ))
            .values(include=new_name)
        )


def downgrade():
    pass
