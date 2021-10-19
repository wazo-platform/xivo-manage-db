"""add auth session_uuid index

Revision ID: 89df34ff3e66
Revises: 035908ce02df

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89df34ff3e66'
down_revision = '035908ce02df'


def upgrade():
    # What we should be careful of: some production systems already have the index in place
    # since it was fixed by support
    idx_to_rename = {
        'auth_token_session_uuid_idx': 'auth_token__idx__session_uuid',
    }
    conn = op.get_bind()
    for idx, idx_renamed in idx_to_rename.items():
        conn.execute(
            sa.text(
                f'ALTER INDEX IF EXISTS {idx} RENAME TO {idx_renamed};'
            )
        )

    conn.execute(
        sa.text('CREATE INDEX IF NOT EXISTS auth_token__idx__session_uuid ON auth_token (session_uuid);')
    )


def downgrade():
    op.drop_index('auth_token__idx__session_uuid')
