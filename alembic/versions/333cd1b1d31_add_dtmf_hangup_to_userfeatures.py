"""add_dtmf_hangup_to_userfeatures

Revision ID: 333cd1b1d31
Revises: 56e683a865e0

"""

# revision identifiers, used by Alembic.
revision = '333cd1b1d31'
down_revision = '56e683a865e0'


from sqlalchemy import Column, sql
from sqlalchemy.types import Integer
from alembic import op

userfeatures = sql.table('userfeatures', sql.column('dtmf_hangup'))


def upgrade():
    op.add_column('userfeatures', Column('dtmf_hangup', Integer, nullable=False, server_default='0'))
    _activate_dtmf_hangup()

    op.alter_column('userfeatures', 'enablexfer', server_default='0')


def _activate_dtmf_hangup():
    op.execute(userfeatures
               .update()
               .values(dtmf_hangup='1'))


def downgrade():
    op.drop_column('userfeatures', 'dtmf_hangup')
    op.alter_column('userfeatures', 'enablexfer', server_default='1')
