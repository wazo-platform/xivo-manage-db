"""add_foreignkey_outcalltrunk

Revision ID: 4fa0a41c0327
Revises: 4fd0315a61fc

"""

# revision identifiers, used by Alembic.
revision = '4fa0a41c0327'
down_revision = '4fd0315a61fc'

from alembic import op
from sqlalchemy import sql

trunk_table = sql.table('trunkfeatures',
                        sql.column('id'))

outcall_table = sql.table('outcall',
                          sql.column('id'))

outcalltrunk_table = sql.table('outcalltrunk',
                               sql.column('trunkfeaturesid'),
                               sql.column('outcallid'))


def upgrade():
    _clean_outcalltrunk_table()
    op.create_foreign_key('outcalltrunk_outcallid_fkey',
                          'outcalltrunk', 'outcall',
                          ['outcallid'], ['id'])
    op.create_foreign_key('outcalltrunk_trunkfeaturesid_fkey',
                          'outcalltrunk', 'trunkfeatures',
                          ['trunkfeaturesid'], ['id'])
    op.alter_column('outcalltrunk', 'outcallid', server_default=None)
    op.alter_column('outcalltrunk', 'trunkfeaturesid', server_default=None)


def _clean_outcalltrunk_table():
    all_trunks = sql.select([trunk_table.c.id]).alias()
    query = (outcalltrunk_table
             .delete()
             .where(outcalltrunk_table.c.trunkfeaturesid.notin_(
                 all_trunks)))

    op.execute(query)

    all_outcalls = sql.select([outcall_table.c.id]).alias()
    query = (outcalltrunk_table
             .delete()
             .where(outcalltrunk_table.c.outcallid.notin_(
                 all_outcalls)))

    op.execute(query)


def downgrade():
    op.drop_constraint('outcalltrunk_outcallid_fkey', 'outcalltrunk')
    op.drop_constraint('outcalltrunk_trunkfeaturesid_fkey', 'outcalltrunk')
    op.alter_column('outcalltrunk', 'outcallid', server_default='0')
    op.alter_column('outcalltrunk', 'trunkfeaturesid', server_default='0')
