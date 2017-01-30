"""drop musiconhold table

Revision ID: 1ddfb39a066f
Revises: 33fa1a10428f

"""

# revision identifiers, used by Alembic.
revision = '1ddfb39a066f'
down_revision = '33fa1a10428f'

from alembic import op
from sqlalchemy import Column, PrimaryKeyConstraint, Integer, String, UniqueConstraint


def upgrade():
    op.execute('''
INSERT INTO moh (uuid, name, mode, application, sort)
SELECT
  uuid_generate_v4(),
  category,
  CASE (SELECT var_val FROM musiconhold WHERE category = m.category AND commented = 0 AND var_name = 'mode')
    WHEN 'custom' THEN 'custom'
    WHEN 'mp3' THEN 'mp3'
    WHEN 'mp3nb' THEN 'mp3'
    WHEN 'quietmp3' THEN 'mp3'
    WHEN 'quietmp3nb' THEN 'mp3'
    ELSE 'files'
  END,
  (SELECT var_val FROM musiconhold WHERE category = m.category AND commented = 0 AND var_name = 'application'),
  CASE (SELECT var_val FROM musiconhold WHERE category = m.category AND commented = 0 AND var_name = 'sort')
    WHEN 'alpha' THEN 'alphabetical'
    WHEN 'random' THEN 'random'
    WHEN 'randstart' THEN 'random_start'
  END
FROM
  musiconhold AS m
GROUP BY
  category;
''')
    op.drop_table('musiconhold')


def downgrade():
    op.create_table(
        'musiconhold',
        Column('id', Integer),
        Column('cat_metric', Integer, nullable=False, server_default='0'),
        Column('var_metric', Integer, nullable=False, server_default='0'),
        Column('commented', Integer, nullable=False, server_default='0'),
        Column('filename', String(128), nullable=False),
        Column('category', String(128), nullable=False),
        Column('var_name', String(128), nullable=False),
        Column('var_val', String(128)),
        PrimaryKeyConstraint('id'),
        UniqueConstraint('filename', 'category', 'var_name'),
    )
