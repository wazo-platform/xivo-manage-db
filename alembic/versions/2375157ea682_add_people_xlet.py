"""add people xlet

Revision ID: 2375157ea682
Revises: 2077c9fc2d49

"""

# revision identifiers, used by Alembic.
revision = '2375157ea682'
down_revision = '2077c9fc2d49'

from alembic import op


def upgrade():
    op.execute("""DELETE FROM "cti_xlet" WHERE "plugin_name" = 'people'""")
    op.execute("""INSERT INTO "cti_xlet" VALUES (DEFAULT, 'people')""")


def downgrade():
    op.execute("""DELETE FROM "cti_xlet" WHERE "plugin_name" = 'people'""")
