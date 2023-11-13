"""fix-toggle-record-default-value

Revision ID: 3067298c4cca
Revises: 2b68f2a8c0b3

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3067298c4cca'
down_revision = '2b68f2a8c0b3'

features_table = sa.sql.table(
    'features',
    sa.sql.column('id'),
    sa.sql.column('filename'),
    sa.sql.column('category'),
    sa.sql.column('var_name'),
    sa.sql.column('var_val'),
)

WRONG_VALUE = '*3,self,AGI(agi://${{XIVO_AGID_IP}}/call_recording)'
CORRECT_VALUE = '*3,self,AGI(agi://${XIVO_AGID_IP}/call_recording)'


def upgrade():
    query = (
        features_table.update()
        .values(
            filename='features.conf',
            category='applicationmap',
            var_name='togglerecord',
            var_val=CORRECT_VALUE,
        )
        .where(
            sa.sql.and_(
                features_table.c.filename == 'features.conf',
                features_table.c.category == 'applicationmap',
                features_table.c.var_name == 'togglerecord',
                features_table.c.var_val == WRONG_VALUE,
            )
        )
    )
    op.execute(query)


def downgrade():
    pass
