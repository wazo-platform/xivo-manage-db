"""remove constraints from linefeatures

Revision ID: 20d4630f2c8e
Revises: 46dbcd084872

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '20d4630f2c8e'
down_revision = '46dbcd084872'


def upgrade():
    op.alter_column('linefeatures', 'protocol', nullable=True)
    op.alter_column('linefeatures', 'protocolid', nullable=True)
    op.alter_column('linefeatures', 'name', nullable=True)
    op.alter_column('linefeatures', 'num', server_default='1')
    op.create_unique_constraint('linefeatures_provisioningid_key',
                                "linefeatures",
                                ['provisioningid'])


def downgrade():
    op.alter_column('linefeatures', 'protocol', nullable=False)
    op.alter_column('linefeatures', 'protocolid', nullable=False)
    op.alter_column('linefeatures', 'name', nullable=False)
    op.alter_column('linefeatures', 'num', server_default='0')
    op.drop_constraint('linefeatures_provisioningid_key', 'linefeatures')
