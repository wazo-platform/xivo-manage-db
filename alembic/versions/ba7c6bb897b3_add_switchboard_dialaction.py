"""add_switchboard_dialaction

Revision ID: ba7c6bb897b3
Revises: 06e9e3483fec

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba7c6bb897b3'
down_revision = '06e9e3483fec'

old_categories = (
    'callfilter',
    'group',
    'incall',
    'queue',
    'user',
    'ivr',
    'ivr_choice',
)
new_categories = sorted(old_categories + ('switchboard',))

new_type = sa.Enum(*new_categories, name='dialaction_category')
old_type = sa.Enum(*old_categories, name='dialaction_category')
tmp_type = sa.Enum(*new_categories, name='dialaction_category_being_replaced')

dialaction_table = sa.sql.table('dialaction',
                                sa.Column('category', new_type, nullable=False))


def upgrade():
    _add_dialaction()


def _add_dialaction():
    op.execute('ALTER TYPE dialaction_category RENAME TO dialaction_category_being_replaced')

    new_type.create(op.get_bind())
    op.execute('ALTER TABLE dialaction ALTER COLUMN category TYPE dialaction_category USING category::text::dialaction_category')

    tmp_type.drop(op.get_bind(), checkfirst=False)


def downgrade():
    _remove_dialaction()


def _remove_dialaction():
    op.execute(dialaction_table
               .delete()
               .where(dialaction_table.c.category == 'switchboard'))

    op.execute('ALTER TYPE dialaction_category RENAME TO dialaction_category_being_replaced')

    old_type.create(op.get_bind())
    op.execute('ALTER TABLE dialaction ALTER COLUMN category TYPE dialaction_category USING category::text::dialaction_category')

    tmp_type.drop(op.get_bind(), checkfirst=False)
