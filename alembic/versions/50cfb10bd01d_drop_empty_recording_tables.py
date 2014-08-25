"""drop empty recording tables

Revision ID: 50cfb10bd01d
Revises: 41d3e47edf4a
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '50cfb10bd01d'
down_revision = '41d3e47edf4a'

from alembic import op
from sqlalchemy import sql, text
from sqlalchemy.types import Integer

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

tables = {'recording': recording_table, 'record_campaign': campaign_table}


def upgrade():
    _conditionnal_drop_table('recording')
    _conditionnal_drop_table('record_campaign')


def downgrade():
    pass


def _conditionnal_drop_table(table_name):
    if _table_exists_empty(table_name):
        op.drop_table(table_name)


def _table_exists_empty(table_name):
    if _table_does_not_exist(table_name):
        return False
    return 0 == op.get_bind().execute(sql.select([sql.func.count()]).select_from(tables[table_name])).scalar()


def _table_does_not_exist(table_name):
    t = text("select count(*) from pg_class where relname=:table and relkind='r';").\
        bindparams(table=table_name).\
        columns(count=Integer)

    for record in op.get_bind().execute(t):
        count = record[0]
        return (count == 0)
