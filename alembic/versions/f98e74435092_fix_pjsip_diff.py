"""fix-pjsip-diff

Revision ID: f98e74435092
Revises: f1fea68b56d9

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'f98e74435092'
down_revision = 'f1fea68b56d9'


def upgrade():
    op.drop_constraint('trunkfeatures_registers_check', 'trunkfeatures')

    op.drop_constraint('trunkfeatures_endpoints_check', 'trunkfeatures')
    op.drop_constraint('trunkfeatures_endpoint_register_check', 'trunkfeatures')
    op.drop_constraint('linefeatures_endpoints_check', 'linefeatures')

    op.drop_column('linefeatures', 'endpoint_sip_id')
    op.drop_column('trunkfeatures', 'endpoint_sip_id')
    op.drop_column('trunkfeatures', 'register_sip_id')

    op.create_check_constraint(
        'trunkfeatures_endpoints_check',
        'trunkfeatures',
        '''
        ( CASE WHEN endpoint_sip_uuid IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_iax_id IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_custom_id IS NULL THEN 0 ELSE 1 END
        ) <= 1
        ''',
    )
    op.create_check_constraint(
        'trunkfeatures_endpoint_register_check',
        'trunkfeatures',
        '''
        (
            register_iax_id IS NULL
        ) OR (
            register_iax_id IS NOT NULL AND
            endpoint_sip_uuid IS NULL AND
            endpoint_custom_id IS NULL
        )
        ''',
    )

    op.create_check_constraint(
        'linefeatures_endpoints_check',
        'linefeatures',
        '''
        ( CASE WHEN endpoint_sip_uuid IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_sccp_id IS NULL THEN 0 ELSE 1 END
        + CASE WHEN endpoint_custom_id IS NULL THEN 0 ELSE 1 END
        ) <= 1
        ''',
    )


def downgrade():
    pass
