"""remove-dangling-user-function-keys

Revision ID: 45ec6bd040ac
Revises: bba3a031fd01

"""

from alembic import op
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '45ec6bd040ac'
down_revision = 'bba3a031fd01'

func_key = sql.table(
    'func_key',
    sql.column('id'),
    sql.column('destination_type_id'),
)

func_key_mapping = sql.table(
    'func_key_mapping',
    sql.column('func_key_id'),
)

func_key_dest_user = sql.table(
    'func_key_dest_user',
    sql.column('func_key_id'),
)


def upgrade():
    sub_query = sql.select([func_key_mapping.c.func_key_id])
    func_keys = op.get_bind().execute(
        sql.select([func_key.c.id])
        .select_from(
            func_key.join(
                func_key_dest_user, func_key_dest_user.c.func_key_id == func_key.c.id
            )
        )
        .where(func_key.c.id.notin_(sub_query))
    )
    func_key_ids = [func_key.id for func_key in func_keys]

    if not func_key_ids:
        return

    op.execute(
        func_key_dest_user
        .delete()
        .where(func_key_dest_user.c.func_key_id.in_(func_key_ids))
    )
    op.execute(
        func_key
        .delete()
        .where(func_key.c.id.in_(func_key_ids))
    )


def downgrade():
    pass
