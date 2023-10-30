"""remove queueskill category

Revision ID: 11aa576dba87
Revises: bcc124448097

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = '11aa576dba87'
down_revision = 'bcc124448097'


def upgrade():
    op.execute(
        """
        ALTER TABLE queueskill DROP COLUMN catid
        """
    )
    op.execute(
        """
        DROP TABLE queueskillcat
        """
    )


def downgrade():
    op.execute(
        """
        CREATE TABLE queueskillcat (
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) NOT NULL UNIQUE DEFAULT ''
        )
        """
    )
    op.execute(
        """
        INSERT INTO queueskillcat (name) values('Default')
        """
    )
    op.execute(
        """
        ALTER TABLE queueskill
        ADD COLUMN catid INTEGER
        """
    )
    op.execute(
        """
        UPDATE queueskill SET catid = (SELECT id from queueskillcat where name='Default')
        """
    )
