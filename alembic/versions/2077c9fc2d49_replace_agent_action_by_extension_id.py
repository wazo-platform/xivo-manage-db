"""replace agent action by extension id

Revision ID: 2077c9fc2d49
Revises: 3ab7cf07eb66

"""

# revision identifiers, used by Alembic.
revision = '2077c9fc2d49'
down_revision = '3ab7cf07eb66'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import sql

ACTIONS = {
    'login': 'agentstaticlogin',
    'logoff': 'agentstaticlogoff',
    'toggle': 'agentstaticlogtoggle'
}

destination_agent = sql.table('func_key_dest_agent',
                              sql.column('func_key_id'),
                              sql.column('action'),
                              sql.column('extension_id'))

extensions = sql.table('extensions',
                       sql.column('id'),
                       sql.column('type'),
                       sql.column('typeval'))


def upgrade():
    op.add_column('func_key_dest_agent',
                  sa.Column('extension_id',
                            sa.Integer(),
                            sa.ForeignKey('extensions.id')),
                  )

    op.create_unique_constraint('func_key_dest_agent_agent_id_extension_id_key',
                                'func_key_dest_agent',
                                ('agent_id', 'extension_id'))

    for action, wonky_action in ACTIONS.items():
        extension_query = (sql.select([extensions.c.id])
                           .where(extensions.c.typeval == wonky_action))

        extension_id = op.get_bind().execute(extension_query).scalar()

        query = (destination_agent
                 .update()
                 .values(extension_id=extension_id)
                 .where(destination_agent.c.action == action))

        op.execute(query)

    op.alter_column('func_key_dest_agent', 'extension_id', nullable=False)
    op.drop_column('func_key_dest_agent', 'action')


def downgrade():
    op.add_column('func_key_dest_agent',
                  sa.Column('action',
                            sa.Unicode(10)))

    op.create_unique_constraint('func_key_dest_agent_id_action_key',
                                'func_key_dest_agent',
                                ('agent_id', 'action'))

    op.create_check_constraint('func_key_dest_agent_action_check',
                               'func_key_dest_agent',
                               "action IN ('login', 'logoff', 'toggle')")

    for action, wonky_action in ACTIONS.items():
        extension_query = (sql.select([extensions.c.id])
                           .where(extensions.c.typeval == wonky_action)
                           .alias())

        query = (destination_agent
                 .update()
                 .values(action=action)
                 .where(destination_agent.c.extension_id == extension_query))

        op.execute(query)

    op.alter_column('func_key_dest_agent', 'action', nullable=False)
    op.drop_column('func_key_dest_agent', 'extension_id')
