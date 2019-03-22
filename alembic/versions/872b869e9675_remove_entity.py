"""remove entity

Revision ID: 872b869e9675
Revises: 90f771359c71

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '872b869e9675'
down_revision = '90f771359c71'


def upgrade():
    op.drop_column('schedule', 'entity_id')
    op.drop_column('pickup', 'entity_id')
    op.drop_column('callfilter', 'entity_id')
    op.drop_column('userfeatures', 'entityid')
    op.drop_column('context', 'entity')
    op.drop_table('entity')


def downgrade():
    pass
