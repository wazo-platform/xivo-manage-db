"""remove-default-moh

Revision ID: 30fc2693c6fc
Revises: 3a893dbde0e0

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '30fc2693c6fc'
down_revision = '3a893dbde0e0'


def upgrade():
    op.execute("""
    DELETE FROM moh WHERE name='default' and label='default'
    """)

def downgrade():
    op.execute("""
    INSERT INTO moh (uuid, name, label, mode, tenant_uuid) 
    VALUES(uuid_generate_v4(), 'default', 'default', 'files', (SELECT uuid from tenant WHERE slug = 'master'))
    """)
