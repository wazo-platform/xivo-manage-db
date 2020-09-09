"""sip-to-pjsip-endpoint

Revision ID: ea74eca400ce
Revises: 56a9fce34ae9

"""

import string
import random

from collections import namedtuple

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ea74eca400ce'
down_revision = '56a9fce34ae9'

ALPHANUMERIC_POOL = string.ascii_lowercase + string.digits

KV = namedtuple('KV', ['key', 'value'])

AOR_SECTION_MAPPING = {
    'qualifyfreq': 'qualify_frequency',
    'maxexpiry': 'maximum_expiration',
    'minexpiry': 'minimum_expiration',
    'defaultexpiry': 'default_expiration',
}
AUTH_SECTION_MAPPING = {
    'secret': 'password',
}
ENDPOINT_SECTION_MAPPING = {
    'allowsubscribe': 'allow_subscribe',
    'allowtransfer': 'allow_transfer',
    'autoframing': 'use_ptime',
    'avpf': 'use_avpf',
    'busylevel': 'device_state_busy_at',
    'callingpres': 'callerid_privacy',
    'cid_tag': 'callerid_tag',
    'dtlscafile': 'dtls_ca_file',
    'dtlscapath': 'dtls_ca_path',
    'dtlscertfile': 'dtls_cert_file',
    'dtlscipher': 'dtls_cipher',
    'dtlsprivatekey': 'dtls_private_key',
    'dtlsrekey': 'dtls_rekey',
    'dtlssetup': 'dtls_setup',
    'dtlsverify': 'dtls_verify',
    'fromdomain': 'from_domain',
    'fromuser': 'from_user',
    'icesupport': 'ice_support',
    'mohsuggest': 'moh_suggest',
    'mwifrom': 'mwi_from_user',
    'outboundproxy': 'outbound_proxy',
    'rtptimeout': 'rtp_timeout',
    'rtpholdtimeout': 'rtp_timeout_hold',
    'sdpowner': 'sdp_owner',
    'sdpsession': 'sdp_session',
    'session-expires': 'timers_sess_expires',
    'session-minse': 'timers_min_se',
    'subminexpiry': 'sub_min_expiry',
    'tonezone': 'tone_zone',
    'trustrpid': 'trust_id_inbound',
}
REGISTRATION_SECTION_MAPPING = {
    'registertimeout': 'retry_interval',
    'registerattempts': 'max_retries',
    'outboundproxy': 'outbound_proxy',
}

# Commented options are in multiple sections and are not handled here and in confgend
VALID_AOR_OPTIONS = [
    # 'authenticate_qualify',
    'contact',
    'default_expiration',
    # 'mailboxes',
    'max_contacts',
    'maximum_expiration',
    'minimum_expiration',
    # 'outbound_proxy',
    # 'qualify_frequency',
    # 'qualify_timeout',
    'remove_existing',
    'support_path',
    # 'voicemail_extension',
]
VALID_AUTH_OPTIONS = [
    'auth_type',
    'nonce_lifetime',
    'md5_cred',
    'password',
    'realm',
    'username',
]
VALID_ENDPOINT_OPTIONS = [
    '100rel',
    'accept_multiple_sdp_answers',
    'accountcode',
    'acl',
    'aggregate_mwi',
    'allow',
    'allow_overlap',
    'allow_subscribe',
    'allow_transfer',
    'aors',
    'asymmetric_rtp_codec',
    'auth',
    'bind_rtp_to_media_address',
    'bundle',
    'call_group',
    'callerid',
    'callerid_privacy',
    'callerid_tag',
    'connected_line_method',
    'contact_acl',
    'contact_deny',
    'contact_permit',
    'contact_user',
    # 'context',  # The context of an endpoint uses the trunk or line context
    'cos_audio',
    'cos_video',
    'deny',
    'device_state_busy_at',
    'direct_media',
    'direct_media_glare_mitigation',
    'direct_media_method',
    'disable_direct_media_on_nat',
    'dtls_auto_generate_cert',
    'dtls_ca_file',
    'dtls_ca_path',
    'dtls_cert_file',
    'dtls_cipher',
    'dtls_fingerprint',
    'dtls_private_key',
    'dtls_rekey',
    'dtls_setup',
    'dtls_verify',
    'dtmf_mode',
    'fax_detect',
    'fax_detect_timeout',
    'follow_early_media_fork',
    'force_avp',
    'force_rport',
    'from_domain',
    'from_user',
    'g726_non_standard',
    'ice_support',
    'identify_by',
    'ignore_183_without_sdp',
    'inband_progress',
    'incoming_mwi_mailbox',
    'language',
    # 'mailboxes',
    'max_audio_streams',
    'max_video_streams',
    'media_address',
    'media_encryption',
    'media_encryption_optimistic',
    'media_use_received_transport',
    'message_context',
    'moh_passthrough',
    'moh_suggest',
    'mwi_from_user',
    'mwi_subscribe_replaces_unsolicited',
    'named_call_group',
    'named_pickup_group',
    'notify_early_inuse_ringing',
    'one_touch_recording',
    'outbound_auth',
    # 'outbound_proxy',
    'permit',
    'pickup_group',
    'preferred_codec_only',
    'record_off_feature',
    'record_on_feature',
    'redirect_method',
    'refer_blind_progress',
    'rewrite_contact',
    'rpid_immediate',
    'rtcp_mux',
    'rtp_engine',
    'rtp_ipv6',
    'rtp_keepalive',
    'rtp_symmetric',
    'rtp_timeout',
    'rtp_timeout_hold',
    'sdp_owner',
    'sdp_session',
    'send_connected_line',
    'send_diversion',
    'send_pai',
    'send_rpid',
    'set_var',
    'srtp_tag_32',
    'sub_min_expiry',
    'subscribe_context',
    'suppress_q850_reason_headers',
    't38_udptl',
    't38_udptl_ec',
    't38_udptl_ipv6',
    't38_udptl_maxdatagram',
    't38_udptl_nat',
    'timers',
    'timers_min_se',
    'timers_sess_expires',
    'tone_zone',
    'tos_audio',
    'tos_video',
    # 'transport',  # Transport is a relation
    'trust_connected_line',
    'trust_id_inbound',
    'trust_id_outbound',
    'use_avpf',
    'use_ptime',
    'user_eq_phone',
    # 'voicemail_extension',
    'webrtc',
]
VALID_REGISTRATION_OPTIONS = [
    'auth_rejection_permanent',
    'forbidden_retry_interval',
    'fatal_retry_interval',
    'max_retries',
    'outbound_proxy',
]

endpoint_sip_tbl = sa.sql.table(
    'endpoint_sip',
    sa.sql.column('uuid'),
    sa.sql.column('label'),
    sa.sql.column('name'),
    sa.sql.column('asterisk_id'),
    sa.sql.column('tenant_uuid'),
    sa.sql.column('transport_uuid'),
    sa.sql.column('template'),
)
endpoint_sip_section_tbl = sa.sql.table(
    'endpoint_sip_section',
    sa.sql.column('uuid'),
    sa.sql.column('type'),
    sa.sql.column('endpoint_sip_uuid'),
)
endpoint_sip_section_option_tbl = sa.sql.table(
    'endpoint_sip_section_option',
    sa.sql.column('uuid'),
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('endpoint_sip_section_uuid'),
)
endpoint_sip_template_tbl = sa.sql.table(
    'endpoint_sip_template',
    sa.sql.column('child_uuid'),
    sa.sql.column('parent_uuid'),
)
linefeatures_tbl = sa.sql.table(
    'linefeatures',
    sa.sql.column('endpoint_sip_id'),
    sa.sql.column('endpoint_sip_uuid'),
)
static_sip_tbl = sa.sql.table(
    'staticsip',
    sa.sql.column('id'),
    sa.sql.column('var_metric'),
    sa.sql.column('commented'),
    sa.sql.column('filename'),
    sa.sql.column('category'),
    sa.sql.column('var_name'),
    sa.sql.column('var_val'),
)
tenant_tbl = sa.sql.table(
    'tenant',
    sa.sql.column('uuid'),
    sa.sql.column('sip_templates_generated'),
    sa.sql.column('global_sip_template_uuid'),
    sa.sql.column('webrtc_sip_template_uuid'),
    sa.sql.column('global_trunk_sip_template_uuid'),
    sa.sql.column('twilio_trunk_sip_template_uuid'),
)
transport_tbl = sa.sql.table(
    'pjsip_transport',
    sa.sql.column('uuid'),
    sa.sql.column('name'),
)
transport_option_tbl = sa.sql.table(
    'pjsip_transport_option',
    sa.sql.column('key'),
    sa.sql.column('value'),
    sa.sql.column('pjsip_transport_uuid'),
)
trunkfeatures_tbl = sa.sql.table(
    'trunkfeatures',
    sa.sql.column('endpoint_sip_id'),
    sa.sql.column('endpoint_sip_uuid'),
    sa.sql.column('twilio_incoming'),
    sa.sql.column('register_sip_id'),
)
user_sip_tbl = sa.sql.table(
    'usersip',
    sa.sql.column('id'),
    sa.sql.column('name'),
    sa.sql.column('type'),
    sa.sql.column('username'),
    sa.sql.column('secret'),
    sa.sql.column('language'),
    sa.sql.column('accountcode'),
    sa.sql.column('amaflags'),
    sa.sql.column('allowtransfer'),
    sa.sql.column('fromuser'),
    sa.sql.column('fromdomain'),
    sa.sql.column('subscribemwi'),
    sa.sql.column('buggymwi'),
    sa.sql.column('call-limit'),
    sa.sql.column('callerid'),
    sa.sql.column('fullname'),
    sa.sql.column('cid_number'),
    sa.sql.column('maxcallbitrate'),
    sa.sql.column('insecure'),
    sa.sql.column('nat'),
    sa.sql.column('promiscredir'),
    sa.sql.column('usereqphone'),
    sa.sql.column('videosupport'),
    sa.sql.column('trustrpid'),
    sa.sql.column('sendrpid'),
    sa.sql.column('allowsubscribe'),
    sa.sql.column('allowoverlap'),
    sa.sql.column('dtmfmode'),
    sa.sql.column('rfc2833compensate'),
    sa.sql.column('qualify'),
    sa.sql.column('g726nonstandard'),
    sa.sql.column('disallow'),
    sa.sql.column('allow'),
    sa.sql.column('autoframing'),
    sa.sql.column('mohinterpret'),
    sa.sql.column('useclientcode'),
    sa.sql.column('progressinband'),
    sa.sql.column('t38pt_udptl'),
    sa.sql.column('t38pt_usertpsource'),
    sa.sql.column('rtptimeout'),
    sa.sql.column('rtpholdtimeout'),
    sa.sql.column('rtpkeepalive'),
    sa.sql.column('deny'),
    sa.sql.column('permit'),
    sa.sql.column('defaultip'),
    sa.sql.column('host'),
    sa.sql.column('port'),
    sa.sql.column('regexten'),
    sa.sql.column('subscribecontext'),
    sa.sql.column('vmexten'),
    sa.sql.column('callingpres'),
    sa.sql.column('parkinglot'),
    sa.sql.column('protocol'),
    sa.sql.column('category'),
    sa.sql.column('outboundproxy'),
    sa.sql.column('transport'),
    sa.sql.column('remotesecret'),
    sa.sql.column('directmedia'),
    sa.sql.column('callcounter'),
    sa.sql.column('busylevel'),
    sa.sql.column('ignoresdpversion'),
    sa.sql.column('session-timers'),
    sa.sql.column('session-expires'),
    sa.sql.column('session-minse'),
    sa.sql.column('session-refresher'),
    sa.sql.column('callbackextension'),
    sa.sql.column('timert1'),
    sa.sql.column('timerb'),
    sa.sql.column('qualifyfreq'),
    sa.sql.column('contactpermit'),
    sa.sql.column('contactdeny'),
    sa.sql.column('unsolicited_mailbox'),
    sa.sql.column('use_q850_reason'),
    sa.sql.column('encryption'),
    sa.sql.column('snom_aoc_enabled'),
    sa.sql.column('maxforwards'),
    sa.sql.column('disallowed_methods'),
    sa.sql.column('textsupport'),
    sa.sql.column('commented'),
    sa.sql.column('options'),
    sa.sql.column('tenant_uuid'),
)


# class heavily inspired from the sip_to_pjsip.py in the Asterisk repository
# https://raw.githubusercontent.com/asterisk/asterisk/master/contrib/scripts/sip_to_pjsip/sip_to_pjsip.py


class Registration(object):
    """
    Class for parsing and storing information in a register line in sip.conf.
    """
    def __init__(self, line, configured_transports):
        self._transport_names = list(configured_transports.keys())

        # Find a "default" transport as a fallback
        for transport_name in self._transport_names:
            # Start with a udp transport
            if 'udp' in transport_name:
                self._transport = transport_name
                break
        else:
            # The first transport as a fallback :(
            self._transport = self._transport_names[0].name

        self.parse(line)

        self.section = 'reg_' + self.user + '@' + self.host
        self.registration_fields = []

        self.auth_section = 'auth_reg_' + self.user + '@' + self.host
        self.auth_fields = []

        self._generate()

    def parse(self, line):
        """
        Initial parsing routine for register lines in sip.conf.

        This splits the line into the part before the host, and the part
        after the '@' symbol. These two parts are then passed to their
        own parsing routines
        """

        # register =>
        # [peer?][transport://]user[@domain][:secret[:authuser]]@host[:port][/extension][~expiry]

        prehost, at, host_part = line.rpartition('@')
        if not prehost:
            raise

        self.parse_host_part(host_part)
        self.parse_user_part(prehost)

    def parse_host_part(self, host_part):
        """
        Parsing routine for the part after the final '@' in a register line.
        The strategy is to use partition calls to peel away the data starting
        from the right and working to the left.
        """
        pre_expiry, sep, expiry = host_part.partition('~')
        pre_extension, sep, self.extension = pre_expiry.partition('/')
        self.host, sep, self.port = pre_extension.partition(':')

        self.expiry = expiry if expiry else '120'

    def parse_user_part(self, user_part):
        """
        Parsing routine for the part before the final '@' in a register line.
        The only mandatory part of this line is the user portion. The strategy
        here is to start by using partition calls to remove everything to
        the right of the user, then finish by using rpartition calls to remove
        everything to the left of the user.
        """
        self.peer = ''
        for transport in self._transport_names:
            begin, _, end = user_part.partition('://')
            self.peer, _, transport = begin.rpartition('?')
            if not transport:
                continue
            if transport not in self._transport_names:
                continue

            self._transport = transport
            user_part = end
            break

        colons = user_part.count(':')
        if (colons == 3):
            # :domainport:secret:authuser
            pre_auth, _, port_auth = user_part.partition(':')
            self.domainport, _, auth = port_auth.partition(':')
            self.secret, _, self.authuser = auth.partition(':')
        elif (colons == 2):
            # :secret:authuser
            pre_auth, _, auth = user_part.partition(':')
            self.secret, _, self.authuser = auth.partition(':')
        elif (colons == 1):
            # :secret
            pre_auth, _, self.secret = user_part.partition(':')
        elif (colons == 0):
            # No port, secret, or authuser
            pre_auth = user_part
        else:
            # Invalid setting
            raise Exception('Invalid SIP register')

        self.user, _, self.domain = pre_auth.partition('@')

    def _generate(self):
        """
        Write parsed registration data into a section in pjsip.conf

        Most of the data in self will get written to a registration section.
        However, there will also need to be an auth section created if a
        secret or authuser is present.

        General mapping of values:
        A combination of self.host and self.port is server_uri
        A combination of self.user, self.domain, and self.domainport is
          client_uri
        self.expiry is expiration
        self.extension is contact_user
        self._transport will map to one of the mapped transports
        self.secret and self.authuser will result in a new auth section, and
          outbound_auth will point to that section.
        XXX self.peer really doesn't map to anything :(
        """

        if self.extension:
            self.registration_fields.append(('contact_user', self.extension))

        self.registration_fields.append(('expiration', self.expiry))
        self.registration_fields.append(('transport', self._transport))

        if hasattr(self, 'secret') and self.secret:
            self.auth_fields.append(('password', self.secret))
            self.auth_fields.append(('username', getattr(self, 'authuser', None) or self.user))
            self.registration_fields.append(('outbound_auth', self.auth_section))

        client_uri = "sip:%s@" % self.user
        if self.domain:
            client_uri += self.domain
        else:
            client_uri += self.host

        if hasattr(self, 'domainport') and self.domainport:
            client_uri += ":" + self.domainport
        elif self.port:
            client_uri += ":" + self.port
        self.registration_fields.append(('client_uri', client_uri))

        server_uri = "sip:%s" % self.host
        if self.port:
            server_uri += ":" + self.port
        self.registration_fields.append(('server_uri', server_uri))


class UserSIP(object):

    twilio_incoming = False
    registration = None

    def __repr__(self):
        return '{}({}, {}, {}, {})'.format(
            self.__class__.__name__,
            self.id,
            self.name,
            self.tenant_uuid,
            self.options,
        )

    @classmethod
    def extract_options(cls, row):
        options = [KV(key, value) for (key, value) in row.options]
        fields = [
            'type',
            'username',
            'secret',
            'language',
            'accountcode',
            'amaflags',
            'allowtransfer',
            'fromuser',
            'fromdomain',
            'subscribemwi',
            'buggymwi',
            'call-limit',
            'callerid',
            'fullname',
            'cid_number',
            'maxcallbitrate',
            'insecure',
            'nat',
            'promiscredir',
            'usereqphone',
            'videosupport',
            'trustrpid',
            'sendrpid',
            'allowsubscribe',
            'allowoverlap',
            'dtmfmode',
            'rfc2833compensate',
            'qualify',
            'g726nonstandard',
            'disallow',
            'allow',
            'autoframing',
            'mohinterpret',
            'useclientcode',
            'progressinband',
            't38pt_udptl',
            't38pt_usertpsource',
            'rtptimeout',
            'rtpholdtimeout',
            'rtpkeepalive',
            'deny',
            'permit',
            'defaultip',
            'host',
            'port',
            'regexten',
            'subscribecontext',
            'vmexten',
            'callingpres',
            'parkinglot',
            'protocol',
            'category',
            'outboundproxy',
            'remotesecret',
            'directmedia',
            'callcounter',
            'busylevel',
            'ignoresdpversion',
            'session-timers',
            'session-expires',
            'session-minse',
            'session-refresher',
            'callbackextension',
            'timert1',
            'timerb',
            'qualifyfreq',
            'contactpermit',
            'contactdeny',
            'unsolicited_mailbox',
            'use_q850_reason',
            'encryption',
            'snom_aoc_enabled',
            'maxforwards',
            'disallowed_methods',
            'textsupport',
        ]
        for field in fields:
            value = getattr(row, field, None)
            if value:
                options.append(KV(field, value))

        return options


class UserSIPTrunk(UserSIP):

    category = 'trunk'

    def __init__(self, id, name, tenant_uuid, options, registration, twilio_incoming):
        self.id = id
        self.name = name
        self.tenant_uuid = tenant_uuid
        self.options = options
        self.registration = registration
        self.twilio_incoming = twilio_incoming

    @classmethod
    def from_row(cls, row, registers, transports):
        options = cls.extract_options(row)
        registration = None
        twilio_incoming = False
        if row.register_sip_id:
            register_url = registers.get(row.register_sip_id)
            if register_url:
                registration = Registration(register_url, transports)
        if row.twilio_incoming:
            twilio_incoming = True
        return cls(row.id, row.name, row.tenant_uuid, options, registration, twilio_incoming)


class UserSIPLine(UserSIP):

    category = 'line'

    def __init__(self, id, name, tenant_uuid, options):
        self.id = id
        self.name = name
        self.tenant_uuid = tenant_uuid
        self.options = options

    @classmethod
    def from_row(cls, row):
        options = cls.extract_options(row)
        return cls(row.id, row.name, row.tenant_uuid, options)


class OptionAccumulator(object):
    def __init__(self, sip_to_pjsip_mapping, valid_options):
        self._sip_to_pjsip = sip_to_pjsip_mapping
        self._valid_options = valid_options
        self._accumulated = []
        self._codecs = []

    def add_option(self, kv):
        conversion_function_name = '_convert_{}'.format(kv.key)
        if hasattr(self, conversion_function_name):
            for name, value in getattr(self, conversion_function_name)(kv.value):
                if name in self._valid_options:
                    self._add_option_no_duplicate(KV(name, value))
        elif kv.key in self._valid_options:
            self._add_option_no_duplicate(kv)
        elif kv.key in self._sip_to_pjsip:
            new_name = self._sip_to_pjsip[kv.key]
            self._add_option_no_duplicate(KV(new_name, kv.value))

    def _add_option_no_duplicate(self, kv):
        if kv in self._accumulated:
            return
        self._accumulated.append(kv)

    def get_options(self):
        options = self._accumulated
        if 'allow' in self._valid_options:
            if not self._codecs:
                options.append(('allow', '!all,ulaw'))
            else:
                options.append(('allow', ','.join(self._codecs)))
        return options

    def _convert_allow(self, val):
        for codec in val.split(','):
            if codec == '!all':
                self._codecs = ['!all']
            else:
                self._codecs.append(codec)
        return
        yield

    def _convert_deny(self, val):
        for codec in val.split(','):
            if codec == 'all':
                self._codecs = ['!all']
            else:
                while codec in self._codecs:
                    self._codecs.remove(codec)
        return
        yield

    @staticmethod
    def _convert_directmedia(val):
        if 'yes' in val:
            yield 'direct_media', 'yes'
        if 'update' in val:
            yield 'direct_media_method', 'update'
        if 'outgoing' in val:
            yield 'direct_media_glare_mitigation', 'outgoing'
        if 'nonat' in val:
            yield 'disable_directed_media_on_nat', 'yes'
        if val == 'no':
            yield 'direct_media', 'no'

    @staticmethod
    def _convert_dtlsenable(val):
        if val == 'yes':
            yield 'media_encryption', 'dtls'

    @staticmethod
    def _convert_dtmfmode(val):
        key = 'dtmf_mode'
        if val == 'rfc2833':
            yield key, 'rfc4733'
        elif val in ('inband', 'info'):
            yield key, val

    @staticmethod
    def _convert_encryption(val):
        if val == 'yes':
            yield 'media_encryption', 'sdes'

    @staticmethod
    def _convert_encryption_taglen(val):
        if val == 32:
            return 'srtp_tag_32', 'yes'

    @staticmethod
    def _convert_nat(val):
        if val == 'yes':
            yield 'rtp_symmetric', 'yes'
            yield 'rewrite_contact', 'yes'
        elif val == 'comedia':
            yield 'rtp_symmetric', 'yes'
        elif val == 'force_rport':
            yield 'force_rport', 'yes'
            yield 'rewrite_contact', 'yes'

    @staticmethod
    def _convert_progressinband(val):
        if val in ('no', 'never'):
            yield 'inband_progress', 'no'
        elif val == 'yes':
            yield 'inband_progress', 'yes'

    @staticmethod
    def _convert_recordonfeature(val):
        if val == 'automixmon':
            yield 'one_touch_recording', 'yes'
        yield 'record_on_feature', val

    @staticmethod
    def _convert_recordofffeature(val):
        if val == 'automixmon':
            yield 'one_touch_recording', 'yes'
        yield 'record_off_feature', val

    @staticmethod
    def _convert_sendrpid(val):
        if val in ('yes', 'rpid'):
            yield 'send_rpid', 'yes'
        elif val == 'pai':
            yield 'send_pai', 'yes'

    @staticmethod
    def _convert_session_timers(val):
        new_val = 'yes'
        if val == 'originate':
            new_val = 'always'
        elif val == 'accept':
            new_val = 'required'
        elif val == 'never':
            new_val = 'no'

        return 'timers', new_val


def get_static_sip():
    query = sa.sql.select([
        static_sip_tbl.c.var_name,
        static_sip_tbl.c.var_val,
    ]).distinct(
        static_sip_tbl.c.var_metric,
        static_sip_tbl.c.var_name,
        static_sip_tbl.c.var_val,
    ).where(sa.sql.and_(
        static_sip_tbl.c.filename == 'sip.conf',
        static_sip_tbl.c.category == 'general',
        static_sip_tbl.c.commented == '0',
        static_sip_tbl.c.var_val.isnot(None),
    )).order_by(
        static_sip_tbl.c.var_metric,
    )
    rows = op.get_bind().execute(query)
    return [KV(row.var_name, row.var_val) for row in rows]


def get_transports():
    query = sa.sql.select([transport_tbl.c.uuid, transport_tbl.c.name])
    rows = op.get_bind().execute(query)
    return {row.name: row.uuid for row in rows}


def get_sip_registers():
    query = sa.sql.select([
        static_sip_tbl.c.id,
        static_sip_tbl.c.var_val,
    ]).where(sa.sql.and_(
        static_sip_tbl.c.filename == 'sip.conf',
        static_sip_tbl.c.category == 'general',
        static_sip_tbl.c.var_name == 'register',
        static_sip_tbl.c.commented == 0,
    ))
    return {row.id: row.var_val for row in op.get_bind().execute(query)}


def find_wss_transport():
    query = sa.sql.select([
        transport_option_tbl.c.pjsip_transport_uuid,
    ]).where(
        sa.sql.and_(
            transport_option_tbl.c.key == 'protocol',
            transport_option_tbl.c.value == 'wss',
        )
    )
    rows = op.get_bind().execute(query)
    for row in rows:
        return row.pjsip_transport_uuid


def list_tenant_uuid():
    query = sa.sql.select([tenant_tbl.c.uuid])
    return [row[0] for row in op.get_bind().execute(query)]


def create_global_config_body(static_sip, transports):
    aor_option_accumulator = OptionAccumulator(
        AOR_SECTION_MAPPING,
        VALID_AOR_OPTIONS,
    )
    endpoint_option_accumulator = OptionAccumulator(
        ENDPOINT_SECTION_MAPPING,
        VALID_ENDPOINT_OPTIONS,
    )
    transport = None

    aor_option_accumulator.add_option(KV('max_contacts', '1'))
    aor_option_accumulator.add_option(KV('remove_existing', 'true'))

    for kv in static_sip:
        aor_option_accumulator.add_option(kv)
        endpoint_option_accumulator.add_option(kv)
        if kv.key == 'transport':
            transport = transports.get(kv.value)

    body = {
        'label': 'General',
        'aor_section_options': aor_option_accumulator.get_options(),
        'endpoint_section_options': endpoint_option_accumulator.get_options(),
        'template': True,
        'transport_uuid': transport,
    }

    return body


def create_webrtc_config_body():
    body = {
        'label': 'WebRTC line',
        'aor_section_options': [
            KV('max_contacts', '10'),
            KV('remove_existing', 'no'),
        ],
        'endpoint_section_options': [
            KV('allow', '!all,opus,g722,alaw,ulaw,vp9,vp8,h264'),
            KV('dtls_auto_generate_cert', 'yes'),
            KV('webrtc', 'yes'),
        ],
        'template': True,
        'transport_uuid': find_wss_transport()
    }

    return body


def create_trunk_config_body(static_sip):
    registration_option_accumulator = OptionAccumulator(
        REGISTRATION_SECTION_MAPPING,
        VALID_REGISTRATION_OPTIONS,
    )

    for kv in static_sip:
        registration_option_accumulator.add_option(kv)

    body = {
        'label': 'Trunk',
        'template': True,
        'registration_section_options': registration_option_accumulator.get_options(),
    }

    return body


def create_twilio_config_body():
    body = {
        'label': 'twilio Trunk',
        'template': True,
        'identify_section_options': [
            KV('match', '54.172.60.0'),
            KV('match', '54.172.60.1'),
            KV('match', '54.172.60.2'),
            KV('match', '54.172.60.3'),
            KV('match', '54.244.51.0'),
            KV('match', '54.244.51.1'),
            KV('match', '54.244.51.2'),
            KV('match', '54.244.51.3'),
            KV('match', '54.171.127.192'),
            KV('match', '54.171.127.193'),
            KV('match', '54.171.127.194'),
            KV('match', '54.171.127.195'),
            KV('match', '35.156.191.128'),
            KV('match', '35.156.191.129'),
            KV('match', '35.156.191.130'),
            KV('match', '35.156.191.131'),
            KV('match', '54.65.63.192'),
            KV('match', '54.65.63.193'),
            KV('match', '54.65.63.194'),
            KV('match', '54.65.63.195'),
            KV('match', '54.169.127.128'),
            KV('match', '54.169.127.129'),
            KV('match', '54.169.127.130'),
            KV('match', '54.169.127.131'),
            KV('match', '54.252.254.64'),
            KV('match', '54.252.254.65'),
            KV('match', '54.252.254.66'),
            KV('match', '54.252.254.67'),
            KV('match', '177.71.206.192'),
            KV('match', '177.71.206.193'),
            KV('match', '177.71.206.194'),
            KV('match', '177.71.206.195'),
        ],
    }

    return body


def insert_section(endpoint_sip_uuid, type, options):
    if not options:
        return

    query = endpoint_sip_section_tbl.insert().returning(endpoint_sip_section_tbl.c.uuid).values(
        endpoint_sip_uuid=endpoint_sip_uuid,
        type=type,
    )
    section_uuid = op.get_bind().execute(query).scalar()

    for key, value in options:
        query = endpoint_sip_section_option_tbl.insert().values(
            key=key,
            value=value,
            endpoint_sip_section_uuid=section_uuid,
        )
        op.execute(query)

    return section_uuid


def insert_endpoint_config(
    tenant_uuid,
    body,
    parents=None,
):
    aor_section_options = body.get('aor_section_options')
    auth_section_options = body.get('auth_section_options')
    endpoint_section_options = body.get('endpoint_section_options')
    identify_section_options = body.get('identify_section_options')
    registration_section_options = body.get('registration_section_options')
    outbound_auth_section_options = body.get('outbound_auth_section_options')
    registration_outbound_auth_section_options = body.get(
        'registration_outbound_auth_section_options'
    )

    query = endpoint_sip_tbl.insert().returning(endpoint_sip_tbl.c.uuid).values(
        label=body['label'],
        name=body.get('name') or generate_unused_name(),
        tenant_uuid=tenant_uuid,
        template=body.get('template', False),
        transport_uuid=body.get('transport_uuid'),
    )
    body['uuid'] = op.get_bind().execute(query).scalar()
    insert_section(body['uuid'], 'aor', aor_section_options)
    insert_section(body['uuid'], 'auth', auth_section_options)
    insert_section(body['uuid'], 'endpoint', endpoint_section_options)
    insert_section(body['uuid'], 'identify', identify_section_options)
    insert_section(body['uuid'], 'registration', registration_section_options)
    insert_section(
        body['uuid'],
        'registration_outbound_auth',
        registration_outbound_auth_section_options,
    )
    insert_section(body['uuid'], 'outbound_auth', outbound_auth_section_options)

    for parent in parents or []:
        query = endpoint_sip_template_tbl.insert().values(
            child_uuid=body['uuid'],
            parent_uuid=parent['uuid'],
        )
        op.execute(query)

    return body


def name_already_exists(name):
    query = (
        sa.sql.select([endpoint_sip_tbl.c.name])
        .where(endpoint_sip_tbl.c.name == name)
    )
    return op.get_bind().execute(query).scalar() is not None


def generate_unused_name():
    while True:
        data = ''.join(random.choice(ALPHANUMERIC_POOL) for _ in range(8))
        if not name_already_exists(data):
            return data


def insert_global_config(tenant_uuid, body):
    body.update({
        'label': 'global',
        'template': True,
    })
    return insert_endpoint_config(tenant_uuid, body)


def insert_webrtc_config(tenant_uuid, parents, body):
    body.update({
        'label': 'webrtc',
        'template': True,
    })
    return insert_endpoint_config(tenant_uuid, body, parents)


def insert_trunk_config(tenant_uuid, parents, body):
    body.update({
        'label': 'global_trunk',
        'template': True,
    })
    return insert_endpoint_config(tenant_uuid, body, parents)


def insert_twilio_config(tenant_uuid, parents, body):
    body.update({
        'label': 'twilio_trunk',
        'template': True,
    })
    return insert_endpoint_config(tenant_uuid, body, parents)


def list_existing_line_config(tenant_uuid):
    query = sa.sql.select([user_sip_tbl]).where(sa.sql.and_(
        user_sip_tbl.c.category == 'user',
        user_sip_tbl.c.commented == 0,
        user_sip_tbl.c.tenant_uuid == tenant_uuid,
    ))
    result = []

    for row in op.get_bind().execute(query):
        result.append(UserSIPLine.from_row(row))

    return result


def list_existing_trunk_config(tenant_uuid, registers, transports):
    query = sa.sql.select([
        user_sip_tbl,
        trunkfeatures_tbl.c.twilio_incoming,
        trunkfeatures_tbl.c.register_sip_id,
    ]).where(sa.sql.and_(
        user_sip_tbl.c.category == 'trunk',
        user_sip_tbl.c.commented == 0,
        user_sip_tbl.c.tenant_uuid == tenant_uuid,
        user_sip_tbl.c.id == trunkfeatures_tbl.c.endpoint_sip_id,
    ))
    result = []
    for row in op.get_bind().execute(query):
        result.append(UserSIPTrunk.from_row(row, registers, transports))
    return result


def convert_host(sip):
    for name, value in sip.options:
        if name == 'host':
            val = value
    else:
        return

    if val == 'dynamic':
        max_contacts = 1
        max_contacts_defined = False

        for key, value in sip.options:
            if key == 'max_contacts':
                max_contacts_defined = True
                max_contacts = value
                break

        if ['webrtc', 'yes'] in sip.options:
            if not max_contacts_defined:
                max_contacts = 10

        if max_contacts == 1:
            yield ('remove_existing', 'yes')

        yield ('max_contacts', max_contacts)
        return

    result = 'sip:'
    # More difficult case. The host will be either a hostname or
    # IP address and may or may not have a port specified. pjsip.conf
    # expects the contact to be a SIP URI.

    if sip.category == 'line':
        user = sip.name
        yield ('qualify_frequency', 0)
    else:
        user = sip.username

    if user:
        result += user + '@'

    port = 5060
    for name, value in sip.options:
        if name == 'port':
            port = value
    host_port = '{}:{}'.format(val, port)
    result += host_port

    yield ('contact', result)


def sip_to_pjsip(sip_config, transports):
    config = {
        'label': sip_config.name,
        'name': sip_config.name,
        'template': False,
    }

    aor_option_accumulator = OptionAccumulator(
        AOR_SECTION_MAPPING,
        VALID_AOR_OPTIONS,
    )
    auth_option_accumulator = OptionAccumulator(
        AUTH_SECTION_MAPPING,
        VALID_AUTH_OPTIONS,
    )
    endpoint_option_accumulator = OptionAccumulator(
        ENDPOINT_SECTION_MAPPING,
        VALID_ENDPOINT_OPTIONS,
    )

    for kv in convert_host(sip_config):
        endpoint_option_accumulator.add_option(kv)

    for kv in sip_config.options:
        aor_option_accumulator.add_option(kv)
        auth_option_accumulator.add_option(kv)
        endpoint_option_accumulator.add_option(kv)
        if kv.key == 'transport':
            config['transport_uuid'] = transports.get(kv.value)

    if sip_config.registration:
        register_section_options = sip_config.registration.registration_fields
        config['register_section_options'] = register_section_options
        config['outbound_auth_section_options'] = sip_config.registration.auth_fields

    config.update({
        'aor_section_options': aor_option_accumulator.get_options(),
        'auth_section_options': auth_option_accumulator.get_options(),
        'endpoint_section_options': endpoint_option_accumulator.get_options(),
    })

    return config


def is_webrtc(pjsip_config):
    endpoint_section_options = pjsip_config.get('endpoint_section_options', [])
    for key, value in endpoint_section_options:
        if key == 'webrtc' and value == 'yes':
            return True
    return False


def is_twilio(pjsip_config):
    return pjsip_config.twilio_incoming is not None


def parent_has_option(parents, section_name, key, value):
    for parent in parents:
        section_options = parent.get(section_name)
        if not section_options:
            continue
        if (key, value) in section_options:
            return True
    return False


def find_inherited_transport(parent_configs):
    last_transport = None
    for config in parent_configs:
        last_transport = config.get('transport_uuid') or last_transport
    return last_transport


def prune_pjsip_config(pjsip_config, parent_configs):
    section_names = [
        'aor_section_options',
        'auth_section_options',
        'endpoint_section_options',
        'identify_section_options',
        'registration_section_options',
        'outbound_auth_section_options',
        'registration_outbound_auth_section_options',
    ]
    for section_name in section_names:
        section_options = pjsip_config.get(section_name)
        if not section_options:
            continue
        to_remove = []
        for key, value in section_options:
            if parent_has_option(parent_configs, section_name, key, value):
                to_remove.append((key, value))

        for pair in to_remove:
            section_options.remove(pair)

    inherited_transport = find_inherited_transport(parent_configs)
    if inherited_transport and inherited_transport == pjsip_config.get('transport_uuid'):
        pjsip_config['transport_uuid'] = None,

    return pjsip_config


def update_line_associations(tenant_uuid, endpoint_uuid, old_sip_id):
    op.execute(
        linefeatures_tbl.update().values(
            endpoint_sip_uuid=endpoint_uuid,
        ).where(linefeatures_tbl.c.endpoint_sip_id == old_sip_id),
    )


def update_trunk_associations(tenant_uuid, endpoint_uuid, old_sip_id):
    op.execute(
        trunkfeatures_tbl.update().values(
            endpoint_sip_uuid=endpoint_uuid,
        ).where(trunkfeatures_tbl.c.endpoint_sip_id == old_sip_id),
    )


def configure_line(tenant_uuid, global_config, webrtc_config, sip_config, transports):
    pjsip_config = sip_to_pjsip(sip_config, transports)
    parent_configs = [global_config]
    if is_webrtc(pjsip_config):
        parent_configs.append(webrtc_config)
    pruned_pjsip_config = prune_pjsip_config(pjsip_config, parent_configs)
    endpoint = insert_endpoint_config(tenant_uuid, pruned_pjsip_config, parent_configs)
    update_line_associations(tenant_uuid, endpoint['uuid'], sip_config.id)


def configure_trunk(tenant_uuid, base_trunk_config, twilio_config, trunk_config, transports):
    pjsip_config = sip_to_pjsip(trunk_config, transports)
    parent_configs = [base_trunk_config]
    if is_twilio(trunk_config):
        parent_configs.append(twilio_config)
    pruned_pjsip_config = prune_pjsip_config(pjsip_config, parent_configs)
    endpoint = insert_endpoint_config(tenant_uuid, pruned_pjsip_config, parent_configs)
    update_trunk_associations(tenant_uuid, endpoint['uuid'], trunk_config.id)


def configure_tenant(
    tenant_uuid,
    global_config_body,
    webrtc_config_body,
    twilio_config_body,
    trunk_config_body,
    transports,
    registers,
):
    global_config = insert_global_config(tenant_uuid, global_config_body)
    webrtc_config = insert_webrtc_config(
        tenant_uuid,
        parents=[global_config],
        body=webrtc_config_body,
    )
    base_trunk_config = insert_trunk_config(
        tenant_uuid,
        parents=[global_config],
        body=trunk_config_body,
    )
    twilio_config = insert_twilio_config(
        tenant_uuid,
        parents=[base_trunk_config],
        body=twilio_config_body,
    )

    op.execute(
        tenant_tbl.update().values(
            sip_templates_generated=True,
            global_sip_template_uuid=global_config['uuid'],
            webrtc_sip_template_uuid=webrtc_config['uuid'],
            global_trunk_sip_template_uuid=base_trunk_config['uuid'],
            twilio_trunk_sip_template_uuid=twilio_config['uuid'],
        ).where(tenant_tbl.c.uuid == tenant_uuid)
    )

    line_configs = list_existing_line_config(tenant_uuid)
    for line_config in line_configs:
        configure_line(tenant_uuid, global_config, webrtc_config, line_config, transports)

    trunk_configs = list_existing_trunk_config(tenant_uuid, registers, transports)
    for trunk_config in trunk_configs:
        configure_trunk(tenant_uuid, base_trunk_config, twilio_config, trunk_config, transports)


def remove_all_sip_endpoints():
    op.execute(endpoint_sip_tbl.delete())


def upgrade():
    tenant_uuids = list_tenant_uuid()
    transports = get_transports()
    static_sip = get_static_sip()
    registers = get_sip_registers()

    global_config_body = create_global_config_body(static_sip, transports)
    webrtc_config_body = create_webrtc_config_body()
    twilio_config_body = create_twilio_config_body()
    trunk_config_body = create_trunk_config_body(static_sip)

    for tenant_uuid in tenant_uuids:
        configure_tenant(
            tenant_uuid,
            global_config_body,
            webrtc_config_body,
            twilio_config_body,
            trunk_config_body,
            transports,
            registers,
        )


def downgrade():
    op.execute(
        tenant_tbl.update().values(
            sip_templates_generated=False,
            global_sip_template_uuid=None,
            webrtc_sip_template_uuid=None,
            global_trunk_sip_template_uuid=None,
            twilio_trunk_sip_template_uuid=None,
        )
    )
    remove_all_sip_endpoints()
