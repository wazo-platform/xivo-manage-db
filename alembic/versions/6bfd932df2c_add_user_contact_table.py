"""add user_contact table

Revision ID: 6bfd932df2c
Revises: 148a96399123
XiVO Version: <version>

"""

# revision identifiers, used by Alembic.
revision = '6bfd932df2c'
down_revision = '148a96399123'

from alembic import op
import sqlalchemy as sa


phonebook_table = sa.sql.table(
    'phonebook',
    sa.sql.column('id'),
)


def upgrade():
    op.create_table(
        'user_contact',
        sa.Column('user_id', sa.Integer),
        sa.Column('phonebook_id', sa.Integer),
        sa.PrimaryKeyConstraint('user_id', 'phonebook_id'),
        sa.ForeignKeyConstraint(
            ['phonebook_id'],
            ['phonebook.id'],
            name='fk_phonebook_id',
            ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['userfeatures.id'],
            name='fk_user_id',
            ondelete='CASCADE',
        ),
    )


def downgrade():
    _remove_private_contacts()
    op.drop_table('user_contact')


def _remove_private_contacts():
    user_contact_table = sa.sql.table(
        'user_contact',
        sa.sql.column('user_id'),
        sa.sql.column('phonebook_id'),
    )

    personnal_contact_query = (
        sa.sql.select(
            [user_contact_table.c.phonebook_id]
        )
    )

    delete_query = (
        phonebook_table.delete().where(phonebook_table.c.id.in_(personnal_contact_query))
    )

    op.get_bind().execute(delete_query)
