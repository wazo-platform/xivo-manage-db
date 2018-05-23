"""remove_pickupmember_invalid

Revision ID: 378c46e8c6fe
Revises: 58fc78d9f67f

"""

from alembic import op
from sqlalchemy import sql

# revision identifiers, used by Alembic.
revision = '378c46e8c6fe'
down_revision = '58fc78d9f67f'

userfeatures = sql.table(
    'userfeatures',
    sql.column('id'),
)

groupfeatures = sql.table(
    'groupfeatures',
    sql.column('id'),
)

queuefeatures = sql.table(
    'queuefeatures',
    sql.column('id'),
)

pickupmember = sql.table(
    'pickupmember',
    sql.column('membertype'),
    sql.column('memberid'),
)


def upgrade():
    conn = op.get_bind()
    group_ids = [r.id for r in conn.execute(sql.select([groupfeatures.c.id])).fetchall()]
    queue_ids = [r.id for r in conn.execute(sql.select([queuefeatures.c.id])).fetchall()]
    user_ids = [r.id for r in conn.execute(sql.select([userfeatures.c.id])).fetchall()]

    op.execute(
        pickupmember
        .delete()
        .where(sql.or_(
            sql.and_(
                pickupmember.c.membertype == 'group',
                sql.not_(pickupmember.c.memberid.in_(group_ids)),
            ),
            sql.and_(
                pickupmember.c.membertype == 'queue',
                sql.not_(pickupmember.c.memberid.in_(queue_ids)),
            ),
            sql.and_(
                pickupmember.c.membertype == 'user',
                sql.not_(pickupmember.c.memberid.in_(user_ids)),
            ),
        ))
    )


def downgrade():
    pass
