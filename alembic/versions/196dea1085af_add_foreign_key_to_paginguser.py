"""add_foreign_key_to_paginguser

Revision ID: 196dea1085af
Revises: 7b3b0ff90f0c

"""

# revision identifiers, used by Alembic.
revision = '196dea1085af'
down_revision = '7b3b0ff90f0c'

from alembic import op
from sqlalchemy import sql

user = sql.table(
    'userfeatures',
    sql.column('id'),
)

paging = sql.table(
    'paging',
    sql.column('id'),
)

paging_user = sql.table(
    'paginguser',
    sql.column('userfeaturesid'),
    sql.column('pagingid'),
)


def upgrade():
    _sanitize_paging_user()
    op.create_foreign_key('paginguser_userfeaturesid_fkey',
                          'paginguser', 'userfeatures',
                          ['userfeaturesid'], ['id'])
    op.create_foreign_key('paginguser_pagingid_fkey',
                          'paginguser', 'paging',
                          ['pagingid'], ['id'])


def _sanitize_paging_user():
    valid_users = sql.select([user.c.id])
    valid_pagings = sql.select([paging.c.id])
    query = (
        paging_user.delete()
        .where(
            sql.or_(
                sql.not_(paging_user.c.pagingid.in_(valid_pagings)),
                sql.not_(paging_user.c.userfeaturesid.in_(valid_users))
            )
        )
    )
    op.get_bind().execute(query)


def downgrade():
    op.drop_constraint('paginguser_pagingid_fkey', 'paginguser')
    op.drop_constraint('paginguser_userfeaturesid_fkey', 'paginguser')
