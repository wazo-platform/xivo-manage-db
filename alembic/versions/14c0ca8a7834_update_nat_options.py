"""update_nat_options

Revision ID: 14c0ca8a7834
Revises: 57461905b7e6

"""

# revision identifiers, used by Alembic.
revision = '14c0ca8a7834'
down_revision = '57461905b7e6'

import sqlalchemy as sa
from alembic import op
from sqlalchemy import sql

old_options = (
    'no',
    'force_rport',
    'comedia',
    'force_rport,comedia'
)
new_options = sorted(old_options + ('auto_force_rport', 'auto_comedia',))

new_type = sa.Enum(*new_options, name='usersip_nat')
old_type = sa.Enum(*old_options, name='usersip_nat')

staticsip_table = sql.table('staticsip',
                            sql.column('var_name'),
                            sql.column('var_val'))

usersip_table = sa.sql.table('usersip',
                             sa.sql.column('id'),
                             sa.sql.column('nat'))


def upgrade():
    _update_staticsip_nat('no', 'auto_force_rport')
    _modify_type(new_type, ('usersip', 'nat'))
    _update_usersip_nat('no', 'auto_force_rport')


def downgrade():
    _update_staticsip_nat('auto_force_rport', 'no')
    _update_usersip_nat('auto_force_rport', 'no')
    _modify_type(old_type, ('usersip', 'nat'))


def _update_staticsip_nat(val_from, val_to):
    op.execute(staticsip_table.update().
               where(sql.and_(
                    staticsip_table.c.var_name == 'nat',
                    staticsip_table.c.var_val == val_from)).
               values(var_val=val_to))


def _update_usersip_nat(val_from, val_to):
    op.execute(usersip_table.update().
               where(sql.and_(
                    usersip_table.c.nat == val_from)).
               values(nat=val_to))


def _modify_type(type_, *table_and_columns):
    op.execute('ALTER TYPE {type_name} RENAME TO tmp_{type_name}'.format(type_name=type_.name))
    type_.create(op.get_bind())
    for table, column in table_and_columns:
        op.execute(
            'ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {type_name} USING {column_name}::text::{type_name}'.format(
                type_name=type_.name, table_name=table, column_name=column))
    op.execute('DROP TYPE tmp_{type_name}'.format(type_name=type_.name))
