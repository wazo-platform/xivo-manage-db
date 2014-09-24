"""queue_autopause_option

Revision ID: 58e808b69aec
Revises: 2c6c9833d839

"""

# revision identifiers, used by Alembic.
revision = '58e808b69aec'
down_revision = '2c6c9833d839'

from alembic import op


def upgrade():
    qry = """ALTER TABLE queue ALTER COLUMN autopause TYPE varchar(3);"""
    op.execute(qry)
    qry = """ALTER TABLE queue ALTER COLUMN autopause SET DEFAULT 'no';"""
    op.execute(qry)
    qry = """UPDATE queue SET autopause='yes' WHERE autopause='1';"""
    op.execute(qry)
    qry = """UPDATE queue SET autopause='no' WHERE autopause='0';"""
    op.execute(qry)
    qry = """ALTER TABLE queue ADD CONSTRAINT queue_autopause CHECK (autopause IN ('no','yes','all'));"""
    op.execute(qry)


def downgrade():
    qry = """ALTER TABLE queue DROP CONSTRAINT queue_autopause;"""
    op.execute(qry)
    qry = """UPDATE queue SET autopause='1' WHERE autopause in ('yes','all');"""
    op.execute(qry)
    qry = """UPDATE queue SET autopause='0' WHERE autopause='no';"""
    op.execute(qry)
    qry = """ALTER TABLE queue ALTER COLUMN autopause SET DEFAULT 1;"""
    op.execute(qry)
    qry = """ALTER TABLE queue ALTER COLUMN autopause TYPE integer USING (autopause::integer);"""
    op.execute(qry)
