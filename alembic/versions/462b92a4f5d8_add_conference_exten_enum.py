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
    op.execute('ALTER TYPE {type_name} RENAME TO tmp_{type_name}'.format(type_name=type_.name))
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute('ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {type_name} USING {column_name}::text::{type_name}'.format(
            type_name=type_.name, table_name=table, column_name=column))
    op.execute('DROP TYPE tmp_{type_name}'.format(type_name=type_.name))


def downgrade():
    pass
