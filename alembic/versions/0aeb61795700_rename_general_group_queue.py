"""rename_general_group_queue

Revision ID: 0aeb61795700
Revises: 7d47aaef973a

"""

from alembic import op
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '0aeb61795700'
down_revision = '7d47aaef973a'

groupfeatures_tbl = sql.table(
    'groupfeatures',
    sql.column('name'),
)

queuefeatures_tbl = sql.table(
    'queuefeatures',
    sql.column('name'),
)

queue_tbl = sql.table(
    'queue',
    sql.column('name'),
    sql.column('category'),
)


def find_next_available_name(name):
    query = queue_tbl.select().where(queue_tbl.c.name == name)
    group_exists = op.get_bind().execute(query).scalar()
    if group_exists:
        next_name = '{}_'.format(name)
        return find_next_available_name(next_name)
    return name


def upgrade():
    query = queue_tbl.select().where(queue_tbl.c.name == 'general')
    queue = op.get_bind().execute(query).first()
    if not queue:
        return

    new_name = find_next_available_name('general')
    op.execute(
        queue_tbl
        .update()
        .where(queue_tbl.c.name == queue.name)
        .values(name=new_name)
    )
    if queue.category == 'group':
        op.execute(
            groupfeatures_tbl
            .update()
            .where(groupfeatures_tbl.c.name == queue.name)
            .values(name=new_name)
        )
    elif queue.category == 'queue':
        op.execute(
            queuefeatures_tbl
            .update()
            .where(queuefeatures_tbl.c.name == queue.name)
            .values(name=new_name)
        )


def downgrade():
    pass
