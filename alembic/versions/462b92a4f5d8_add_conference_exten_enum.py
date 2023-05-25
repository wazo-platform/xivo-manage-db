"""add-conference-exten-enum

Revision ID: 462b92a4f5d8
Revises: 2f69acadecbe

"""

# revision identifiers, used by Alembic.
revision = '462b92a4f5d8'
down_revision = '2f69acadecbe'

from alembic import op
from sqlalchemy import Enum


extenumbers_type = Enum(
    'extenfeatures',
    'featuremap',
    'generalfeatures',
    'group',
    'incall',
    'meetme',
    'outcall',
    'queue',
    'user',
    'voicemenu',
    'conference',
    name='extenumbers_type'
)


def upgrade():
    _modify_extenumbers_type()


def _modify_extenumbers_type():
    _modify_type(extenumbers_type,
                 ('extensions', 'type'))


def _modify_type(type_, *table_and_columns):
    op.execute(f'ALTER TYPE {type_.name} RENAME TO tmp_{type_.name}')
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute(f'ALTER TABLE {table} ALTER COLUMN {column} TYPE {type_.name} USING {column}::text::{type_.name}')
    op.execute(f'DROP TYPE tmp_{type_.name}')


def downgrade():
    pass
