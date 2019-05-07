"""queueskillrule remove name unique constraint

Revision ID: 15ca57fa1b71
Revises: 73889d1db031

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15ca57fa1b71'
down_revision = '73889d1db031'

queueskillrule_tbl = sa.sql.table(
    'queueskillrule',
    sa.sql.column('id'),
    sa.sql.column('name')
)


def _remove_duplicates():
    query = sa.sql.select([queueskillrule_tbl.c.id, queueskillrule_tbl.c.name])
    queueskillrules = op.get_bind().execute(query)

    unique_skillrules = set()
    for rule_id, name in queueskillrules:
        if name in unique_skillrules:
            query = (
                queueskillrule_tbl.delete()
                .where(queueskillrule_tbl.c.id == rule_id)
            )
            op.execute(query)
        else:
            unique_skillrules.add(name)


def upgrade():
    op.drop_constraint('queueskillrule_name_key', 'queueskillrule')


def downgrade():
    _remove_duplicates()
    op.create_unique_constraint('queueskillrule_name_key', 'queueskillrule', ['name'])
