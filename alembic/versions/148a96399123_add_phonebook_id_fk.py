"""add phonebook id fk

Revision ID: 148a96399123
Revises: 1d05ffb14525
Create Date: 2014-05-20 13:11:13.362172
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '148a96399123'
down_revision = '1d05ffb14525'

from alembic import op
import sqlalchemy as sa


phonebook_table = sa.sql.table(
    'phonebook',
    sa.sql.column('id'),
)


def upgrade():
    _add_phonebook_fk('phonebooknumber')
    _add_phonebook_fk('phonebookaddress')


def downgrade():
    op.drop_constraint('fk_phonebook_id', 'phonebookaddress')
    op.drop_constraint('fk_phonebook_id', 'phonebooknumber')


def _add_phonebook_fk(table_name):
    _remove_orphaned(table_name)
    op.create_foreign_key(
        'fk_phonebook_id',
        table_name,
        'phonebook',
        ['phonebookid'],
        ['id'],
        ondelete='CASCADE',
    )


def _remove_orphaned(table_name):
    table = sa.sql.table(
        table_name,
        sa.sql.column('id'),
        sa.sql.column('phonebookid'),
    )

    existing_phonebook_ids_query = (
        sa.sql.select([phonebook_table.c.id])
    )

    orphaned_numbers_query = (
        sa.sql.select(
            [table.c.id]
        ).where(~table.c.phonebookid.in_(existing_phonebook_ids_query))
    )

    delete_query = (
        table.delete()
        .where(table.c.id.in_(orphaned_numbers_query))
    )

    op.get_bind().execute(delete_query)
