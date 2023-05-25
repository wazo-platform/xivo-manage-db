"""add group member extensions

Revision ID: 28721fe085d3
Revises: 872b869e9675

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql


# revision identifiers, used by Alembic.
revision = '28721fe085d3'
down_revision = '872b869e9675'

func_key_destination_type_table = sql.table('func_key_destination_type',
                                            sql.column('id'),
                                            sql.column('name'))
extensions_table = sql.table('extensions',
                             sql.column('context'),
                             sql.column('exten'),
                             sql.column('type'),
                             sql.column('typeval'))

DESTINATION_ID = 13
DESTINATION_NAME = 'groupmember'


def upgrade():
    insert_query = extensions_table.insert().values(
        context='xivo-features',
        exten='_*50.',
        type='extenfeatures',
        typeval='groupmembertoggle',
    )
    op.get_bind().execute(insert_query)
    insert_query = extensions_table.insert().values(
        context='xivo-features',
        exten='_*51.',
        type='extenfeatures',
        typeval='groupmemberjoin',
    )
    op.get_bind().execute(insert_query)
    insert_query = extensions_table.insert().values(
        context='xivo-features',
        exten='_*52.',
        type='extenfeatures',
        typeval='groupmemberleave',
    )
    op.get_bind().execute(insert_query)

    insert_query = func_key_destination_type_table.insert().values(
        id=DESTINATION_ID,
        name=DESTINATION_NAME,
    )
    op.get_bind().execute(insert_query)

    op.create_table(
        'func_key_dest_groupmember',
        sa.Column('func_key_id', sa.Integer),
        sa.Column('destination_type_id',
                  sa.Integer,
                  sa.CheckConstraint(f'destination_type_id = {DESTINATION_ID}'),
                  server_default=str(DESTINATION_ID)),
        sa.Column('group_id',
                  sa.Integer,
                  nullable=False),
        sa.Column('extension_id',
                  sa.Integer,
                  sa.ForeignKey('extensions.id'),
                  nullable=False),
        sa.PrimaryKeyConstraint('func_key_id', 'destination_type_id'),
        sa.ForeignKeyConstraint(['func_key_id', 'destination_type_id'],
                                ['func_key.id', 'func_key.destination_type_id']),
        sa.ForeignKeyConstraint(['group_id'], ['groupfeatures.id']),
        sa.UniqueConstraint('group_id', 'extension_id'),
    )


def downgrade():
    query = (extensions_table
             .delete()
             .where(
                 sql.and_(
                     extensions_table.c.type == 'extenfeatures',
                     extensions_table.c.typeval == 'groupmembertoggle'
                 )
             ))
    op.get_bind().execute(query)
    query = (extensions_table
             .delete()
             .where(
                 sql.and_(
                     extensions_table.c.type == 'extenfeatures',
                     extensions_table.c.typeval == 'groupmemberjoin'
                 )
             ))
    op.get_bind().execute(query)
    query = (extensions_table
             .delete()
             .where(
                 sql.and_(
                     extensions_table.c.type == 'extenfeatures',
                     extensions_table.c.typeval == 'groupmemberleave'
                 )
             ))
    op.get_bind().execute(query)

    query = (func_key_destination_type_table
             .delete()
             .where(
                 func_key_destination_type_table.c.id == DESTINATION_ID,
             ))
    op.get_bind().execute(query)

    op.drop_table('func_key_dest_groupmember')
