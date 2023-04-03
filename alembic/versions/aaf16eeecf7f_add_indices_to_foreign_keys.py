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

    op.create_index('agentfeatures__idx__tenant_uuid', 'agentfeatures', ['tenant_uuid'])
    op.create_index('application__idx__tenant_uuid', 'application', ['tenant_uuid'])
    op.create_index('callfilter__idx__tenant_uuid', 'callfilter', ['tenant_uuid'])
    op.create_index('conference__idx__tenant_uuid', 'conference', ['tenant_uuid'])
    op.create_index('context__idx__tenant_uuid', 'context', ['tenant_uuid'])
    op.create_index('endpoint_sip_section__idx__endpoint_sip_uuid', 'endpoint_sip_section', ['endpoint_sip_uuid'])
    op.create_index('endpoint_sip_section_option__idx__endpoint_sip_section_uuid', 'endpoint_sip_section_option', ['endpoint_sip_section_uuid'])
    op.create_index('func_key_template__idx__tenant_uuid', 'func_key_template', ['tenant_uuid'])
    op.create_index('groupfeatures__idx__tenant_uuid', 'groupfeatures', ['tenant_uuid'])
    op.create_index('incall__idx__tenant_uuid', 'incall', ['tenant_uuid'])
    op.create_index('ingress_http__idx__tenant_uuid', 'ingress_http', ['tenant_uuid'])
    op.create_index('ivr__idx__tenant_uuid', 'ivr', ['tenant_uuid'])
    op.create_index('linefeatures__idx__application_uuid', 'linefeatures', ['application_uuid'])
    op.create_index('linefeatures__idx__endpoint_sip_uuid', 'linefeatures', ['endpoint_sip_uuid'])
    op.create_index('meeting__idx__guest_endpoint_sip_uuid', 'meeting', ['guest_endpoint_sip_uuid'])
    op.create_index('meeting__idx__tenant_uuid', 'meeting', ['tenant_uuid'])
    op.create_index('meeting_authorization__idx__guest_uuid', 'meeting_authorization', ['guest_uuid'])
    op.create_index('meeting_authorization__idx__meeting_uuid', 'meeting_authorization', ['meeting_uuid'])
    op.create_index('moh__idx__tenant_uuid', 'moh', ['tenant_uuid'])
    op.create_index('outcall__idx__tenant_uuid', 'outcall', ['tenant_uuid'])
    op.create_index('paging__idx__tenant_uuid', 'paging', ['tenant_uuid'])
    op.create_index('parking_lot__idx__tenant_uuid', 'parking_lot', ['tenant_uuid'])
    op.create_index('pickup__idx__tenant_uuid', 'pickup', ['tenant_uuid'])
    op.create_index('pjsip_transport_option__idx__pjsip_transport_uuid', 'pjsip_transport_option', ['pjsip_transport_uuid'])
    op.create_index('queuefeatures__idx__tenant_uuid', 'queuefeatures', ['tenant_uuid'])
    op.create_index('queueskill__idx__tenant_uuid', 'queueskill', ['tenant_uuid'])
    op.create_index('queueskillrule__idx__tenant_uuid', 'queueskillrule', ['tenant_uuid'])
    op.create_index('rightcall__idx__tenant_uuid', 'rightcall', ['tenant_uuid'])
    op.create_index('sccpline__idx__tenant_uuid', 'sccpline', ['tenant_uuid'])
    op.create_index('schedule__idx__tenant_uuid', 'schedule', ['tenant_uuid'])
    op.create_index('switchboard__idx__tenant_uuid', 'switchboard', ['tenant_uuid'])
    op.create_index('switchboard__idx__hold_moh_uuid', 'switchboard', ['hold_moh_uuid'])
    op.create_index('switchboard__idx__queue_moh_uuid', 'switchboard', ['queue_moh_uuid'])
    op.create_index('switchboard_member_user__idx__user_uuid', 'switchboard_member_user', ['user_uuid'])
    op.create_index('tenant__idx__global_sip_template_uuid', 'tenant', ['global_sip_template_uuid'])
    op.create_index('tenant__idx__webrtc_sip_template_uuid', 'tenant', ['webrtc_sip_template_uuid'])
    op.create_index('tenant__idx__registration_trunk_sip_template_uuid', 'tenant', ['registration_trunk_sip_template_uuid'])
    op.create_index('tenant__idx__meeting_guest_sip_template_uuid', 'tenant', ['meeting_guest_sip_template_uuid'])
    op.create_index('tenant__idx__twilio_trunk_sip_template_uuid', 'tenant', ['twilio_trunk_sip_template_uuid'])
    op.create_index('trunkfeatures__idx__tenant_uuid', 'trunkfeatures', ['tenant_uuid'])
    op.create_index('trunkfeatures__idx__endpoint_sip_uuid', 'trunkfeatures', ['endpoint_sip_uuid'])
    op.create_index('usercustom__idx__tenant_uuid', 'usercustom', ['tenant_uuid'])
    op.create_index('userfeatures__idx__tenant_uuid', 'userfeatures', ['tenant_uuid'])
    op.create_index('useriax__idx__tenant_uuid', 'useriax', ['tenant_uuid'])
    op.create_index('usersip__idx__tenant_uuid', 'usersip', ['tenant_uuid'])


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

    op.drop_index('agentfeatures__idx__tenant_uuid')
    op.drop_index('application__idx__tenant_uuid')
    op.drop_index('callfilter__idx__tenant_uuid')
    op.drop_index('conference__idx__tenant_uuid')
    op.drop_index('context__idx__tenant_uuid')
    op.drop_index('endpoint_sip_section__idx__endpoint_sip_uuid')
    op.drop_index('endpoint_sip_section_option__idx__endpoint_sip_section_uuid')
    op.drop_index('func_key_template__idx__tenant_uuid')
    op.drop_index('groupfeatures__idx__tenant_uuid')
    op.drop_index('incall__idx__tenant_uuid')
    op.drop_index('ingress_http__idx__tenant_uuid')
    op.drop_index('ivr__idx__tenant_uuid')
    op.drop_index('linefeatures__idx__application_uuid')
    op.drop_index('linefeatures__idx__endpoint_sip_uuid')
    op.drop_index('meeting__idx__guest_endpoint_sip_uuid')
    op.drop_index('meeting__idx__tenant_uuid')
    op.drop_index('meeting_authorization__idx__guest_uuid')
    op.drop_index('meeting_authorization__idx__meeting_uuid')
    op.drop_index('moh__idx__tenant_uuid')
    op.drop_index('outcall__idx__tenant_uuid')
    op.drop_index('paging__idx__tenant_uuid')
    op.drop_index('parking_lot__idx__tenant_uuid')
    op.drop_index('pickup__idx__tenant_uuid')
    op.drop_index('pjsip_transport_option__idx__pjsip_transport_uuid')
    op.drop_index('queuefeatures__idx__tenant_uuid')
    op.drop_index('queueskill__idx__tenant_uuid')
    op.drop_index('queueskillrule__idx__tenant_uuid')
    op.drop_index('rightcall__idx__tenant_uuid')
    op.drop_index('sccpline__idx__tenant_uuid')
    op.drop_index('schedule__idx__tenant_uuid')
    op.drop_index('switchboard__idx__tenant_uuid')
    op.drop_index('switchboard__idx__hold_moh_uuid')
    op.drop_index('switchboard__idx__queue_moh_uuid')
    op.drop_index('switchboard_member_user__idx__user_uuid')
    op.drop_index('tenant__idx__global_sip_template_uuid')
    op.drop_index('tenant__idx__webrtc_sip_template_uuid')
    op.drop_index('tenant__idx__registration_trunk_sip_template_uuid')
    op.drop_index('tenant__idx__meeting_guest_sip_template_uuid')
    op.drop_index('tenant__idx__twilio_trunk_sip_template_uuid')
    op.drop_index('trunkfeatures__idx__tenant_uuid')
    op.drop_index('trunkfeatures__idx__endpoint_sip_uuid')
    op.drop_index('usercustom__idx__tenant_uuid')
    op.drop_index('userfeatures__idx__tenant_uuid')
    op.drop_index('useriax__idx__tenant_uuid')
    op.drop_index('usersip__idx__tenant_uuid')
