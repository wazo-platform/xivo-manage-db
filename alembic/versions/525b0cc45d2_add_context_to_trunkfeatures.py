"""add_context_to_trunkfeatures

Revision ID: 525b0cc45d2
Revises: 2989b8b30fe7

"""

# revision identifiers, used by Alembic.
revision = '525b0cc45d2'
down_revision = '2989b8b30fe7'

from alembic import op
import sqlalchemy as sa


trunk_table = sa.sql.table('trunkfeatures',
                           sa.sql.column('protocol'),
                           sa.sql.column('protocolid'),
                           sa.sql.column('context'))

usersip_table = sa.sql.table('usersip',
                             sa.sql.column('id'),
                             sa.sql.column('context'))

useriax_table = sa.sql.table('useriax',
                             sa.sql.column('id'),
                             sa.sql.column('context'))

usercustom_table = sa.sql.table('usercustom',
                                sa.sql.column('id'),
                                sa.sql.column('context'))


def upgrade():
    op.alter_column('trunkfeatures', 'protocol', nullable=True)
    op.alter_column('trunkfeatures', 'protocolid', nullable=True)
    op.add_column('trunkfeatures', sa.Column('context', sa.String))
    _populate_context_from_usersip()
    _populate_context_from_useriax()
    _populate_context_from_usercustom()


def _populate_context_from_usersip():
    query = (trunk_table
             .update()
             .values(context=usersip_table.c.context)
             .where(trunk_table.c.protocol == 'sip')
             .where(trunk_table.c.protocolid == usersip_table.c.id))
    op.get_bind().execute(query)


def _populate_context_from_useriax():
    query = (trunk_table
             .update()
             .values(context=useriax_table.c.context)
             .where(trunk_table.c.protocol == 'iax')
             .where(trunk_table.c.protocolid == useriax_table.c.id))
    op.get_bind().execute(query)


def _populate_context_from_usercustom():
    query = (trunk_table
             .update()
             .values(context=usercustom_table.c.context)
             .where(trunk_table.c.protocol == 'custom')
             .where(trunk_table.c.protocolid == usercustom_table.c.id))
    op.get_bind().execute(query)


def downgrade():
    op.drop_column('trunkfeatures', 'context')
    op.alter_column('trunkfeatures', 'protocolid', nullable=False)
    op.alter_column('trunkfeatures', 'protocol', nullable=False)
