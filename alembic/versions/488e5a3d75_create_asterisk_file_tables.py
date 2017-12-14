"""create_asterisk_file_tables

Revision ID: 488e5a3d75
Revises: 40359c5c2c92

"""

# revision identifiers, used by Alembic.
revision = '488e5a3d75'
down_revision = '40359c5c2c92'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import Column

constraint_name = 'asterisk_file_section_name_asterisk_file_id_key'


def upgrade():
    op.create_table(
        'asterisk_file',
        Column('id', sa.Integer, primary_key=True),
        Column('name', sa.String(255), unique=True, nullable=False),
    )

    op.create_table(
        'asterisk_file_section',
        Column('id', sa.Integer, primary_key=True),
        Column('name', sa.String(255), nullable=False),
        Column('priority', sa.Integer),
        Column('asterisk_file_id', sa.Integer,
               sa.ForeignKey('asterisk_file.id', ondelete='CASCADE'),
               nullable=False),
    )
    op.create_table(
        'asterisk_file_variable',
        Column('id', sa.Integer, primary_key=True),
        Column('key', sa.String(255), nullable=False),
        Column('value', sa.Text),
        Column('priority', sa.Integer),
        Column('asterisk_file_section_id', sa.Integer,
               sa.ForeignKey('asterisk_file_section.id', ondelete='CASCADE'),
               nullable=False),
    )
    op.create_unique_constraint(constraint_name, 'asterisk_file_section',
                                ['name', 'asterisk_file_id'])


def downgrade():
    op.drop_constraint(constraint_name, 'asterisk_file_section')
    op.drop_table('asterisk_file_variable')
    op.drop_table('asterisk_file_section')
    op.drop_table('asterisk_file')
