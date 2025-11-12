"""Replace shared field with accesstype enum for voicemail

Revision ID: f0046ed0d70e
Revises: f16fdc26c6c6

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.sql import text
from sqlalchemy import DDL
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'f0046ed0d70e'
down_revision = 'f16fdc26c6c6'

voicemail_table = sa.sql.table(
    'voicemail',
    sa.sql.column('uniqueid'),
    sa.sql.column('shared'),
    sa.sql.column('accesstype'),
    sa.sql.column('context'),
)


def upgrade():
    # Create enum type explicitly using DDL
    create_enum = DDL("CREATE TYPE voicemail_accesstype AS ENUM ('personal', 'global')")
    op.get_bind().execute(create_enum)

    # Add accesstype column with enum type and default value
    accesstype_enum = postgresql.ENUM('personal', 'global', name='voicemail_accesstype', create_type=False)
    op.add_column('voicemail', sa.Column('accesstype', accesstype_enum, nullable=False, server_default=text("'personal'::voicemail_accesstype")))

    # Migrate data: shared=true -> 'global', shared=false -> 'personal'
    update_shared_voicemails = (
        voicemail_table
        .update()
        .where(voicemail_table.c.shared == True)
        .values(accesstype='global')
    )
    op.get_bind().execute(update_shared_voicemails)

    op.create_index(
        'voicemail__idx__unique_global_per_context',
        'voicemail',
        ['accesstype', 'context'],
        unique=True,
        postgresql_where=(text("accesstype = 'global'"))
    )

    op.drop_index('voicemail__idx__unique_shared_per_context', 'voicemail')
    op.drop_column('voicemail', 'shared')


def downgrade():
    op.add_column('voicemail', sa.Column('shared', sa.Boolean, nullable=False, server_default=text('false')))

    # Migrate data: accesstype='global' -> shared=true, accesstype='personal' -> shared=false
    update_global_voicemails = (
        voicemail_table
        .update()
        .where(voicemail_table.c.accesstype == 'global')
        .values(shared=True)
    )
    op.get_bind().execute(update_global_voicemails)

    op.create_index(
        'voicemail__idx__unique_shared_per_context',
        'voicemail',
        ['shared', 'context'],
        unique=True,
        postgresql_where=(text('shared is true'))
    )

    op.drop_index('voicemail__idx__unique_global_per_context', 'voicemail')
    op.drop_column('voicemail', 'accesstype')

    # Drop enum type using DDL
    drop_enum = DDL('DROP TYPE voicemail_accesstype')
    op.get_bind().execute(drop_enum)
