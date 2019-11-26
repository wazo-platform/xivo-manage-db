"""registration options

Revision ID: cc9063471025
Revises: 4c4a8eaa31e7

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc9063471025'
down_revision = '4c4a8eaa31e7'


staticsip_table = sa.sql.table(
    'staticsip',
    sa.sql.column('var_name'),
    sa.sql.column('var_val'),
    sa.sql.column('category'),
    sa.sql.column('filename'),
)

DEFAULTS = {
    'auth_rejection_permanent': 'no',
    'forbidden_retry_interval': 30,
    'fatal_retry_interval': 30,
}
DEFAULT_MAX_RETRIES = 10000


def upgrade():
    query = (
        sa.sql.select(
            [staticsip_table.c.var_name, staticsip_table.c.var_val],
        ).where(
            staticsip_table.c.category == 'general',
        )
    )

    # If registerattemps is configured and not 0 use that value
    max_retries = None
    existing_keys = set()
    for var_name, var_val in op.get_bind().execute(query):
        existing_keys.add(var_name)
        if var_name == 'registerattempts' and var_val not in ('0', 0):
            max_retries = var_val
    DEFAULTS['max_retries'] = max_retries or DEFAULT_MAX_RETRIES

    op.execute(staticsip_table.delete().where(sa.sql.and_(
        staticsip_table.c.category == 'general',
        staticsip_table.c.var_name.in_(DEFAULTS.keys()),
    )))

    for key, value in DEFAULTS.items():
        op.execute(staticsip_table.insert().values(
            var_name=key,
            var_val=value,
            filename='sip.conf',
            category='general',
        ))


def downgrade():
    pass
