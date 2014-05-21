"""remove unused tables

Revision ID: 1d05ffb14525
Revises: 447e4ab61975
Create Date: 2014-05-21 08:43:19.169757
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '1d05ffb14525'
down_revision = '447e4ab61975'

from alembic import op
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import INTEGER, VARCHAR, TIMESTAMP


def upgrade():
    op.drop_table('ctilog')
    op.drop_table('stats_conf_user')
    op.drop_table('stats_conf_group')
    op.drop_table('stats_conf_incall')


def downgrade():
    op.create_table(
        'ctilog',
        Column('id', INTEGER, primary_key=True),
        Column('eventdate', TIMESTAMP),
        Column('loginclient', VARCHAR(64)),
        Column('company', VARCHAR(64)),
        Column('status', VARCHAR(64)),
        Column('action', VARCHAR(64)),
        Column('arguments', VARCHAR(255)),
        Column('callduration', INTEGER)
    )

    op.create_table(
        'stats_conf_group',
        Column('stats_conf_id', INTEGER, primary_key=True, autoincrement=False),
        Column('groupfeatures_id', INTEGER, primary_key=True, autoincrement=False)
    )

    op.create_table(
        'stats_conf_incall',
        Column('stats_conf_id', INTEGER, primary_key=True, autoincrement=False),
        Column('incall_id', INTEGER, primary_key=True, autoincrement=False)
    )

    op.create_table(
        'stats_conf_user',
        Column('stats_conf_id', INTEGER, primary_key=True, autoincrement=False),
        Column('userfeatures_id', INTEGER, primary_key=True, autoincrement=False)
    )
