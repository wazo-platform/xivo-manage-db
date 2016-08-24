"""create_line_extension_table

Revision ID: 2989b8b30fe7
Revises: 4bb90c6c47bb

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2989b8b30fe7'
down_revision = '4bb90c6c47bb'


line_extension_table = sa.sql.table('line_extension',
                                    sa.sql.column('line_id'),
                                    sa.sql.column('extension_id'),
                                    sa.sql.column('main_extension'))

user_line_table = sa.sql.table('user_line',
                               sa.sql.column('line_id'),
                               sa.sql.column('extension_id'),
                               sa.sql.column('main_line'),
                               sa.sql.column('main_user'),
                               sa.sql.column('user_id'))


def upgrade():
    _create_line_extension_table()
    _populate_line_extension_from_user_line()
    _remove_unused_user_line_entries()
    op.drop_column('user_line', 'extension_id')
    op.drop_constraint('user_line_pkey', 'user_line')
    op.drop_column('user_line', 'id')
    op.execute("DROP SEQUENCE IF EXISTS user_line_id_seq")  # downgrade create a persistent sequence
    op.drop_constraint('user_line_user_id_line_id_key', 'user_line')
    op.create_primary_key('user_line_pkey', 'user_line', ['user_id', 'line_id'])
    op.alter_column('user_line', 'user_id', nullable=False)


def _create_line_extension_table():
    op.create_table(
        'line_extension',
        sa.Column('line_id',
                  sa.Integer,
                  sa.ForeignKey('linefeatures.id'),
                  nullable=False),
        sa.Column('extension_id',
                  sa.Integer,
                  sa.ForeignKey('extensions.id'),
                  nullable=False),
        sa.Column('main_extension',
                  sa.Boolean,
                  nullable=False),
        sa.PrimaryKeyConstraint('line_id', 'extension_id'),
    )


def _get_all_line_extension_from_user_line():
    query = (
        sa.sql.select(
            [user_line_table.c.line_id, user_line_table.c.extension_id])
        .where(
            user_line_table.c.extension_id != None)  # noqa
        .distinct())
    return op.get_bind().execute(query).fetchall()


def _populate_line_extension_from_user_line():
    for line_extension in _get_all_line_extension_from_user_line():
        query = (line_extension_table
                 .insert()
                 .values(line_id=line_extension.line_id,
                         extension_id=line_extension.extension_id,
                         main_extension=True))
        op.get_bind().execute(query)


def _remove_unused_user_line_entries():
    query = (user_line_table
             .delete()
             .where(user_line_table.c.user_id == None))  # noqa
    op.get_bind().execute(query)


def downgrade():
    op.drop_constraint('user_line_pkey', 'user_line')
    op.alter_column('user_line', 'user_id', nullable=True)
    op.create_unique_constraint('user_line_user_id_line_id_key', 'user_line', ['user_id', 'line_id'])
    op.execute(sa.schema.CreateSequence(sa.schema.Sequence('user_line_id_seq')))
    op.add_column('user_line', sa.Column('id',
                                         sa.Integer,
                                         nullable=False,
                                         server_default=sa.text("nextval('user_line_id_seq'::regclass)")))
    op.create_primary_key('user_line_pkey', 'user_line', ['id', 'line_id'])
    op.add_column('user_line', sa.Column('extension_id', sa.Integer, sa.ForeignKey('extensions.id')))
    _populate_user_line_from_line_extension()
    op.drop_table('line_extension')


def _get_all_line_extension_from_line_extension():
    query = (
        sa.sql.select(
            [line_extension_table.c.line_id, line_extension_table.c.extension_id]))
    return op.get_bind().execute(query).fetchall()


def _user_line_exists(line_id):
    query = (
        sa.sql.select(
            [user_line_table.c.user_id, user_line_table.c.line_id])
        .where(user_line_table.c.line_id == line_id))
    return op.get_bind().execute(query).fetchall()


def _populate_user_line_from_line_extension():
    for line_extension in _get_all_line_extension_from_line_extension():
        if _user_line_exists(line_extension.line_id):
            query = (user_line_table
                     .update()
                     .where(user_line_table.c.line_id == line_extension.line_id)
                     .values(extension_id=line_extension.extension_id))
        else:
            query = (user_line_table
                     .insert()
                     .values(user_id=None,
                             line_id=line_extension.line_id,
                             extension_id=line_extension.extension_id,
                             main_line=True,
                             main_user=True))

        op.get_bind().execute(query)
