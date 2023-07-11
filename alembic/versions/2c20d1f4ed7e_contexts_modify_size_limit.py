"""contexts modify size limit to 79 chars

Revision ID: 2c20d1f4ed7e
Revises: 1ec7cdef9eeb

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c20d1f4ed7e'
down_revision = '1ec7cdef9eeb'

TBL_CONTEXT = 'context'
TBL_CONTEXTINCLUDE = 'contextinclude'

tables = (
    'agent_login_status',
    'agentfeatures',
    'cel',
    'contextinclude',
    'contextmember',
    'contextnumbers',
    'extensions',
    'linefeatures',
    'outcall',
    'queuefeatures',
    'queue',
    'sccpline',
    'trunkfeatures',
    'usercustom',
    'voicemail',
    'usersip',
    'useriax',
)


def upgrade():
    op.alter_column(TBL_CONTEXT, 'name', type_=sa.String(length=79))
    op.alter_column(TBL_CONTEXTINCLUDE, 'include', type_=sa.String(length=79))

    for table in tables:
        op.alter_column(table, 'context', type_=sa.String(length=79))


def downgrade():
    op.alter_column(TBL_CONTEXT, 'name', type_=sa.String(length=39))
    op.alter_column(TBL_CONTEXTINCLUDE, 'include', type_=sa.String(length=39))

    for table in tables:
        op.alter_column(table, 'context', type_=sa.String(length=39))
