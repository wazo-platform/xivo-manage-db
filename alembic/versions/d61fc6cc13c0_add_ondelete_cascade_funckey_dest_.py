"""add_ondelete_cascade_funckey_dest_conference

Revision ID: d61fc6cc13c0
Revises: 3067298c4cca

"""

from alembic import op

revision = 'd61fc6cc13c0'
down_revision = '3067298c4cca'


def upgrade():
    op.execute("""
        ALTER TABLE func_key_dest_conference
        DROP CONSTRAINT func_key_dest_conference_conference_id_fkey CASCADE;""")

    op.execute("""
        ALTER TABLE func_key_dest_conference
        ADD CONSTRAINT func_key_dest_conference_conference_id_fkey
        FOREIGN KEY (conference_id)
        REFERENCES conference(id)
        ON DELETE CASCADE;""")



def downgrade():
    op.execute("""
        ALTER TABLE func_key_dest_conference
        DROP CONSTRAINT func_key_dest_conference_conference_id_fkey CASCADE""")

    op.execute("""
        ALTER TABLE func_key_dest_conference
        ADD CONSTRAINT func_key_dest_conference_conference_id_fkey
        FOREIGN KEY (conference_id)
        REFERENCES conference(id)""")
