"""drop_order_column_in_schedule_path

Revision ID: 1a72b3da2baf
Revises: c18e988da503

"""

# revision identifiers, used by Alembic.
revision = '1a72b3da2baf'
down_revision = 'c18e988da503'

from alembic import op
from sqlalchemy import sql, Column, Integer


schedule = sql.table(
    'schedule',
    sql.column('id'),
)

schedule_path = sql.table(
    'schedule_path',
    sql.column('schedule_id'),
)


def upgrade():
    _sanitize_schedule_path()
    op.drop_column('schedule_path', 'order')
    op.create_foreign_key('schedule_path_schedule_id_fkey',
                          'schedule_path', 'schedule',
                          ['schedule_id'], ['id'])


def _sanitize_schedule_path():
    valid_schedules = sql.select([schedule.c.id])
    query = (schedule_path
             .delete()
             .where(sql.not_(
                 schedule_path.c.schedule_id.in_(valid_schedules)
             )))
    op.get_bind().execute(query)


def downgrade():
    op.drop_constraint('schedule_path_schedule_id_fkey', 'schedule_path')
    op.add_column('schedule_path', Column('order', Integer(), nullable=False))
