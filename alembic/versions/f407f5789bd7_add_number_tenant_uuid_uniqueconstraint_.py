"""add_number_tenant_uuid_uniqueconstraint_agentfeatures

Revision ID: f407f5789bd7
Revises: 767da50673df

"""

from alembic import op


revision = 'f407f5789bd7'
down_revision = '767da50673df'


def upgrade():
    op.drop_constraint(
        'agentfeatures_number_key',
        'agentfeatures')
    op.create_unique_constraint(
        'agentfeatures_number_tenant_uuid_key',
        'agentfeatures',
        ['number', 'tenant_uuid'])

def downgrade():
    op.drop_constraint(
        'agentfeatures_number_tenant_uuid_key',
        'agentfeatures')
    op.create_unique_constraint(
        'agentfeatures_number_key',
        'agentfeatures',
        ['number'])
