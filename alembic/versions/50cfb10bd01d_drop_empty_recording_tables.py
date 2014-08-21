"""drop empty recording tables

Revision ID: 50cfb10bd01d
Revises: 41d3e47edf4a
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '50cfb10bd01d'
down_revision = '41d3e47edf4a'

from alembic import op
from sqlalchemy import sql
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import INTEGER, VARCHAR, TIMESTAMP, BOOLEAN

recording_table = sql.table('recording',
                            sql.column('cid'),
                            sql.column('start_time'),
                            sql.column('end_time'),
                            sql.column('caller'),
                            sql.column('client_id'),
                            sql.column('callee'),
                            sql.column('filename'),
                            sql.column('campaign_id'),
                            sql.column('agent_id'))

campaign_table = sql.table('record_campaign',
                           sql.column('id'),
                           sql.column('campaign_name'),
                           sql.column('activated'),
                           sql.column('base_filename'),
                           sql.column('queue_id'),
                           sql.column('start_date'),
                           sql.column('end_date'))


def upgrade():
    if _recording_is_empty():
        op.drop_table('recording')
    if _record_campaign_is_empty():
        op.drop_table('record_campaign')


def downgrade():
    _create_campaign_table()
    _create_recording_table()


def _recording_is_empty():
    return 0 == op.get_bind().execute(sql.select([sql.func.count()]).select_from(recording_table)).scalar()


def _record_campaign_is_empty():
    return 0 == op.get_bind().execute(sql.select([sql.func.count()]).select_from(campaign_table)).scalar()


def _create_recording_table():
    op.create_table(
        'recording',
        Column('cid', VARCHAR(32), primary_key=True, nullable=False, autoincrement=False),
        Column('start_time', TIMESTAMP),
        Column('end_time', TIMESTAMP),
        Column('caller', VARCHAR(32)),
        Column('client_id', VARCHAR(1024)),
        Column('callee', VARCHAR(32)),
        Column('filename', VARCHAR(1024)),
        Column('campaign_id', INTEGER, nullable=False),
        Column('agent_id', INTEGER, nullable=False)
    )

    op.create_foreign_key('recording_agent_id_fkey', 'recording',
                          'agentfeatures', ['agent_id'], ['id'],
                          onupdate='CASCADE',
                          ondelete='SET NULL')

    op.create_foreign_key('recording_campaign_id_fkey', 'recording',
                          'record_campaign', ['campaign_id'], ['id'])


def _create_campaign_table():
    op.create_table(
        'record_campaign',
        Column('id', INTEGER, primary_key=True, nullable=False, autoincrement=True),
        Column('campaign_name', VARCHAR(128), nullable=False),
        Column('activated', BOOLEAN, nullable=False),
        Column('base_filename', VARCHAR(64), nullable=False),
        Column('queue_id', INTEGER),
        Column('start_date', TIMESTAMP),
        Column('end_date', TIMESTAMP)
    )

    op.create_foreign_key('record_campaign_queue_id_fkey', 'record_campaign',
                          'queuefeatures', ['queue_id'], ['id'],
                          onupdate='CASCADE',
                          ondelete='SET NULL')

    op.create_unique_constraint('record_campaign_campaign_name_key', 'record_campaign', ['campaign_name'])
