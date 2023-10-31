"""delete_orphan_queues

Revision ID: 91b9efd85e0b
Revises: 11aa576dba87

"""

from alembic import op


revision = '91b9efd85e0b'
down_revision = '11aa576dba87'


def upgrade():
    op.execute(
        """DELETE FROM queue WHERE name NOT IN (
        SELECT name FROM queuefeatures) 
        AND name NOT IN (SELECT name FROM groupfeatures)"""
    )


def downgrade():
    pass
