"""add_parking_lot

Revision ID: 198c5bc02abf
Revises: 1f533d5f5f51

"""

# revision identifiers, used by Alembic.
revision = '198c5bc02abf'
down_revision = '1f533d5f5f51'

from alembic import op
from sqlalchemy import Column, Integer, Enum, PrimaryKeyConstraint, String

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
    'parking',
    name='extenumbers_type'
)


def upgrade():
    _create_parking_lot_table()
    _modify_extenumbers_type()


def _create_parking_lot_table():
    op.create_table(
        'parking_lot',
        Column('id', Integer),
        Column('name', String(128)),
        Column('slots_start', String(40), nullable=False),
        Column('slots_end', String(40), nullable=False),
        Column('timeout', Integer),
        Column('music_on_hold', String(128)),
        PrimaryKeyConstraint('id'),
    )


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
    op.drop_table('parking_lot')
