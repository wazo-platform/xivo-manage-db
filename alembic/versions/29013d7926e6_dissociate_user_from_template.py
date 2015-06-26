"""dissociate_user_from_template

Revision ID: 29013d7926e6
Revises: 5a4fe661486c

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '29013d7926e6'
down_revision = '5a4fe661486c'


def upgrade():
    op.drop_constraint('userfeatures_func_key_template_id_fkey', 'userfeatures')
    op.create_foreign_key('userfeatures_func_key_template_id_fkey',
                          'userfeatures',
                          'func_key_template',
                          ['func_key_template_id'],
                          ['id'],
                          ondelete="SET NULL")


def downgrade():
    op.drop_constraint('userfeatures_func_key_template_id_fkey', 'userfeatures')
    op.create_foreign_key('userfeatures_func_key_template_id_fkey',
                          'userfeatures',
                          'func_key_template',
                          ['func_key_template_id'],
                          ['id'])
