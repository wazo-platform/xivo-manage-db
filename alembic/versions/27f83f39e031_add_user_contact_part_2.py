"""add user_contact part 2

Revision ID: 27f83f39e031
Revises: 3c14d64c95a3
XiVO Version: 14.11

"""

# revision identifiers, used by Alembic.
revision = '27f83f39e031'
down_revision = '3c14d64c95a3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute(sa.text('DROP TABLE IF EXISTS "user_contact"'))
    op.create_table(
        'user_contact',
        sa.Column('user_id', sa.Integer),
        sa.Column('phonebook_id', sa.Integer),
        sa.PrimaryKeyConstraint('user_id', 'phonebook_id'),
        sa.ForeignKeyConstraint(
            ['phonebook_id'],
            ['phonebook.id'],
            name='user_contact_phonebook_id_fkey',
            ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['userfeatures.id'],
            name='user_contact_user_id_fkey',
            ondelete='CASCADE',
        ),
    )


def downgrade():
    pass
