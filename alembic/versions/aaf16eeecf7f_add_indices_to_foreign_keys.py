"""add_indices_to_foreign_keys

Revision ID: aaf16eeecf7f
Revises: 8bbb46a9f362

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaf16eeecf7f'
down_revision = '8bbb46a9f362'


def upgrade():
    op.create_index('agent_login_status__idx__agent_id', 'agent_login_status', ['agent_id'])

    op.create_index('agent_membership_status__idx__agent_id', 'agent_membership_status', ['agent_id'])
    op.create_index('agent_membership_status__idx__queue_id', 'agent_membership_status', ['queue_id'])

    op.create_index('asterisk_file_section__idx__asterisk_file_id', 'asterisk_file_section', ['asterisk_file_id'])
    op.create_index('asterisk_file_variable__idx__asterisk_file_section_id', 'asterisk_file_variable', ['asterisk_file_section_id'])

    op.create_index('func_key__idx__type_id', 'func_key', ['type_id'])

    op.create_index('func_key_dest_agent__idx__agent_id', 'func_key_dest_agent', ['agent_id'])
    op.create_index('func_key_dest_agent__idx__extension_id', 'func_key_dest_agent', ['extension_id'])

    op.create_index('func_key_dest_bsfilter__idx__filtermember_id', 'func_key_dest_bsfilter', ['filtermember_id'])

    op.create_index('func_key_dest_features__idx__features_id', 'func_key_dest_features', ['features_id'])

    op.create_index('func_key_dest_forward__idx__extension_id', 'func_key_dest_forward', ['extension_id'])

    op.create_index('func_key_dest_groupmember__idx__group_id', 'func_key_dest_groupmember', ['group_id'])
    op.create_index('func_key_dest_groupmember__idx__extension_id', 'func_key_dest_groupmember', ['extension_id'])

    op.create_index('func_key_dest_paging__idx__paging_id', 'func_key_dest_paging', ['paging_id'])

    op.create_index('func_key_dest_service__idx__extension_id', 'func_key_dest_service', ['extension_id'])

    op.create_index('ivr_choice__idx__ivr_id', 'ivr_choice', ['ivr_id'])

    op.create_index('line_extension__idx__line_id', 'line_extension', ['line_id'])
    op.create_index('line_extension__idx__extension_id', 'line_extension', ['extension_id'])

    op.create_index('linefeatures__idx__endpoint_sccp_id', 'linefeatures', ['endpoint_sccp_id'])
    op.create_index('linefeatures__idx__endpoint_custom_id', 'linefeatures', ['endpoint_custom_id'])

    op.create_index('schedule_path__idx__schedule_id', 'schedule_path', ['schedule_id'])

    op.create_index('stat_call_on_queue__idx__stat_agent_id', 'stat_call_on_queue', ['stat_agent_id'])
    op.create_index('stat_call_on_queue__idx__stat_queue_id', 'stat_call_on_queue', ['stat_queue_id'])

    op.create_index('stat_queue_periodic__idx__stat_queue_id', 'stat_queue_periodic', ['stat_queue_id'])

    op.create_index('trunkfeatures__idx__endpoint_iax_id', 'trunkfeatures', ['endpoint_iax_id'])
    op.create_index('trunkfeatures__idx__endpoint_custom_id', 'trunkfeatures', ['endpoint_custom_id'])
    op.create_index('trunkfeatures__idx__register_iax_id', 'trunkfeatures', ['register_iax_id'])

    op.create_index('user_line__idx__user_id', 'user_line', ['user_id'])
    op.create_index('user_line__idx__line_id', 'user_line', ['line_id'])

    op.create_index('userfeatures__idx__func_key_template_id', 'userfeatures', ['func_key_template_id'])
    op.create_index('userfeatures__idx__func_key_private_template_id', 'userfeatures', ['func_key_private_template_id'])


def downgrade():
    op.drop_index('agent_login_status__idx__agent_id')

    op.drop_index('agent_membership_status__idx__agent_id')
    op.drop_index('agent_membership_status__idx__queue_id')

    op.drop_index('asterisk_file_section__idx__asterisk_file_id')
    op.drop_index('asterisk_file_variable__idx__asterisk_file_section_id')

    op.drop_index('func_key__idx__type_id')

    op.drop_index('func_key_dest_agent__idx__agent_id')
    op.drop_index('func_key_dest_agent__idx__extension_id')

    op.drop_index('func_key_dest_bsfilter__idx__filtermember_id')

    op.drop_index('func_key_dest_features__idx__features_id')

    op.drop_index('func_key_dest_forward__idx__extension_id')

    op.drop_index('func_key_dest_groupmember__idx__group_id')
    op.drop_index('func_key_dest_groupmember__idx__extension_id')

    op.drop_index('func_key_dest_paging__idx__paging_id')

    op.drop_index('func_key_dest_service__idx__extension_id')

    op.drop_index('ivr_choice__idx__ivr_id')

    op.drop_index('line_extension__idx__line_id')
    op.drop_index('line_extension__idx__extension_id')

    op.drop_index('linefeatures__idx__endpoint_sccp_id')
    op.drop_index('linefeatures__idx__endpoint_custom_id')

    op.drop_index('schedule_path__idx__schedule_id')

    op.drop_index('stat_call_on_queue__idx__stat_agent_id')
    op.drop_index('stat_call_on_queue__idx__stat_queue_id')

    op.drop_index('stat_queue_periodic__idx__stat_queue_id')

    op.drop_index('trunkfeatures__idx__endpoint_iax_id')
    op.drop_index('trunkfeatures__idx__endpoint_custom_id')
    op.drop_index('trunkfeatures__idx__register_iax_id')

    op.drop_index('user_line__idx__user_id')
    op.drop_index('user_line__idx__line_id')

    op.drop_index('userfeatures__idx__func_key_template_id')
    op.drop_index('userfeatures__idx__func_key_private_template_id')
