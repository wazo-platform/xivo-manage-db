--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: call_exit_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE call_exit_type AS ENUM (
    'full',
    'closed',
    'joinempty',
    'leaveempty',
    'divert_ca_ratio',
    'divert_waittime',
    'answered',
    'abandoned',
    'timeout'
);


ALTER TYPE public.call_exit_type OWNER TO asterisk;

--
-- Name: callerid_mode; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE callerid_mode AS ENUM (
    'prepend',
    'overwrite',
    'append'
);


ALTER TYPE public.callerid_mode OWNER TO asterisk;

--
-- Name: callerid_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE callerid_type AS ENUM (
    'callfilter',
    'incall',
    'group',
    'queue'
);


ALTER TYPE public.callerid_type OWNER TO asterisk;

--
-- Name: callfilter_bosssecretary; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE callfilter_bosssecretary AS ENUM (
    'bossfirst-serial',
    'bossfirst-simult',
    'secretary-serial',
    'secretary-simult',
    'all'
);


ALTER TYPE public.callfilter_bosssecretary OWNER TO asterisk;

--
-- Name: callfilter_callfrom; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE callfilter_callfrom AS ENUM (
    'internal',
    'external',
    'all'
);


ALTER TYPE public.callfilter_callfrom OWNER TO asterisk;

--
-- Name: callfilter_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE callfilter_type AS ENUM (
    'bosssecretary'
);


ALTER TYPE public.callfilter_type OWNER TO asterisk;

--
-- Name: callfiltermember_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE callfiltermember_type AS ENUM (
    'user'
);


ALTER TYPE public.callfiltermember_type OWNER TO asterisk;

--
-- Name: contextnumbers_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE contextnumbers_type AS ENUM (
    'user',
    'group',
    'queue',
    'meetme',
    'incall'
);


ALTER TYPE public.contextnumbers_type OWNER TO asterisk;

--
-- Name: dialaction_action; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE dialaction_action AS ENUM (
    'none',
    'endcall:busy',
    'endcall:congestion',
    'endcall:hangup',
    'user',
    'group',
    'queue',
    'meetme',
    'voicemail',
    'trunk',
    'schedule',
    'voicemenu',
    'extension',
    'outcall',
    'application:callbackdisa',
    'application:disa',
    'application:directory',
    'application:faxtomail',
    'application:voicemailmain',
    'application:password',
    'sound',
    'custom'
);


ALTER TYPE public.dialaction_action OWNER TO asterisk;

--
-- Name: dialaction_category; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE dialaction_category AS ENUM (
    'callfilter',
    'group',
    'incall',
    'queue',
    'schedule',
    'user',
    'outcall'
);


ALTER TYPE public.dialaction_category OWNER TO asterisk;

--
-- Name: dialaction_event; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE dialaction_event AS ENUM (
    'answer',
    'noanswer',
    'congestion',
    'busy',
    'chanunavail',
    'inschedule',
    'outschedule',
    'qwaittime',
    'qwaitratio'
);


ALTER TYPE public.dialaction_event OWNER TO asterisk;

--
-- Name: extenumbers_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE extenumbers_type AS ENUM (
    'extenfeatures',
    'featuremap',
    'generalfeatures',
    'group',
    'incall',
    'meetme',
    'outcall',
    'queue',
    'user',
    'voicemenu'
);


ALTER TYPE public.extenumbers_type OWNER TO asterisk;

--
-- Name: generic_bsfilter; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE generic_bsfilter AS ENUM (
    'no',
    'boss',
    'secretary'
);


ALTER TYPE public.generic_bsfilter OWNER TO asterisk;

--
-- Name: ldapfilter_additionaltype; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE ldapfilter_additionaltype AS ENUM (
    'office',
    'home',
    'mobile',
    'fax',
    'other',
    'custom'
);


ALTER TYPE public.ldapfilter_additionaltype OWNER TO asterisk;

--
-- Name: ldapserver_protocolversion; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE ldapserver_protocolversion AS ENUM (
    '2',
    '3'
);


ALTER TYPE public.ldapserver_protocolversion OWNER TO asterisk;

--
-- Name: ldapserver_securitylayer; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE ldapserver_securitylayer AS ENUM (
    'tls',
    'ssl'
);


ALTER TYPE public.ldapserver_securitylayer OWNER TO asterisk;

--
-- Name: meetmefeatures_admin_identification; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE meetmefeatures_admin_identification AS ENUM (
    'calleridnum',
    'pin',
    'all'
);


ALTER TYPE public.meetmefeatures_admin_identification OWNER TO asterisk;

--
-- Name: meetmefeatures_admin_typefrom; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE meetmefeatures_admin_typefrom AS ENUM (
    'none',
    'internal',
    'external',
    'undefined'
);


ALTER TYPE public.meetmefeatures_admin_typefrom OWNER TO asterisk;

--
-- Name: meetmefeatures_announcejoinleave; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE meetmefeatures_announcejoinleave AS ENUM (
    'no',
    'yes',
    'noreview'
);


ALTER TYPE public.meetmefeatures_announcejoinleave OWNER TO asterisk;

--
-- Name: meetmefeatures_mode; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE meetmefeatures_mode AS ENUM (
    'listen',
    'talk',
    'all'
);


ALTER TYPE public.meetmefeatures_mode OWNER TO asterisk;

--
-- Name: netiface_family; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE netiface_family AS ENUM (
    'inet',
    'inet6'
);


ALTER TYPE public.netiface_family OWNER TO asterisk;

--
-- Name: netiface_method; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE netiface_method AS ENUM (
    'static',
    'dhcp',
    'manual'
);


ALTER TYPE public.netiface_method OWNER TO asterisk;

--
-- Name: netiface_networktype; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE netiface_networktype AS ENUM (
    'data',
    'voip'
);


ALTER TYPE public.netiface_networktype OWNER TO asterisk;

--
-- Name: netiface_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE netiface_type AS ENUM (
    'iface'
);


ALTER TYPE public.netiface_type OWNER TO asterisk;

--
-- Name: phonebook_title; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE phonebook_title AS ENUM (
    'mr',
    'mrs',
    'ms'
);


ALTER TYPE public.phonebook_title OWNER TO asterisk;

--
-- Name: phonebookaddress_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE phonebookaddress_type AS ENUM (
    'home',
    'office',
    'other'
);


ALTER TYPE public.phonebookaddress_type OWNER TO asterisk;

--
-- Name: phonebooknumber_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE phonebooknumber_type AS ENUM (
    'home',
    'office',
    'mobile',
    'fax',
    'other'
);


ALTER TYPE public.phonebooknumber_type OWNER TO asterisk;

--
-- Name: phonefunckey_typeextenumbers; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE phonefunckey_typeextenumbers AS ENUM (
    'extenfeatures',
    'featuremap',
    'generalfeatures'
);


ALTER TYPE public.phonefunckey_typeextenumbers OWNER TO asterisk;

--
-- Name: phonefunckey_typeextenumbersright; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE phonefunckey_typeextenumbersright AS ENUM (
    'agent',
    'group',
    'meetme',
    'queue',
    'user',
    'paging'
);


ALTER TYPE public.phonefunckey_typeextenumbersright OWNER TO asterisk;

--
-- Name: pickup_category; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE pickup_category AS ENUM (
    'member',
    'pickup'
);


ALTER TYPE public.pickup_category OWNER TO asterisk;

--
-- Name: pickup_membertype; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE pickup_membertype AS ENUM (
    'group',
    'queue',
    'user'
);


ALTER TYPE public.pickup_membertype OWNER TO asterisk;

--
-- Name: queue_category; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE queue_category AS ENUM (
    'group',
    'queue'
);


ALTER TYPE public.queue_category OWNER TO asterisk;

--
-- Name: queue_monitor_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE queue_monitor_type AS ENUM (
    'no',
    'mixmonitor'
);


ALTER TYPE public.queue_monitor_type OWNER TO asterisk;

--
-- Name: queue_statistics; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE queue_statistics AS (
	received_call_count bigint,
	answered_call_count bigint,
	answered_call_in_qos_count bigint,
	abandonned_call_count bigint,
	received_and_done bigint,
	max_hold_time integer,
	mean_hold_time integer
);


ALTER TYPE public.queue_statistics OWNER TO asterisk;

--
-- Name: queuemember_usertype; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE queuemember_usertype AS ENUM (
    'agent',
    'user'
);


ALTER TYPE public.queuemember_usertype OWNER TO asterisk;

--
-- Name: queuepenaltychange_sign; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE queuepenaltychange_sign AS ENUM (
    '=',
    '+',
    '-'
);


ALTER TYPE public.queuepenaltychange_sign OWNER TO asterisk;

--
-- Name: rightcallmember_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE rightcallmember_type AS ENUM (
    'user',
    'group',
    'incall',
    'outcall'
);


ALTER TYPE public.rightcallmember_type OWNER TO asterisk;

--
-- Name: schedule_path_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE schedule_path_type AS ENUM (
    'user',
    'group',
    'queue',
    'incall',
    'outcall',
    'voicemenu'
);


ALTER TYPE public.schedule_path_type OWNER TO asterisk;

--
-- Name: schedule_time_mode; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE schedule_time_mode AS ENUM (
    'opened',
    'closed'
);


ALTER TYPE public.schedule_time_mode OWNER TO asterisk;

--
-- Name: serverfeatures_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE serverfeatures_type AS ENUM (
    'xivo',
    'ldap'
);


ALTER TYPE public.serverfeatures_type OWNER TO asterisk;

--
-- Name: sipauthentication_secretmode; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE sipauthentication_secretmode AS ENUM (
    'md5',
    'clear'
);


ALTER TYPE public.sipauthentication_secretmode OWNER TO asterisk;

--
-- Name: trunk_protocol; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE trunk_protocol AS ENUM (
    'sip',
    'iax',
    'sccp',
    'custom'
);


ALTER TYPE public.trunk_protocol OWNER TO asterisk;

--
-- Name: user_meta; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE user_meta AS ENUM (
    'user',
    'admin',
    'root'
);


ALTER TYPE public.user_meta OWNER TO asterisk;

--
-- Name: usercustom_category; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usercustom_category AS ENUM (
    'user',
    'trunk'
);


ALTER TYPE public.usercustom_category OWNER TO asterisk;

--
-- Name: userfeatures_voicemailtype; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE userfeatures_voicemailtype AS ENUM (
    'asterisk',
    'exchange'
);


ALTER TYPE public.userfeatures_voicemailtype OWNER TO asterisk;

--
-- Name: useriax_amaflags; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_amaflags AS ENUM (
    'default',
    'omit',
    'billing',
    'documentation'
);


ALTER TYPE public.useriax_amaflags OWNER TO asterisk;

--
-- Name: useriax_auth; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_auth AS ENUM (
    'plaintext',
    'md5',
    'rsa',
    'plaintext,md5',
    'plaintext,rsa',
    'md5,rsa',
    'plaintext,md5,rsa'
);


ALTER TYPE public.useriax_auth OWNER TO asterisk;

--
-- Name: useriax_category; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_category AS ENUM (
    'user',
    'trunk'
);


ALTER TYPE public.useriax_category OWNER TO asterisk;

--
-- Name: useriax_codecpriority; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_codecpriority AS ENUM (
    'disabled',
    'host',
    'caller',
    'reqonly'
);


ALTER TYPE public.useriax_codecpriority OWNER TO asterisk;

--
-- Name: useriax_encryption; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_encryption AS ENUM (
    'no',
    'yes',
    'aes128'
);


ALTER TYPE public.useriax_encryption OWNER TO asterisk;

--
-- Name: useriax_protocol; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_protocol AS ENUM (
    'iax'
);


ALTER TYPE public.useriax_protocol OWNER TO asterisk;

--
-- Name: useriax_transfer; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_transfer AS ENUM (
    'no',
    'yes',
    'mediaonly'
);


ALTER TYPE public.useriax_transfer OWNER TO asterisk;

--
-- Name: useriax_type; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE useriax_type AS ENUM (
    'friend',
    'peer',
    'user'
);


ALTER TYPE public.useriax_type OWNER TO asterisk;

--
-- Name: usersip_directmedia; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_directmedia AS ENUM (
    'no',
    'yes',
    'nonat',
    'update',
    'update,nonat'
);


ALTER TYPE public.usersip_directmedia OWNER TO asterisk;

--
-- Name: usersip_dtmfmode; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_dtmfmode AS ENUM (
    'rfc2833',
    'inband',
    'info',
    'auto'
);


ALTER TYPE public.usersip_dtmfmode OWNER TO asterisk;

--
-- Name: usersip_insecure; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_insecure AS ENUM (
    'port',
    'invite',
    'port,invite'
);


ALTER TYPE public.usersip_insecure OWNER TO asterisk;

--
-- Name: usersip_nat; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_nat AS ENUM (
    'no',
    'force_rport',
    'comedia',
    'force_rport,comedia'
);


ALTER TYPE public.usersip_nat OWNER TO asterisk;

--
-- Name: usersip_progressinband; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_progressinband AS ENUM (
    'no',
    'yes',
    'never'
);


ALTER TYPE public.usersip_progressinband OWNER TO asterisk;

--
-- Name: usersip_protocol; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_protocol AS ENUM (
    'sip'
);


ALTER TYPE public.usersip_protocol OWNER TO asterisk;

--
-- Name: usersip_session_refresher; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_session_refresher AS ENUM (
    'uac',
    'uas'
);


ALTER TYPE public.usersip_session_refresher OWNER TO asterisk;

--
-- Name: usersip_session_timers; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_session_timers AS ENUM (
    'originate',
    'accept',
    'refuse'
);


ALTER TYPE public.usersip_session_timers OWNER TO asterisk;

--
-- Name: usersip_videosupport; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE usersip_videosupport AS ENUM (
    'no',
    'yes',
    'always'
);


ALTER TYPE public.usersip_videosupport OWNER TO asterisk;

--
-- Name: voicemail_hidefromdir; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE voicemail_hidefromdir AS ENUM (
    'no',
    'yes'
);


ALTER TYPE public.voicemail_hidefromdir OWNER TO asterisk;

--
-- Name: voicemail_passwordlocation; Type: TYPE; Schema: public; Owner: asterisk
--

CREATE TYPE voicemail_passwordlocation AS ENUM (
    'spooldir',
    'voicemail'
);


ALTER TYPE public.voicemail_passwordlocation OWNER TO asterisk;

--
-- Name: fill_answered_calls(text, text); Type: FUNCTION; Schema: public; Owner: asterisk
--

CREATE FUNCTION fill_answered_calls(period_start text, period_end text) RETURNS void
    LANGUAGE sql
    AS $_$
  INSERT INTO stat_call_on_queue (callid, "time", talktime, waittime, queue_id, agent_id, status)
  SELECT
    outer_queue_log.callid,
    CAST ((SELECT "time"
           FROM queue_log
           WHERE callid=outer_queue_log.callid AND
                 queuename=outer_queue_log.queuename AND
                 event='ENTERQUEUE' ORDER BY "time" DESC LIMIT 1) AS TIMESTAMP) AS "time",
    CASE WHEN event IN ('COMPLETEAGENT', 'COMPLETECALLER') THEN CAST (data2 AS INTEGER)
         WHEN event = 'TRANSFER' THEN CAST (data4 AS INTEGER) END as talktime,
    CASE WHEN event IN ('COMPLETEAGENT', 'COMPLETECALLER') THEN CAST (data1 AS INTEGER)
         WHEN event = 'TRANSFER' THEN CAST (data3 AS INTEGER) END as waittime,
    stat_queue.id AS queue_id,
    stat_agent.id AS agent_id,
    'answered' AS status
  FROM
    queue_log as outer_queue_log
  LEFT JOIN
    stat_agent ON outer_queue_log.agent = stat_agent.name
  LEFT JOIN
    stat_queue ON outer_queue_log.queuename = stat_queue.name
  WHERE
    callid IN
      (SELECT callid
       FROM queue_log
       WHERE event = 'ENTERQUEUE' AND "time" BETWEEN $1 AND $2)
    AND event IN ('COMPLETEAGENT', 'COMPLETECALLER', 'TRANSFER');
$_$;


ALTER FUNCTION public.fill_answered_calls(period_start text, period_end text) OWNER TO asterisk;

--
-- Name: fill_leaveempty_calls(text, text); Type: FUNCTION; Schema: public; Owner: asterisk
--

CREATE FUNCTION fill_leaveempty_calls(period_start text, period_end text) RETURNS void
    LANGUAGE sql
    AS $_$
INSERT INTO stat_call_on_queue (callid, time, waittime, queue_id, status)
SELECT
  callid,
  enter_time as time,
  EXTRACT(EPOCH FROM (leave_time - enter_time))::INTEGER as waittime,
  queue_id,
  'leaveempty' AS status
FROM (SELECT
        CAST (time AS TIMESTAMP) AS enter_time,
        (select CAST (time AS TIMESTAMP) from queue_log where callid=main.callid AND event='LEAVEEMPTY' LIMIT 1) AS leave_time,
        callid,
        (SELECT id FROM stat_queue WHERE name=queuename) AS queue_id
      FROM queue_log AS main
      WHERE callid IN (SELECT callid FROM queue_log WHERE event = 'LEAVEEMPTY')
            AND event = 'ENTERQUEUE'
            AND time BETWEEN $1 AND $2) AS first;
$_$;


ALTER FUNCTION public.fill_leaveempty_calls(period_start text, period_end text) OWNER TO asterisk;

--
-- Name: fill_simple_calls(text, text); Type: FUNCTION; Schema: public; Owner: asterisk
--

CREATE FUNCTION fill_simple_calls(period_start text, period_end text) RETURNS void
    LANGUAGE sql
    AS $_$
  INSERT INTO "stat_call_on_queue" (callid, "time", queue_id, status)
    SELECT
      callid,
      CAST ("time" AS TIMESTAMP) as "time",
      (SELECT id FROM stat_queue WHERE name=queuename) as queue_id,
      CASE WHEN event = 'FULL' THEN 'full'::call_exit_type
           WHEN event = 'DIVERT_CA_RATIO' THEN 'divert_ca_ratio'
           WHEN event = 'DIVERT_HOLDTIME' THEN 'divert_waittime'
           WHEN event = 'CLOSED' THEN 'closed'
           WHEN event = 'JOINEMPTY' THEN 'joinempty'
      END as status
    FROM queue_log
    WHERE event IN ('FULL', 'DIVERT_CA_RATIO', 'DIVERT_HOLDTIME', 'CLOSED', 'JOINEMPTY') AND
          "time" BETWEEN $1 AND $2;
$_$;


ALTER FUNCTION public.fill_simple_calls(period_start text, period_end text) OWNER TO asterisk;

--
-- Name: get_queue_statistics(text, integer, integer); Type: FUNCTION; Schema: public; Owner: asterisk
--

CREATE FUNCTION get_queue_statistics(queue_name text, in_window integer, xqos integer) RETURNS queue_statistics
    LANGUAGE sql
    AS $_$
    SELECT
        -- received_call_count
        count(*),
        -- answered_call_count
        count(case when call_picker <> '' then 1 end),
        -- answered_call_in_qos_count
        count(case when call_picker <> '' and hold_time < $3 then 1 end),
        -- abandonned_call_count
        count(case when hold_time is not null and (call_picker = '' or call_picker is null) then 1 end),
        -- received_and_done
        count(hold_time),
        -- max_hold_time
        max(hold_time),
         -- mean_hold_time
        cast (round(avg(hold_time)) as int)
    FROM
        queue_info
    WHERE
        queue_name = $1 and call_time_t > $2;
$_$;


ALTER FUNCTION public.get_queue_statistics(queue_name text, in_window integer, xqos integer) OWNER TO asterisk;

--
-- Name: set_agent_on_pauseall(); Type: FUNCTION; Schema: public; Owner: asterisk
--

CREATE FUNCTION set_agent_on_pauseall() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
    "number" text;
BEGIN
    SELECT "agent_number" INTO "number" FROM "agent_login_status" WHERE "interface" = NEW."agent";
    IF FOUND THEN
        NEW."agent" := 'Agent/' || "number";
    END IF;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.set_agent_on_pauseall() OWNER TO asterisk;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accessfeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE accessfeatures (
    id integer NOT NULL,
    host character varying(255) DEFAULT ''::character varying NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    feature character varying(64) DEFAULT 'phonebook'::character varying NOT NULL,
    CONSTRAINT accessfeatures_feature_check CHECK (((feature)::text = 'phonebook'::text))
);


ALTER TABLE public.accessfeatures OWNER TO asterisk;

--
-- Name: accessfeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE accessfeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accessfeatures_id_seq OWNER TO asterisk;

--
-- Name: accessfeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE accessfeatures_id_seq OWNED BY accessfeatures.id;


--
-- Name: accesswebservice; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE accesswebservice (
    id integer NOT NULL,
    name character varying(64) DEFAULT ''::character varying NOT NULL,
    login character varying(64),
    passwd character varying(64),
    host character varying(255),
    obj text NOT NULL,
    disable integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.accesswebservice OWNER TO asterisk;

--
-- Name: accesswebservice_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE accesswebservice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accesswebservice_id_seq OWNER TO asterisk;

--
-- Name: accesswebservice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE accesswebservice_id_seq OWNED BY accesswebservice.id;


--
-- Name: agent_login_status; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE agent_login_status (
    agent_id integer NOT NULL,
    login_at timestamp without time zone DEFAULT now() NOT NULL,
    extension character varying(80) NOT NULL,
    context character varying(80) NOT NULL,
    interface character varying(128) NOT NULL,
    state_interface character varying(128) NOT NULL,
    agent_number character varying(40) NOT NULL
);


ALTER TABLE public.agent_login_status OWNER TO asterisk;

--
-- Name: agent_membership_status; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE agent_membership_status (
    agent_id integer NOT NULL,
    queue_id integer NOT NULL,
    queue_name character varying(128) NOT NULL,
    penalty integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.agent_membership_status OWNER TO asterisk;

--
-- Name: agentfeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE agentfeatures (
    id integer NOT NULL,
    numgroup integer NOT NULL,
    firstname character varying(128) DEFAULT ''::character varying NOT NULL,
    lastname character varying(128) DEFAULT ''::character varying NOT NULL,
    number character varying(40) NOT NULL,
    passwd character varying(128) NOT NULL,
    context character varying(39) NOT NULL,
    language character varying(20) NOT NULL,
    autologoff integer,
    "group" character varying(255),
    description text NOT NULL,
    preprocess_subroutine character varying(40)
);


ALTER TABLE public.agentfeatures OWNER TO asterisk;

--
-- Name: agentfeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE agentfeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.agentfeatures_id_seq OWNER TO asterisk;

--
-- Name: agentfeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE agentfeatures_id_seq OWNED BY agentfeatures.id;


--
-- Name: agentglobalparams; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE agentglobalparams (
    id integer NOT NULL,
    category character varying(128) NOT NULL,
    option_name character varying(255) NOT NULL,
    option_value character varying(255)
);


ALTER TABLE public.agentglobalparams OWNER TO asterisk;

--
-- Name: agentglobalparams_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE agentglobalparams_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.agentglobalparams_id_seq OWNER TO asterisk;

--
-- Name: agentglobalparams_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE agentglobalparams_id_seq OWNED BY agentglobalparams.id;


--
-- Name: agentgroup; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE agentgroup (
    id integer NOT NULL,
    groupid integer NOT NULL,
    name character varying(128) DEFAULT ''::character varying NOT NULL,
    groups character varying(255) DEFAULT ''::character varying NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    deleted integer DEFAULT 0 NOT NULL,
    description text
);


ALTER TABLE public.agentgroup OWNER TO asterisk;

--
-- Name: agentgroup_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE agentgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.agentgroup_id_seq OWNER TO asterisk;

--
-- Name: agentgroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE agentgroup_id_seq OWNED BY agentgroup.id;


--
-- Name: agentqueueskill; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE agentqueueskill (
    agentid integer NOT NULL,
    skillid integer NOT NULL,
    weight integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.agentqueueskill OWNER TO asterisk;

--
-- Name: attachment; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE attachment (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    object_type character varying(16) NOT NULL,
    object_id integer NOT NULL,
    file bytea,
    size integer NOT NULL,
    mime character varying(64) NOT NULL
);


ALTER TABLE public.attachment OWNER TO asterisk;

--
-- Name: attachment_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE attachment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attachment_id_seq OWNER TO asterisk;

--
-- Name: attachment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE attachment_id_seq OWNED BY attachment.id;


--
-- Name: call_log; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE call_log (
    id integer NOT NULL,
    date timestamp without time zone NOT NULL,
    source_name character varying(255),
    source_exten character varying(255),
    destination_name character varying(255),
    destination_exten character varying(255),
    duration interval NOT NULL,
    user_field character varying(255),
    answered boolean,
    source_line_identity character varying(255),
    destination_line_identity character varying(255)
);


ALTER TABLE public.call_log OWNER TO asterisk;

--
-- Name: call_log_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE call_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.call_log_id_seq OWNER TO asterisk;

--
-- Name: call_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE call_log_id_seq OWNED BY call_log.id;


--
-- Name: callerid; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE callerid (
    mode callerid_mode,
    callerdisplay character varying(80) DEFAULT ''::character varying NOT NULL,
    type callerid_type NOT NULL,
    typeval integer NOT NULL
);


ALTER TABLE public.callerid OWNER TO asterisk;

--
-- Name: callfilter; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE callfilter (
    id integer NOT NULL,
    name character varying(128) DEFAULT ''::character varying NOT NULL,
    type callfilter_type NOT NULL,
    bosssecretary callfilter_bosssecretary,
    callfrom callfilter_callfrom,
    ringseconds integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.callfilter OWNER TO asterisk;

--
-- Name: callfilter_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE callfilter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.callfilter_id_seq OWNER TO asterisk;

--
-- Name: callfilter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE callfilter_id_seq OWNED BY callfilter.id;


--
-- Name: callfiltermember; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE callfiltermember (
    id integer NOT NULL,
    callfilterid integer DEFAULT 0 NOT NULL,
    type callfiltermember_type NOT NULL,
    typeval character varying(128) DEFAULT '0'::character varying NOT NULL,
    ringseconds integer DEFAULT 0 NOT NULL,
    priority integer DEFAULT 0 NOT NULL,
    bstype generic_bsfilter NOT NULL,
    active integer DEFAULT 0 NOT NULL,
    CONSTRAINT callfiltermember_bstype_check CHECK ((bstype = ANY (ARRAY['boss'::generic_bsfilter, 'secretary'::generic_bsfilter])))
);


ALTER TABLE public.callfiltermember OWNER TO asterisk;

--
-- Name: callfiltermember_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE callfiltermember_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.callfiltermember_id_seq OWNER TO asterisk;

--
-- Name: callfiltermember_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE callfiltermember_id_seq OWNED BY callfiltermember.id;


--
-- Name: cel; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cel (
    id integer NOT NULL,
    eventtype character varying(30) NOT NULL,
    eventtime timestamp without time zone NOT NULL,
    userdeftype character varying(255) NOT NULL,
    cid_name character varying(80) NOT NULL,
    cid_num character varying(80) NOT NULL,
    cid_ani character varying(80) NOT NULL,
    cid_rdnis character varying(80) NOT NULL,
    cid_dnid character varying(80) NOT NULL,
    exten character varying(80) NOT NULL,
    context character varying(80) NOT NULL,
    channame character varying(80) NOT NULL,
    appname character varying(80) NOT NULL,
    appdata character varying(512) NOT NULL,
    amaflags integer NOT NULL,
    accountcode character varying(20) NOT NULL,
    peeraccount character varying(20) NOT NULL,
    uniqueid character varying(150) NOT NULL,
    linkedid character varying(150) NOT NULL,
    userfield character varying(255) NOT NULL,
    peer character varying(80) NOT NULL,
    call_log_id integer
);


ALTER TABLE public.cel OWNER TO asterisk;

--
-- Name: cel_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE cel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cel_id_seq OWNER TO asterisk;

--
-- Name: cel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE cel_id_seq OWNED BY cel.id;


--
-- Name: context; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE context (
    name character varying(39) NOT NULL,
    displayname character varying(128) DEFAULT ''::character varying NOT NULL,
    entity character varying(64),
    contexttype character varying(40) DEFAULT 'internal'::character varying NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.context OWNER TO asterisk;

--
-- Name: contextinclude; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE contextinclude (
    context character varying(39) NOT NULL,
    include character varying(39) NOT NULL,
    priority integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.contextinclude OWNER TO asterisk;

--
-- Name: contextmember; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE contextmember (
    context character varying(39) NOT NULL,
    type character varying(32) NOT NULL,
    typeval character varying(128) DEFAULT ''::character varying NOT NULL,
    varname character varying(128) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.contextmember OWNER TO asterisk;

--
-- Name: contextnumbers; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE contextnumbers (
    context character varying(39) NOT NULL,
    type contextnumbers_type NOT NULL,
    numberbeg character varying(16) DEFAULT ''::character varying NOT NULL,
    numberend character varying(16) DEFAULT ''::character varying NOT NULL,
    didlength integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.contextnumbers OWNER TO asterisk;

--
-- Name: contexttype; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE contexttype (
    id integer NOT NULL,
    name character varying(40) NOT NULL,
    commented integer,
    deletable integer,
    description text
);


ALTER TABLE public.contexttype OWNER TO asterisk;

--
-- Name: contexttype_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE contexttype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contexttype_id_seq OWNER TO asterisk;

--
-- Name: contexttype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE contexttype_id_seq OWNED BY contexttype.id;


--
-- Name: cti_preference; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_preference (
    id integer NOT NULL,
    option character varying(255) NOT NULL
);


ALTER TABLE public.cti_preference OWNER TO asterisk;

--
-- Name: cti_preference_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE cti_preference_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cti_preference_id_seq OWNER TO asterisk;

--
-- Name: cti_preference_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE cti_preference_id_seq OWNED BY cti_preference.id;


--
-- Name: cti_profile; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_profile (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    presence_id integer,
    phonehints_id integer
);


ALTER TABLE public.cti_profile OWNER TO asterisk;

--
-- Name: cti_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE cti_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cti_profile_id_seq OWNER TO asterisk;

--
-- Name: cti_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE cti_profile_id_seq OWNED BY cti_profile.id;


--
-- Name: cti_profile_preference; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_profile_preference (
    profile_id integer NOT NULL,
    preference_id integer NOT NULL,
    value character varying(255)
);


ALTER TABLE public.cti_profile_preference OWNER TO asterisk;

--
-- Name: cti_profile_service; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_profile_service (
    profile_id integer NOT NULL,
    service_id integer NOT NULL
);


ALTER TABLE public.cti_profile_service OWNER TO asterisk;

--
-- Name: cti_profile_xlet; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_profile_xlet (
    xlet_id integer NOT NULL,
    profile_id integer NOT NULL,
    layout_id integer,
    closable boolean DEFAULT true,
    movable boolean DEFAULT true,
    floating boolean DEFAULT true,
    scrollable boolean DEFAULT true,
    "order" integer
);


ALTER TABLE public.cti_profile_xlet OWNER TO asterisk;

--
-- Name: cti_service; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_service (
    id integer NOT NULL,
    key character varying(255) NOT NULL
);


ALTER TABLE public.cti_service OWNER TO asterisk;

--
-- Name: cti_service_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE cti_service_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cti_service_id_seq OWNER TO asterisk;

--
-- Name: cti_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE cti_service_id_seq OWNED BY cti_service.id;


--
-- Name: cti_xlet; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_xlet (
    id integer NOT NULL,
    plugin_name character varying(40) NOT NULL
);


ALTER TABLE public.cti_xlet OWNER TO asterisk;

--
-- Name: cti_xlet_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE cti_xlet_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cti_xlet_id_seq OWNER TO asterisk;

--
-- Name: cti_xlet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE cti_xlet_id_seq OWNED BY cti_xlet.id;


--
-- Name: cti_xlet_layout; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cti_xlet_layout (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.cti_xlet_layout OWNER TO asterisk;

--
-- Name: cti_xlet_layout_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE cti_xlet_layout_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cti_xlet_layout_id_seq OWNER TO asterisk;

--
-- Name: cti_xlet_layout_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE cti_xlet_layout_id_seq OWNED BY cti_xlet_layout.id;


--
-- Name: cticontexts; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE cticontexts (
    id integer NOT NULL,
    name character varying(50),
    directories text NOT NULL,
    display text NOT NULL,
    description text,
    deletable integer
);


ALTER TABLE public.cticontexts OWNER TO asterisk;

--
-- Name: cticontexts_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE cticontexts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cticontexts_id_seq OWNER TO asterisk;

--
-- Name: cticontexts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE cticontexts_id_seq OWNED BY cticontexts.id;


--
-- Name: ctidirectories; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctidirectories (
    id integer NOT NULL,
    name character varying(255),
    uri character varying(255),
    delimiter character varying(20),
    match_direct text NOT NULL,
    match_reverse text NOT NULL,
    description character varying(255),
    deletable integer
);


ALTER TABLE public.ctidirectories OWNER TO asterisk;

--
-- Name: ctidirectories_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctidirectories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctidirectories_id_seq OWNER TO asterisk;

--
-- Name: ctidirectories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctidirectories_id_seq OWNED BY ctidirectories.id;


--
-- Name: ctidirectoryfields; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctidirectoryfields (
    dir_id integer NOT NULL,
    fieldname character varying(255) NOT NULL,
    value character varying(255)
);


ALTER TABLE public.ctidirectoryfields OWNER TO asterisk;

--
-- Name: ctidisplays; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctidisplays (
    id integer NOT NULL,
    name character varying(50),
    data text NOT NULL,
    deletable integer,
    description text
);


ALTER TABLE public.ctidisplays OWNER TO asterisk;

--
-- Name: ctidisplays_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctidisplays_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctidisplays_id_seq OWNER TO asterisk;

--
-- Name: ctidisplays_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctidisplays_id_seq OWNED BY ctidisplays.id;


--
-- Name: ctilog; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctilog (
    id integer NOT NULL,
    eventdate timestamp without time zone,
    loginclient character varying(64),
    company character varying(64),
    status character varying(64),
    action character varying(64),
    arguments character varying(255),
    callduration integer
);


ALTER TABLE public.ctilog OWNER TO asterisk;

--
-- Name: ctilog_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctilog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctilog_id_seq OWNER TO asterisk;

--
-- Name: ctilog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctilog_id_seq OWNED BY ctilog.id;


--
-- Name: ctimain; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctimain (
    id integer NOT NULL,
    commandset character varying(20),
    ami_ip character varying(16),
    ami_port integer,
    ami_login character varying(64),
    ami_password character varying(64),
    cti_ip character varying(16),
    cti_port integer,
    cti_active integer DEFAULT 1 NOT NULL,
    ctis_ip character varying(16),
    ctis_port integer,
    ctis_active integer DEFAULT 1 NOT NULL,
    webi_ip character varying(16),
    webi_port integer,
    webi_active integer DEFAULT 1 NOT NULL,
    info_ip character varying(16),
    info_port integer,
    info_active integer DEFAULT 1 NOT NULL,
    tlscertfile character varying(128),
    tlsprivkeyfile character varying(128),
    socket_timeout integer,
    login_timeout integer,
    context_separation integer,
    live_reload_conf integer
);


ALTER TABLE public.ctimain OWNER TO asterisk;

--
-- Name: ctimain_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctimain_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctimain_id_seq OWNER TO asterisk;

--
-- Name: ctimain_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctimain_id_seq OWNED BY ctimain.id;


--
-- Name: ctiphonehints; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctiphonehints (
    id integer NOT NULL,
    idgroup integer,
    number character varying(8),
    name character varying(255),
    color character varying(128)
);


ALTER TABLE public.ctiphonehints OWNER TO asterisk;

--
-- Name: ctiphonehints_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctiphonehints_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctiphonehints_id_seq OWNER TO asterisk;

--
-- Name: ctiphonehints_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctiphonehints_id_seq OWNED BY ctiphonehints.id;


--
-- Name: ctiphonehintsgroup; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctiphonehintsgroup (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description character varying(255),
    deletable integer
);


ALTER TABLE public.ctiphonehintsgroup OWNER TO asterisk;

--
-- Name: ctiphonehintsgroup_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctiphonehintsgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctiphonehintsgroup_id_seq OWNER TO asterisk;

--
-- Name: ctiphonehintsgroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctiphonehintsgroup_id_seq OWNED BY ctiphonehintsgroup.id;


--
-- Name: ctipresences; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctipresences (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    description character varying(255),
    deletable integer
);


ALTER TABLE public.ctipresences OWNER TO asterisk;

--
-- Name: ctipresences_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctipresences_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctipresences_id_seq OWNER TO asterisk;

--
-- Name: ctipresences_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctipresences_id_seq OWNED BY ctipresences.id;


--
-- Name: ctireversedirectories; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctireversedirectories (
    id integer NOT NULL,
    directories text NOT NULL
);


ALTER TABLE public.ctireversedirectories OWNER TO asterisk;

--
-- Name: ctireversedirectories_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctireversedirectories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctireversedirectories_id_seq OWNER TO asterisk;

--
-- Name: ctireversedirectories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctireversedirectories_id_seq OWNED BY ctireversedirectories.id;


--
-- Name: ctisheetactions; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctisheetactions (
    id integer NOT NULL,
    name character varying(50),
    description text NOT NULL,
    whom character varying(50),
    sheet_info text,
    systray_info text,
    sheet_qtui text,
    action_info text,
    focus integer,
    deletable integer,
    disable integer
);


ALTER TABLE public.ctisheetactions OWNER TO asterisk;

--
-- Name: ctisheetactions_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctisheetactions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctisheetactions_id_seq OWNER TO asterisk;

--
-- Name: ctisheetactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctisheetactions_id_seq OWNED BY ctisheetactions.id;


--
-- Name: ctisheetevents; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctisheetevents (
    id integer NOT NULL,
    incomingdid character varying(50),
    dial character varying(50),
    link character varying(50),
    unlink character varying(50),
    hangup character varying(50)
);


ALTER TABLE public.ctisheetevents OWNER TO asterisk;

--
-- Name: ctisheetevents_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctisheetevents_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctisheetevents_id_seq OWNER TO asterisk;

--
-- Name: ctisheetevents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctisheetevents_id_seq OWNED BY ctisheetevents.id;


--
-- Name: ctistatus; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ctistatus (
    id integer NOT NULL,
    presence_id integer,
    name character varying(255) NOT NULL,
    display_name character varying(255),
    actions character varying(255),
    color character varying(20),
    access_status character varying(255),
    deletable integer
);


ALTER TABLE public.ctistatus OWNER TO asterisk;

--
-- Name: ctistatus_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ctistatus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ctistatus_id_seq OWNER TO asterisk;

--
-- Name: ctistatus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ctistatus_id_seq OWNED BY ctistatus.id;


--
-- Name: dhcp; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE dhcp (
    id integer NOT NULL,
    active integer DEFAULT 0 NOT NULL,
    pool_start character varying(64) DEFAULT ''::character varying NOT NULL,
    pool_end character varying(64) DEFAULT ''::character varying NOT NULL,
    extra_ifaces character varying(255) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.dhcp OWNER TO asterisk;

--
-- Name: dhcp_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE dhcp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dhcp_id_seq OWNER TO asterisk;

--
-- Name: dhcp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE dhcp_id_seq OWNED BY dhcp.id;


--
-- Name: dialaction; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE dialaction (
    category dialaction_category NOT NULL,
    categoryval character varying(128) DEFAULT ''::character varying NOT NULL,
    action dialaction_action NOT NULL,
    actionarg1 character varying(255),
    actionarg2 character varying(255),
    linked integer DEFAULT 0 NOT NULL,
    event dialaction_event NOT NULL
);


ALTER TABLE public.dialaction OWNER TO asterisk;

--
-- Name: dialpattern; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE dialpattern (
    id integer NOT NULL,
    type character varying(32) NOT NULL,
    typeid integer NOT NULL,
    externprefix character varying(64),
    prefix character varying(32),
    exten character varying(40) NOT NULL,
    stripnum integer,
    callerid character varying(80)
);


ALTER TABLE public.dialpattern OWNER TO asterisk;

--
-- Name: dialpattern_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE dialpattern_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dialpattern_id_seq OWNER TO asterisk;

--
-- Name: dialpattern_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE dialpattern_id_seq OWNED BY dialpattern.id;


--
-- Name: directories; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE directories (
    id integer NOT NULL,
    uri character varying(255),
    dirtype character varying(20),
    name character varying(255),
    tablename character varying(255),
    description text NOT NULL
);


ALTER TABLE public.directories OWNER TO asterisk;

--
-- Name: directories_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE directories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directories_id_seq OWNER TO asterisk;

--
-- Name: directories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE directories_id_seq OWNED BY directories.id;


--
-- Name: entity; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE entity (
    id integer NOT NULL,
    name character varying(64) DEFAULT ''::character varying NOT NULL,
    displayname character varying(128) DEFAULT ''::character varying NOT NULL,
    phonenumber character varying(40) DEFAULT ''::character varying NOT NULL,
    faxnumber character varying(40) DEFAULT ''::character varying NOT NULL,
    email character varying(255) DEFAULT ''::character varying NOT NULL,
    url character varying(255) DEFAULT ''::character varying NOT NULL,
    address1 character varying(30) DEFAULT ''::character varying NOT NULL,
    address2 character varying(30) DEFAULT ''::character varying NOT NULL,
    city character varying(128) DEFAULT ''::character varying NOT NULL,
    state character varying(128) DEFAULT ''::character varying NOT NULL,
    zipcode character varying(16) DEFAULT ''::character varying NOT NULL,
    country character varying(3) DEFAULT ''::character varying NOT NULL,
    disable integer DEFAULT 0 NOT NULL,
    dcreate integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.entity OWNER TO asterisk;

--
-- Name: entity_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE entity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.entity_id_seq OWNER TO asterisk;

--
-- Name: entity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE entity_id_seq OWNED BY entity.id;


--
-- Name: extensions; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE extensions (
    id integer NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    context character varying(39) DEFAULT ''::character varying NOT NULL,
    exten character varying(40) DEFAULT ''::character varying NOT NULL,
    type extenumbers_type NOT NULL,
    typeval character varying(255) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.extensions OWNER TO asterisk;

--
-- Name: extensions_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE extensions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.extensions_id_seq OWNER TO asterisk;

--
-- Name: extensions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE extensions_id_seq OWNED BY extensions.id;


--
-- Name: features; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE features (
    id integer NOT NULL,
    cat_metric integer DEFAULT 0 NOT NULL,
    var_metric integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    filename character varying(128) NOT NULL,
    category character varying(128) NOT NULL,
    var_name character varying(128) NOT NULL,
    var_val character varying(255)
);


ALTER TABLE public.features OWNER TO asterisk;

--
-- Name: features_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE features_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.features_id_seq OWNER TO asterisk;

--
-- Name: features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE features_id_seq OWNED BY features.id;


--
-- Name: func_key; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key (
    id integer NOT NULL,
    type_id integer NOT NULL,
    destination_type_id integer NOT NULL
);


ALTER TABLE public.func_key OWNER TO asterisk;

--
-- Name: func_key_dest_conference; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_dest_conference (
    func_key_id integer NOT NULL,
    destination_type_id integer DEFAULT 4 NOT NULL,
    conference_id integer NOT NULL,
    CONSTRAINT func_key_dest_conference_destination_type_id_check CHECK ((destination_type_id = 4))
);


ALTER TABLE public.func_key_dest_conference OWNER TO asterisk;

--
-- Name: func_key_dest_group; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_dest_group (
    func_key_id integer NOT NULL,
    destination_type_id integer DEFAULT 2 NOT NULL,
    group_id integer NOT NULL,
    CONSTRAINT func_key_dest_group_destination_type_id_check CHECK ((destination_type_id = 2))
);


ALTER TABLE public.func_key_dest_group OWNER TO asterisk;

--
-- Name: func_key_dest_queue; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_dest_queue (
    func_key_id integer NOT NULL,
    destination_type_id integer DEFAULT 3 NOT NULL,
    queue_id integer NOT NULL,
    CONSTRAINT func_key_dest_queue_destination_type_id_check CHECK ((destination_type_id = 3))
);


ALTER TABLE public.func_key_dest_queue OWNER TO asterisk;

--
-- Name: func_key_dest_user; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_dest_user (
    func_key_id integer NOT NULL,
    user_id integer NOT NULL,
    destination_type_id integer DEFAULT 1 NOT NULL,
    CONSTRAINT func_key_dest_user_destination_type_id_check CHECK ((destination_type_id = 1))
);


ALTER TABLE public.func_key_dest_user OWNER TO asterisk;

--
-- Name: func_key_destination_type; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_destination_type (
    id integer NOT NULL,
    name character varying(128) NOT NULL
);


ALTER TABLE public.func_key_destination_type OWNER TO asterisk;

--
-- Name: func_key_destination_type_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE func_key_destination_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.func_key_destination_type_id_seq OWNER TO asterisk;

--
-- Name: func_key_destination_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE func_key_destination_type_id_seq OWNED BY func_key_destination_type.id;


--
-- Name: func_key_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE func_key_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.func_key_id_seq OWNER TO asterisk;

--
-- Name: func_key_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE func_key_id_seq OWNED BY func_key.id;


--
-- Name: func_key_mapping; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_mapping (
    template_id integer NOT NULL,
    func_key_id integer NOT NULL,
    destination_type_id integer NOT NULL,
    label character varying(128),
    "position" integer NOT NULL,
    blf boolean DEFAULT false NOT NULL,
    CONSTRAINT func_key_mapping_position_check CHECK (("position" > 0))
);


ALTER TABLE public.func_key_mapping OWNER TO asterisk;

--
-- Name: func_key_template; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_template (
    id integer NOT NULL,
    name character varying(128),
    private boolean DEFAULT false NOT NULL
);


ALTER TABLE public.func_key_template OWNER TO asterisk;

--
-- Name: func_key_template_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE func_key_template_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.func_key_template_id_seq OWNER TO asterisk;

--
-- Name: func_key_template_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE func_key_template_id_seq OWNED BY func_key_template.id;


--
-- Name: func_key_type; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE func_key_type (
    id integer NOT NULL,
    name character varying(128) NOT NULL
);


ALTER TABLE public.func_key_type OWNER TO asterisk;

--
-- Name: func_key_type_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE func_key_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.func_key_type_id_seq OWNER TO asterisk;

--
-- Name: func_key_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE func_key_type_id_seq OWNED BY func_key_type.id;


--
-- Name: general; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE general (
    id integer NOT NULL,
    timezone character varying(128),
    exchange_trunkid integer,
    exchange_exten character varying(128),
    dundi integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.general OWNER TO asterisk;

--
-- Name: general_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE general_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.general_id_seq OWNER TO asterisk;

--
-- Name: general_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE general_id_seq OWNED BY general.id;


--
-- Name: groupfeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE groupfeatures (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    number character varying(40) DEFAULT ''::character varying NOT NULL,
    context character varying(39) NOT NULL,
    transfer_user integer DEFAULT 0 NOT NULL,
    transfer_call integer DEFAULT 0 NOT NULL,
    write_caller integer DEFAULT 0 NOT NULL,
    write_calling integer DEFAULT 0 NOT NULL,
    timeout integer DEFAULT 0 NOT NULL,
    preprocess_subroutine character varying(39),
    deleted integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.groupfeatures OWNER TO asterisk;

--
-- Name: groupfeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE groupfeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.groupfeatures_id_seq OWNER TO asterisk;

--
-- Name: groupfeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE groupfeatures_id_seq OWNED BY groupfeatures.id;


--
-- Name: iaxcallnumberlimits; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE iaxcallnumberlimits (
    id integer NOT NULL,
    destination character varying(39) NOT NULL,
    netmask character varying(39) NOT NULL,
    calllimits integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.iaxcallnumberlimits OWNER TO asterisk;

--
-- Name: iaxcallnumberlimits_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE iaxcallnumberlimits_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.iaxcallnumberlimits_id_seq OWNER TO asterisk;

--
-- Name: iaxcallnumberlimits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE iaxcallnumberlimits_id_seq OWNED BY iaxcallnumberlimits.id;


--
-- Name: incall; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE incall (
    id integer NOT NULL,
    exten character varying(40) NOT NULL,
    context character varying(39) NOT NULL,
    preprocess_subroutine character varying(39),
    commented integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.incall OWNER TO asterisk;

--
-- Name: incall_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE incall_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.incall_id_seq OWNER TO asterisk;

--
-- Name: incall_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE incall_id_seq OWNED BY incall.id;


--
-- Name: ldapfilter; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ldapfilter (
    id integer NOT NULL,
    ldapserverid integer NOT NULL,
    name character varying(128) DEFAULT ''::character varying NOT NULL,
    "user" character varying(255),
    passwd character varying(255),
    basedn character varying(255) DEFAULT ''::character varying NOT NULL,
    filter character varying(255) DEFAULT ''::character varying NOT NULL,
    attrdisplayname character varying(255) DEFAULT ''::character varying NOT NULL,
    attrphonenumber character varying(255) DEFAULT ''::character varying NOT NULL,
    additionaltype ldapfilter_additionaltype NOT NULL,
    additionaltext character varying(16) DEFAULT ''::character varying NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.ldapfilter OWNER TO asterisk;

--
-- Name: ldapfilter_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ldapfilter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ldapfilter_id_seq OWNER TO asterisk;

--
-- Name: ldapfilter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ldapfilter_id_seq OWNED BY ldapfilter.id;


--
-- Name: ldapserver; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE ldapserver (
    id integer NOT NULL,
    name character varying(64) DEFAULT ''::character varying NOT NULL,
    host character varying(255) DEFAULT ''::character varying NOT NULL,
    port integer NOT NULL,
    securitylayer ldapserver_securitylayer,
    protocolversion ldapserver_protocolversion DEFAULT '3'::ldapserver_protocolversion NOT NULL,
    disable integer DEFAULT 0 NOT NULL,
    dcreate integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.ldapserver OWNER TO asterisk;

--
-- Name: ldapserver_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE ldapserver_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ldapserver_id_seq OWNER TO asterisk;

--
-- Name: ldapserver_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE ldapserver_id_seq OWNED BY ldapserver.id;


--
-- Name: linefeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE linefeatures (
    id integer NOT NULL,
    protocolid integer NOT NULL,
    device character varying(32),
    configregistrar character varying(128),
    name character varying(128) NOT NULL,
    number character varying(40),
    context character varying(39) NOT NULL,
    provisioningid integer NOT NULL,
    num integer DEFAULT 0,
    ipfrom character varying(15),
    commented integer DEFAULT 0 NOT NULL,
    description text,
    protocol trunk_protocol NOT NULL
);


ALTER TABLE public.linefeatures OWNER TO asterisk;

--
-- Name: linefeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE linefeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.linefeatures_id_seq OWNER TO asterisk;

--
-- Name: linefeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE linefeatures_id_seq OWNED BY linefeatures.id;


--
-- Name: mail; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE mail (
    id integer NOT NULL,
    mydomain character varying(255) DEFAULT '0'::character varying NOT NULL,
    origin character varying(255) DEFAULT 'xivo-clients.proformatique.com'::character varying NOT NULL,
    relayhost character varying(255),
    fallback_relayhost character varying(255),
    canonical text NOT NULL
);


ALTER TABLE public.mail OWNER TO asterisk;

--
-- Name: mail_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE mail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mail_id_seq OWNER TO asterisk;

--
-- Name: mail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE mail_id_seq OWNED BY mail.id;


--
-- Name: meetmefeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE meetmefeatures (
    id integer NOT NULL,
    meetmeid integer NOT NULL,
    name character varying(80) NOT NULL,
    confno character varying(40) NOT NULL,
    context character varying(39) NOT NULL,
    admin_typefrom meetmefeatures_admin_typefrom,
    admin_internalid integer,
    admin_externalid character varying(40),
    admin_identification meetmefeatures_admin_identification NOT NULL,
    admin_mode meetmefeatures_mode NOT NULL,
    admin_announceusercount integer DEFAULT 0 NOT NULL,
    admin_announcejoinleave meetmefeatures_announcejoinleave NOT NULL,
    admin_moderationmode integer DEFAULT 0 NOT NULL,
    admin_initiallymuted integer DEFAULT 0 NOT NULL,
    admin_musiconhold character varying(128),
    admin_poundexit integer DEFAULT 0 NOT NULL,
    admin_quiet integer DEFAULT 0 NOT NULL,
    admin_starmenu integer DEFAULT 0 NOT NULL,
    admin_closeconflastmarkedexit integer DEFAULT 0 NOT NULL,
    admin_enableexitcontext integer DEFAULT 0 NOT NULL,
    admin_exitcontext character varying(39),
    user_mode meetmefeatures_mode NOT NULL,
    user_announceusercount integer DEFAULT 0 NOT NULL,
    user_hiddencalls integer DEFAULT 0 NOT NULL,
    user_announcejoinleave meetmefeatures_announcejoinleave NOT NULL,
    user_initiallymuted integer DEFAULT 0 NOT NULL,
    user_musiconhold character varying(128),
    user_poundexit integer DEFAULT 0 NOT NULL,
    user_quiet integer DEFAULT 0 NOT NULL,
    user_starmenu integer DEFAULT 0 NOT NULL,
    user_enableexitcontext integer DEFAULT 0 NOT NULL,
    user_exitcontext character varying(39),
    talkeroptimization integer DEFAULT 0 NOT NULL,
    record integer DEFAULT 0 NOT NULL,
    talkerdetection integer DEFAULT 0 NOT NULL,
    noplaymsgfirstenter integer DEFAULT 0 NOT NULL,
    durationm integer,
    closeconfdurationexceeded integer DEFAULT 0 NOT NULL,
    nbuserstartdeductduration integer,
    timeannounceclose integer,
    maxusers integer DEFAULT 0 NOT NULL,
    startdate integer,
    emailfrom character varying(255),
    emailfromname character varying(255),
    emailsubject character varying(255),
    emailbody text NOT NULL,
    preprocess_subroutine character varying(39),
    description text NOT NULL,
    commented integer DEFAULT 0
);


ALTER TABLE public.meetmefeatures OWNER TO asterisk;

--
-- Name: meetmefeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE meetmefeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meetmefeatures_id_seq OWNER TO asterisk;

--
-- Name: meetmefeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE meetmefeatures_id_seq OWNED BY meetmefeatures.id;


--
-- Name: meetmeguest; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE meetmeguest (
    id integer NOT NULL,
    meetmefeaturesid integer NOT NULL,
    fullname character varying(255) NOT NULL,
    telephonenumber character varying(40),
    email character varying(320)
);


ALTER TABLE public.meetmeguest OWNER TO asterisk;

--
-- Name: meetmeguest_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE meetmeguest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meetmeguest_id_seq OWNER TO asterisk;

--
-- Name: meetmeguest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE meetmeguest_id_seq OWNED BY meetmeguest.id;


--
-- Name: monitoring; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE monitoring (
    id integer NOT NULL,
    maintenance integer DEFAULT 0 NOT NULL,
    alert_emails character varying(4096),
    dahdi_monitor_ports character varying(255),
    max_call_duration integer
);


ALTER TABLE public.monitoring OWNER TO asterisk;

--
-- Name: monitoring_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE monitoring_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.monitoring_id_seq OWNER TO asterisk;

--
-- Name: monitoring_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE monitoring_id_seq OWNED BY monitoring.id;


--
-- Name: musiconhold; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE musiconhold (
    id integer NOT NULL,
    cat_metric integer DEFAULT 0 NOT NULL,
    var_metric integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    filename character varying(128) NOT NULL,
    category character varying(128) NOT NULL,
    var_name character varying(128) NOT NULL,
    var_val character varying(128)
);


ALTER TABLE public.musiconhold OWNER TO asterisk;

--
-- Name: musiconhold_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE musiconhold_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.musiconhold_id_seq OWNER TO asterisk;

--
-- Name: musiconhold_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE musiconhold_id_seq OWNED BY musiconhold.id;


--
-- Name: netiface; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE netiface (
    id integer NOT NULL,
    ifname character varying(64) DEFAULT ''::character varying NOT NULL,
    hwtypeid integer DEFAULT 65534 NOT NULL,
    networktype netiface_networktype NOT NULL,
    type netiface_type NOT NULL,
    family netiface_family NOT NULL,
    address character varying(39),
    netmask character varying(39),
    broadcast character varying(15),
    gateway character varying(39),
    mtu integer,
    vlanrawdevice character varying(64),
    vlanid integer,
    options text NOT NULL,
    disable integer DEFAULT 0 NOT NULL,
    dcreate integer DEFAULT 0 NOT NULL,
    description text,
    method netiface_method
);


ALTER TABLE public.netiface OWNER TO asterisk;

--
-- Name: netiface_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE netiface_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.netiface_id_seq OWNER TO asterisk;

--
-- Name: netiface_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE netiface_id_seq OWNED BY netiface.id;


--
-- Name: outcall; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE outcall (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    context character varying(39) NOT NULL,
    useenum integer DEFAULT 0 NOT NULL,
    internal integer DEFAULT 0 NOT NULL,
    preprocess_subroutine character varying(39),
    hangupringtime integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text
);


ALTER TABLE public.outcall OWNER TO asterisk;

--
-- Name: outcall_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE outcall_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.outcall_id_seq OWNER TO asterisk;

--
-- Name: outcall_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE outcall_id_seq OWNED BY outcall.id;


--
-- Name: outcalltrunk; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE outcalltrunk (
    outcallid integer DEFAULT 0 NOT NULL,
    trunkfeaturesid integer DEFAULT 0 NOT NULL,
    priority integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.outcalltrunk OWNER TO asterisk;

--
-- Name: paging; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE paging (
    id integer NOT NULL,
    number character varying(32),
    duplex integer DEFAULT 0 NOT NULL,
    ignore integer DEFAULT 0 NOT NULL,
    record integer DEFAULT 0 NOT NULL,
    quiet integer DEFAULT 0 NOT NULL,
    timeout integer NOT NULL,
    announcement_file character varying(64),
    announcement_play integer DEFAULT 0 NOT NULL,
    announcement_caller integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text
);


ALTER TABLE public.paging OWNER TO asterisk;

--
-- Name: paging_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE paging_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paging_id_seq OWNER TO asterisk;

--
-- Name: paging_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE paging_id_seq OWNED BY paging.id;


--
-- Name: paginguser; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE paginguser (
    pagingid integer NOT NULL,
    userfeaturesid integer NOT NULL,
    caller integer NOT NULL
);


ALTER TABLE public.paginguser OWNER TO asterisk;

--
-- Name: phonebook; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE phonebook (
    id integer NOT NULL,
    title phonebook_title NOT NULL,
    firstname character varying(128) DEFAULT ''::character varying NOT NULL,
    lastname character varying(128) DEFAULT ''::character varying NOT NULL,
    displayname character varying(64) DEFAULT ''::character varying NOT NULL,
    society character varying(128) DEFAULT ''::character varying NOT NULL,
    email character varying(255) DEFAULT ''::character varying NOT NULL,
    url character varying(255) DEFAULT ''::character varying NOT NULL,
    image bytea,
    description text NOT NULL
);


ALTER TABLE public.phonebook OWNER TO asterisk;

--
-- Name: phonebook_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE phonebook_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.phonebook_id_seq OWNER TO asterisk;

--
-- Name: phonebook_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE phonebook_id_seq OWNED BY phonebook.id;


--
-- Name: phonebookaddress; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE phonebookaddress (
    id integer NOT NULL,
    phonebookid integer NOT NULL,
    address1 character varying(30) DEFAULT ''::character varying NOT NULL,
    address2 character varying(30) DEFAULT ''::character varying NOT NULL,
    city character varying(128) DEFAULT ''::character varying NOT NULL,
    state character varying(128) DEFAULT ''::character varying NOT NULL,
    zipcode character varying(16) DEFAULT ''::character varying NOT NULL,
    country character varying(3) DEFAULT ''::character varying NOT NULL,
    type phonebookaddress_type NOT NULL
);


ALTER TABLE public.phonebookaddress OWNER TO asterisk;

--
-- Name: phonebookaddress_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE phonebookaddress_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.phonebookaddress_id_seq OWNER TO asterisk;

--
-- Name: phonebookaddress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE phonebookaddress_id_seq OWNED BY phonebookaddress.id;


--
-- Name: phonebooknumber; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE phonebooknumber (
    id integer NOT NULL,
    phonebookid integer NOT NULL,
    number character varying(40) DEFAULT ''::character varying NOT NULL,
    type phonebooknumber_type NOT NULL
);


ALTER TABLE public.phonebooknumber OWNER TO asterisk;

--
-- Name: phonebooknumber_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE phonebooknumber_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.phonebooknumber_id_seq OWNER TO asterisk;

--
-- Name: phonebooknumber_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE phonebooknumber_id_seq OWNED BY phonebooknumber.id;


--
-- Name: phonefunckey; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE phonefunckey (
    iduserfeatures integer NOT NULL,
    fknum integer NOT NULL,
    exten character varying(40),
    typeextenumbers phonefunckey_typeextenumbers,
    typevalextenumbers character varying(255),
    typevalextenumbersright character varying(255),
    label character varying(32),
    supervision integer DEFAULT 0 NOT NULL,
    progfunckey integer DEFAULT 0 NOT NULL,
    typeextenumbersright phonefunckey_typeextenumbersright
);


ALTER TABLE public.phonefunckey OWNER TO asterisk;

--
-- Name: pickup; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE pickup (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text
);


ALTER TABLE public.pickup OWNER TO asterisk;

--
-- Name: pickupmember; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE pickupmember (
    pickupid integer NOT NULL,
    category pickup_category NOT NULL,
    membertype pickup_membertype NOT NULL,
    memberid integer NOT NULL
);


ALTER TABLE public.pickupmember OWNER TO asterisk;

--
-- Name: provisioning; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE provisioning (
    id integer NOT NULL,
    net4_ip character varying(39) NOT NULL,
    net4_ip_rest character varying(39) NOT NULL,
    username character varying(32) NOT NULL,
    password character varying(32) NOT NULL,
    dhcp_integration integer DEFAULT 0 NOT NULL,
    rest_port integer NOT NULL,
    http_port integer NOT NULL,
    private integer DEFAULT 0 NOT NULL,
    secure integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.provisioning OWNER TO asterisk;

--
-- Name: provisioning_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE provisioning_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.provisioning_id_seq OWNER TO asterisk;

--
-- Name: provisioning_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE provisioning_id_seq OWNED BY provisioning.id;


--
-- Name: queue; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queue (
    name character varying(128) NOT NULL,
    musicclass character varying(128),
    announce character varying(128),
    context character varying(39),
    timeout integer DEFAULT 0,
    "monitor-type" queue_monitor_type,
    "monitor-format" character varying(128),
    "queue-youarenext" character varying(128),
    "queue-thereare" character varying(128),
    "queue-callswaiting" character varying(128),
    "queue-holdtime" character varying(128),
    "queue-minutes" character varying(128),
    "queue-seconds" character varying(128),
    "queue-thankyou" character varying(128),
    "queue-reporthold" character varying(128),
    "periodic-announce" text,
    "announce-frequency" integer,
    "periodic-announce-frequency" integer,
    "announce-round-seconds" integer,
    "announce-holdtime" character varying(4),
    retry integer,
    wrapuptime integer,
    maxlen integer,
    servicelevel integer,
    strategy character varying(11),
    joinempty character varying(255),
    leavewhenempty character varying(255),
    eventmemberstatus integer DEFAULT 0 NOT NULL,
    eventwhencalled integer DEFAULT 0 NOT NULL,
    ringinuse integer DEFAULT 0 NOT NULL,
    reportholdtime integer DEFAULT 0 NOT NULL,
    memberdelay integer,
    weight integer,
    timeoutrestart integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    category queue_category NOT NULL,
    timeoutpriority character varying(10) DEFAULT 'app'::character varying NOT NULL,
    autofill integer DEFAULT 1 NOT NULL,
    autopause integer DEFAULT 1 NOT NULL,
    setinterfacevar integer DEFAULT 0 NOT NULL,
    setqueueentryvar integer DEFAULT 0 NOT NULL,
    setqueuevar integer DEFAULT 0 NOT NULL,
    membermacro character varying(1024),
    "min-announce-frequency" integer DEFAULT 60 NOT NULL,
    "random-periodic-announce" integer DEFAULT 0 NOT NULL,
    "announce-position" character varying(1024) DEFAULT 'yes'::character varying NOT NULL,
    "announce-position-limit" integer DEFAULT 5 NOT NULL,
    defaultrule character varying(1024)
);


ALTER TABLE public.queue OWNER TO asterisk;

--
-- Name: queue_info; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queue_info (
    id integer NOT NULL,
    call_time_t integer,
    queue_name character varying(128) DEFAULT ''::character varying NOT NULL,
    caller character varying(80) DEFAULT ''::character varying NOT NULL,
    caller_uniqueid character varying(32) DEFAULT ''::character varying NOT NULL,
    call_picker character varying(80),
    hold_time integer,
    talk_time integer
);


ALTER TABLE public.queue_info OWNER TO asterisk;

--
-- Name: queue_info_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE queue_info_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queue_info_id_seq OWNER TO asterisk;

--
-- Name: queue_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE queue_info_id_seq OWNED BY queue_info.id;


--
-- Name: queue_log; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queue_log (
    "time" character varying(26) DEFAULT ''::character varying NOT NULL,
    callid character varying(32) DEFAULT ''::character varying NOT NULL,
    queuename character varying(50) DEFAULT ''::character varying NOT NULL,
    agent character varying(50) DEFAULT ''::character varying NOT NULL,
    event character varying(20) DEFAULT ''::character varying NOT NULL,
    data1 character varying(30) DEFAULT ''::character varying,
    data2 character varying(30) DEFAULT ''::character varying,
    data3 character varying(30) DEFAULT ''::character varying,
    data4 character varying(30) DEFAULT ''::character varying,
    data5 character varying(30) DEFAULT ''::character varying,
    id integer NOT NULL
);


ALTER TABLE public.queue_log OWNER TO asterisk;

--
-- Name: queue_log_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE queue_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queue_log_id_seq OWNER TO asterisk;

--
-- Name: queue_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE queue_log_id_seq OWNED BY queue_log.id;


--
-- Name: queuefeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queuefeatures (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    displayname character varying(128) NOT NULL,
    number character varying(40) DEFAULT ''::character varying NOT NULL,
    context character varying(39),
    data_quality integer DEFAULT 0 NOT NULL,
    hitting_callee integer DEFAULT 0 NOT NULL,
    hitting_caller integer DEFAULT 0 NOT NULL,
    retries integer DEFAULT 0 NOT NULL,
    ring integer DEFAULT 0 NOT NULL,
    transfer_user integer DEFAULT 0 NOT NULL,
    transfer_call integer DEFAULT 0 NOT NULL,
    write_caller integer DEFAULT 0 NOT NULL,
    write_calling integer DEFAULT 0 NOT NULL,
    url character varying(255) DEFAULT ''::character varying NOT NULL,
    announceoverride character varying(128) DEFAULT ''::character varying NOT NULL,
    timeout integer DEFAULT 0 NOT NULL,
    preprocess_subroutine character varying(39),
    announce_holdtime integer DEFAULT 0 NOT NULL,
    waittime integer,
    waitratio double precision
);


ALTER TABLE public.queuefeatures OWNER TO asterisk;

--
-- Name: queuefeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE queuefeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queuefeatures_id_seq OWNER TO asterisk;

--
-- Name: queuefeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE queuefeatures_id_seq OWNED BY queuefeatures.id;


--
-- Name: queuemember; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queuemember (
    queue_name character varying(128) NOT NULL,
    interface character varying(128) NOT NULL,
    penalty integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    usertype queuemember_usertype NOT NULL,
    userid integer NOT NULL,
    channel character varying(25) NOT NULL,
    category queue_category NOT NULL,
    "position" integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.queuemember OWNER TO asterisk;

--
-- Name: queuepenalty; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queuepenalty (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.queuepenalty OWNER TO asterisk;

--
-- Name: queuepenalty_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE queuepenalty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queuepenalty_id_seq OWNER TO asterisk;

--
-- Name: queuepenalty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE queuepenalty_id_seq OWNED BY queuepenalty.id;


--
-- Name: queuepenaltychange; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queuepenaltychange (
    queuepenalty_id integer NOT NULL,
    seconds integer DEFAULT 0 NOT NULL,
    maxp_sign queuepenaltychange_sign,
    maxp_value integer,
    minp_sign queuepenaltychange_sign,
    minp_value integer
);


ALTER TABLE public.queuepenaltychange OWNER TO asterisk;

--
-- Name: queueskill; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queueskill (
    id integer NOT NULL,
    catid integer DEFAULT 1 NOT NULL,
    name character varying(64) DEFAULT ''::character varying NOT NULL,
    description text,
    printscreen character varying(5)
);


ALTER TABLE public.queueskill OWNER TO asterisk;

--
-- Name: queueskill_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE queueskill_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queueskill_id_seq OWNER TO asterisk;

--
-- Name: queueskill_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE queueskill_id_seq OWNED BY queueskill.id;


--
-- Name: queueskillcat; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queueskillcat (
    id integer NOT NULL,
    name character varying(64) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.queueskillcat OWNER TO asterisk;

--
-- Name: queueskillcat_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE queueskillcat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queueskillcat_id_seq OWNER TO asterisk;

--
-- Name: queueskillcat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE queueskillcat_id_seq OWNED BY queueskillcat.id;


--
-- Name: queueskillrule; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE queueskillrule (
    id integer NOT NULL,
    name character varying(64) DEFAULT ''::character varying NOT NULL,
    rule text
);


ALTER TABLE public.queueskillrule OWNER TO asterisk;

--
-- Name: queueskillrule_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE queueskillrule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queueskillrule_id_seq OWNER TO asterisk;

--
-- Name: queueskillrule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE queueskillrule_id_seq OWNED BY queueskillrule.id;


--
-- Name: record_campaign; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE record_campaign (
    id integer NOT NULL,
    campaign_name character varying(128) NOT NULL,
    activated boolean NOT NULL,
    base_filename character varying(64) NOT NULL,
    queue_id integer,
    start_date timestamp without time zone,
    end_date timestamp without time zone
);


ALTER TABLE public.record_campaign OWNER TO asterisk;

--
-- Name: record_campaign_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE record_campaign_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.record_campaign_id_seq OWNER TO asterisk;

--
-- Name: record_campaign_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE record_campaign_id_seq OWNED BY record_campaign.id;


--
-- Name: recording; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE recording (
    cid character varying(32) NOT NULL,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    caller character varying(32),
    client_id character varying(1024),
    callee character varying(32),
    filename character varying(1024),
    campaign_id integer NOT NULL,
    agent_id integer NOT NULL
);


ALTER TABLE public.recording OWNER TO asterisk;

--
-- Name: resolvconf; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE resolvconf (
    id integer NOT NULL,
    hostname character varying(63) DEFAULT 'xivo'::character varying NOT NULL,
    domain character varying(255) DEFAULT ''::character varying NOT NULL,
    nameserver1 character varying(255),
    nameserver2 character varying(255),
    nameserver3 character varying(255),
    search character varying(255),
    description text
);


ALTER TABLE public.resolvconf OWNER TO asterisk;

--
-- Name: resolvconf_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE resolvconf_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resolvconf_id_seq OWNER TO asterisk;

--
-- Name: resolvconf_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE resolvconf_id_seq OWNED BY resolvconf.id;


--
-- Name: rightcall; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE rightcall (
    id integer NOT NULL,
    name character varying(128) DEFAULT ''::character varying NOT NULL,
    passwd character varying(40) DEFAULT ''::character varying NOT NULL,
    "authorization" integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    description text
);


ALTER TABLE public.rightcall OWNER TO asterisk;

--
-- Name: rightcall_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE rightcall_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rightcall_id_seq OWNER TO asterisk;

--
-- Name: rightcall_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE rightcall_id_seq OWNED BY rightcall.id;


--
-- Name: rightcallexten; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE rightcallexten (
    id integer NOT NULL,
    rightcallid integer DEFAULT 0 NOT NULL,
    exten character varying(40) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.rightcallexten OWNER TO asterisk;

--
-- Name: rightcallexten_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE rightcallexten_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rightcallexten_id_seq OWNER TO asterisk;

--
-- Name: rightcallexten_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE rightcallexten_id_seq OWNED BY rightcallexten.id;


--
-- Name: rightcallmember; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE rightcallmember (
    id integer NOT NULL,
    rightcallid integer DEFAULT 0 NOT NULL,
    type rightcallmember_type NOT NULL,
    typeval character varying(128) DEFAULT '0'::character varying NOT NULL
);


ALTER TABLE public.rightcallmember OWNER TO asterisk;

--
-- Name: rightcallmember_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE rightcallmember_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rightcallmember_id_seq OWNER TO asterisk;

--
-- Name: rightcallmember_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE rightcallmember_id_seq OWNED BY rightcallmember.id;


--
-- Name: sccpdevice; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE sccpdevice (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    device character varying(80) NOT NULL,
    line character varying(80) DEFAULT ''::character varying NOT NULL,
    voicemail character varying(80) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.sccpdevice OWNER TO asterisk;

--
-- Name: sccpdevice_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE sccpdevice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sccpdevice_id_seq OWNER TO asterisk;

--
-- Name: sccpdevice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE sccpdevice_id_seq OWNED BY sccpdevice.id;


--
-- Name: sccpgeneralsettings; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE sccpgeneralsettings (
    id integer NOT NULL,
    option_name character varying(80) NOT NULL,
    option_value character varying(80) NOT NULL
);


ALTER TABLE public.sccpgeneralsettings OWNER TO asterisk;

--
-- Name: sccpgeneralsettings_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE sccpgeneralsettings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sccpgeneralsettings_id_seq OWNER TO asterisk;

--
-- Name: sccpgeneralsettings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE sccpgeneralsettings_id_seq OWNED BY sccpgeneralsettings.id;


--
-- Name: sccpline; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE sccpline (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    cid_name character varying(80) NOT NULL,
    cid_num character varying(80) NOT NULL,
    context character varying(80) NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    protocol trunk_protocol DEFAULT 'sccp'::trunk_protocol NOT NULL,
    disallow character varying(100),
    allow text
);


ALTER TABLE public.sccpline OWNER TO asterisk;

--
-- Name: sccpline_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE sccpline_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sccpline_id_seq OWNER TO asterisk;

--
-- Name: sccpline_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE sccpline_id_seq OWNED BY sccpline.id;


--
-- Name: schedule; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE schedule (
    id integer NOT NULL,
    name character varying(255) DEFAULT ''::character varying NOT NULL,
    timezone character varying(128),
    fallback_action dialaction_action DEFAULT 'none'::dialaction_action NOT NULL,
    fallback_actionid character varying(255),
    fallback_actionargs character varying(255),
    description text,
    commented integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.schedule OWNER TO asterisk;

--
-- Name: schedule_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE schedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_id_seq OWNER TO asterisk;

--
-- Name: schedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE schedule_id_seq OWNED BY schedule.id;


--
-- Name: schedule_path; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE schedule_path (
    schedule_id integer NOT NULL,
    path schedule_path_type NOT NULL,
    pathid integer NOT NULL,
    "order" integer NOT NULL
);


ALTER TABLE public.schedule_path OWNER TO asterisk;

--
-- Name: schedule_time; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE schedule_time (
    id integer NOT NULL,
    schedule_id integer,
    mode schedule_time_mode DEFAULT 'opened'::schedule_time_mode NOT NULL,
    hours character varying(512),
    weekdays character varying(512),
    monthdays character varying(512),
    months character varying(512),
    action dialaction_action,
    actionid character varying(255),
    actionargs character varying(255),
    commented integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.schedule_time OWNER TO asterisk;

--
-- Name: schedule_time_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE schedule_time_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.schedule_time_id_seq OWNER TO asterisk;

--
-- Name: schedule_time_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE schedule_time_id_seq OWNED BY schedule_time.id;


--
-- Name: serverfeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE serverfeatures (
    id integer NOT NULL,
    serverid integer NOT NULL,
    type serverfeatures_type NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    feature character varying(64) DEFAULT 'phonebook'::character varying NOT NULL,
    CONSTRAINT serverfeatures_feature_check CHECK (((feature)::text = 'phonebook'::text))
);


ALTER TABLE public.serverfeatures OWNER TO asterisk;

--
-- Name: serverfeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE serverfeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.serverfeatures_id_seq OWNER TO asterisk;

--
-- Name: serverfeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE serverfeatures_id_seq OWNED BY serverfeatures.id;


--
-- Name: session; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE session (
    sessid character varying(32) NOT NULL,
    start integer NOT NULL,
    expire integer NOT NULL,
    identifier character varying(255) NOT NULL,
    data text NOT NULL
);


ALTER TABLE public.session OWNER TO asterisk;

--
-- Name: sipauthentication; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE sipauthentication (
    id integer NOT NULL,
    usersip_id integer,
    "user" character varying(255) NOT NULL,
    secretmode sipauthentication_secretmode NOT NULL,
    secret character varying(255) NOT NULL,
    realm character varying(1024) NOT NULL
);


ALTER TABLE public.sipauthentication OWNER TO asterisk;

--
-- Name: sipauthentication_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE sipauthentication_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sipauthentication_id_seq OWNER TO asterisk;

--
-- Name: sipauthentication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE sipauthentication_id_seq OWNED BY sipauthentication.id;


--
-- Name: stat_agent; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stat_agent (
    id integer NOT NULL,
    name character varying(128) NOT NULL
);


ALTER TABLE public.stat_agent OWNER TO asterisk;

--
-- Name: stat_agent_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE stat_agent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stat_agent_id_seq OWNER TO asterisk;

--
-- Name: stat_agent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE stat_agent_id_seq OWNED BY stat_agent.id;


--
-- Name: stat_agent_periodic; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stat_agent_periodic (
    id integer NOT NULL,
    "time" timestamp without time zone NOT NULL,
    login_time interval DEFAULT '00:00:00'::interval NOT NULL,
    agent_id integer,
    pause_time interval DEFAULT '00:00:00'::interval NOT NULL,
    wrapup_time interval DEFAULT '00:00:00'::interval NOT NULL
);


ALTER TABLE public.stat_agent_periodic OWNER TO asterisk;

--
-- Name: stat_agent_periodic_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE stat_agent_periodic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stat_agent_periodic_id_seq OWNER TO asterisk;

--
-- Name: stat_agent_periodic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE stat_agent_periodic_id_seq OWNED BY stat_agent_periodic.id;


--
-- Name: stat_call_on_queue; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stat_call_on_queue (
    id integer NOT NULL,
    callid character varying(32) NOT NULL,
    "time" timestamp without time zone NOT NULL,
    ringtime integer DEFAULT 0 NOT NULL,
    talktime integer DEFAULT 0 NOT NULL,
    waittime integer DEFAULT 0 NOT NULL,
    queue_id integer,
    agent_id integer,
    status call_exit_type NOT NULL
);


ALTER TABLE public.stat_call_on_queue OWNER TO asterisk;

--
-- Name: stat_call_on_queue_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE stat_call_on_queue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stat_call_on_queue_id_seq OWNER TO asterisk;

--
-- Name: stat_call_on_queue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE stat_call_on_queue_id_seq OWNED BY stat_call_on_queue.id;


--
-- Name: stat_queue; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stat_queue (
    id integer NOT NULL,
    name character varying(128) NOT NULL
);


ALTER TABLE public.stat_queue OWNER TO asterisk;

--
-- Name: stat_queue_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE stat_queue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stat_queue_id_seq OWNER TO asterisk;

--
-- Name: stat_queue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE stat_queue_id_seq OWNED BY stat_queue.id;


--
-- Name: stat_queue_periodic; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stat_queue_periodic (
    id integer NOT NULL,
    "time" timestamp without time zone NOT NULL,
    answered integer DEFAULT 0 NOT NULL,
    abandoned integer DEFAULT 0 NOT NULL,
    total integer DEFAULT 0 NOT NULL,
    "full" integer DEFAULT 0 NOT NULL,
    closed integer DEFAULT 0 NOT NULL,
    joinempty integer DEFAULT 0 NOT NULL,
    leaveempty integer DEFAULT 0 NOT NULL,
    timeout integer DEFAULT 0 NOT NULL,
    queue_id integer,
    divert_ca_ratio integer DEFAULT 0 NOT NULL,
    divert_waittime integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.stat_queue_periodic OWNER TO asterisk;

--
-- Name: stat_queue_periodic_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE stat_queue_periodic_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stat_queue_periodic_id_seq OWNER TO asterisk;

--
-- Name: stat_queue_periodic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE stat_queue_periodic_id_seq OWNED BY stat_queue_periodic.id;


--
-- Name: staticiax; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE staticiax (
    id integer NOT NULL,
    cat_metric integer DEFAULT 0 NOT NULL,
    var_metric integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    filename character varying(128) NOT NULL,
    category character varying(128) NOT NULL,
    var_name character varying(128) NOT NULL,
    var_val character varying(255)
);


ALTER TABLE public.staticiax OWNER TO asterisk;

--
-- Name: staticiax_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE staticiax_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staticiax_id_seq OWNER TO asterisk;

--
-- Name: staticiax_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE staticiax_id_seq OWNED BY staticiax.id;


--
-- Name: staticmeetme; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE staticmeetme (
    id integer NOT NULL,
    cat_metric integer DEFAULT 0 NOT NULL,
    var_metric integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    filename character varying(128) NOT NULL,
    category character varying(128) NOT NULL,
    var_name character varying(128) NOT NULL,
    var_val character varying(128)
);


ALTER TABLE public.staticmeetme OWNER TO asterisk;

--
-- Name: staticmeetme_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE staticmeetme_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staticmeetme_id_seq OWNER TO asterisk;

--
-- Name: staticmeetme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE staticmeetme_id_seq OWNED BY staticmeetme.id;


--
-- Name: staticqueue; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE staticqueue (
    id integer NOT NULL,
    cat_metric integer DEFAULT 0 NOT NULL,
    var_metric integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    filename character varying(128) NOT NULL,
    category character varying(128) NOT NULL,
    var_name character varying(128) NOT NULL,
    var_val character varying(128)
);


ALTER TABLE public.staticqueue OWNER TO asterisk;

--
-- Name: staticqueue_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE staticqueue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staticqueue_id_seq OWNER TO asterisk;

--
-- Name: staticqueue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE staticqueue_id_seq OWNED BY staticqueue.id;


--
-- Name: staticsip; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE staticsip (
    id integer NOT NULL,
    cat_metric integer DEFAULT 0 NOT NULL,
    var_metric integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    filename character varying(128) NOT NULL,
    category character varying(128) NOT NULL,
    var_name character varying(128) NOT NULL,
    var_val character varying(255)
);


ALTER TABLE public.staticsip OWNER TO asterisk;

--
-- Name: staticsip_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE staticsip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staticsip_id_seq OWNER TO asterisk;

--
-- Name: staticsip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE staticsip_id_seq OWNED BY staticsip.id;


--
-- Name: staticvoicemail; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE staticvoicemail (
    id integer NOT NULL,
    cat_metric integer DEFAULT 0 NOT NULL,
    var_metric integer DEFAULT 0 NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    filename character varying(128) NOT NULL,
    category character varying(128) NOT NULL,
    var_name character varying(128) NOT NULL,
    var_val text
);


ALTER TABLE public.staticvoicemail OWNER TO asterisk;

--
-- Name: staticvoicemail_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE staticvoicemail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staticvoicemail_id_seq OWNER TO asterisk;

--
-- Name: staticvoicemail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE staticvoicemail_id_seq OWNED BY staticvoicemail.id;


--
-- Name: stats_conf; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stats_conf (
    id integer NOT NULL,
    name character varying(64) DEFAULT ''::character varying NOT NULL,
    hour_start time without time zone NOT NULL,
    hour_end time without time zone NOT NULL,
    homepage integer,
    timezone character varying(128) DEFAULT ''::character varying NOT NULL,
    default_delta character varying(16) DEFAULT '0'::character varying NOT NULL,
    monday smallint DEFAULT 0 NOT NULL,
    tuesday smallint DEFAULT 0 NOT NULL,
    wednesday smallint DEFAULT 0 NOT NULL,
    thursday smallint DEFAULT 0 NOT NULL,
    friday smallint DEFAULT 0 NOT NULL,
    saturday smallint DEFAULT 0 NOT NULL,
    sunday smallint DEFAULT 0 NOT NULL,
    period1 character varying(16) DEFAULT '0'::character varying NOT NULL,
    period2 character varying(16) DEFAULT '0'::character varying NOT NULL,
    period3 character varying(16) DEFAULT '0'::character varying NOT NULL,
    period4 character varying(16) DEFAULT '0'::character varying NOT NULL,
    period5 character varying(16) DEFAULT '0'::character varying NOT NULL,
    dbegcache integer DEFAULT 0,
    dendcache integer DEFAULT 0,
    dgenercache integer DEFAULT 0,
    dcreate integer DEFAULT 0,
    dupdate integer DEFAULT 0,
    disable smallint DEFAULT 0 NOT NULL,
    description text
);


ALTER TABLE public.stats_conf OWNER TO asterisk;

--
-- Name: stats_conf_agent; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stats_conf_agent (
    stats_conf_id integer NOT NULL,
    agentfeatures_id integer NOT NULL
);


ALTER TABLE public.stats_conf_agent OWNER TO asterisk;

--
-- Name: stats_conf_group; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stats_conf_group (
    stats_conf_id integer NOT NULL,
    groupfeatures_id integer NOT NULL
);


ALTER TABLE public.stats_conf_group OWNER TO asterisk;

--
-- Name: stats_conf_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE stats_conf_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stats_conf_id_seq OWNER TO asterisk;

--
-- Name: stats_conf_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE stats_conf_id_seq OWNED BY stats_conf.id;


--
-- Name: stats_conf_incall; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stats_conf_incall (
    stats_conf_id integer NOT NULL,
    incall_id integer NOT NULL
);


ALTER TABLE public.stats_conf_incall OWNER TO asterisk;

--
-- Name: stats_conf_queue; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stats_conf_queue (
    stats_conf_id integer NOT NULL,
    queuefeatures_id integer NOT NULL,
    qos smallint DEFAULT 0 NOT NULL
);


ALTER TABLE public.stats_conf_queue OWNER TO asterisk;

--
-- Name: stats_conf_user; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stats_conf_user (
    stats_conf_id integer NOT NULL,
    userfeatures_id integer NOT NULL
);


ALTER TABLE public.stats_conf_user OWNER TO asterisk;

--
-- Name: stats_conf_xivouser; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE stats_conf_xivouser (
    stats_conf_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.stats_conf_xivouser OWNER TO asterisk;

--
-- Name: trunkfeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE trunkfeatures (
    id integer NOT NULL,
    protocolid integer NOT NULL,
    registerid integer DEFAULT 0 NOT NULL,
    registercommented integer DEFAULT 0 NOT NULL,
    description text,
    protocol trunk_protocol NOT NULL
);


ALTER TABLE public.trunkfeatures OWNER TO asterisk;

--
-- Name: trunkfeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE trunkfeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trunkfeatures_id_seq OWNER TO asterisk;

--
-- Name: trunkfeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE trunkfeatures_id_seq OWNED BY trunkfeatures.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE "user" (
    id integer NOT NULL,
    login character varying(64) DEFAULT ''::character varying NOT NULL,
    passwd character varying(64) DEFAULT ''::character varying NOT NULL,
    meta user_meta DEFAULT 'user'::user_meta NOT NULL,
    valid integer DEFAULT 1 NOT NULL,
    "time" integer DEFAULT 0 NOT NULL,
    dcreate integer DEFAULT 0 NOT NULL,
    dupdate integer DEFAULT 0 NOT NULL,
    obj text NOT NULL,
    entity_id integer
);


ALTER TABLE public."user" OWNER TO asterisk;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO asterisk;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE user_id_seq OWNED BY "user".id;


--
-- Name: user_line; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE user_line (
    id integer NOT NULL,
    user_id integer,
    line_id integer NOT NULL,
    extension_id integer,
    main_user boolean NOT NULL,
    main_line boolean NOT NULL
);


ALTER TABLE public.user_line OWNER TO asterisk;

--
-- Name: user_line_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE user_line_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_line_id_seq OWNER TO asterisk;

--
-- Name: user_line_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE user_line_id_seq OWNED BY user_line.id;


--
-- Name: usercustom; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE usercustom (
    id integer NOT NULL,
    name character varying(40),
    context character varying(39),
    interface character varying(128) NOT NULL,
    intfsuffix character varying(32) DEFAULT ''::character varying NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    category usercustom_category NOT NULL,
    protocol trunk_protocol DEFAULT 'custom'::trunk_protocol NOT NULL
);


ALTER TABLE public.usercustom OWNER TO asterisk;

--
-- Name: usercustom_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE usercustom_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usercustom_id_seq OWNER TO asterisk;

--
-- Name: usercustom_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE usercustom_id_seq OWNED BY usercustom.id;


--
-- Name: userfeatures; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE userfeatures (
    id integer NOT NULL,
    firstname character varying(128) DEFAULT ''::character varying NOT NULL,
    lastname character varying(128) DEFAULT ''::character varying NOT NULL,
    voicemailtype userfeatures_voicemailtype,
    voicemailid integer,
    agentid integer,
    pictureid integer,
    entityid integer,
    callerid character varying(160),
    ringseconds integer DEFAULT 30 NOT NULL,
    simultcalls integer DEFAULT 5 NOT NULL,
    enableclient integer DEFAULT 1 NOT NULL,
    loginclient character varying(64) DEFAULT ''::character varying NOT NULL,
    passwdclient character varying(64) DEFAULT ''::character varying NOT NULL,
    enablehint integer DEFAULT 1 NOT NULL,
    enablevoicemail integer DEFAULT 0 NOT NULL,
    enablexfer integer DEFAULT 1 NOT NULL,
    enableautomon integer DEFAULT 0 NOT NULL,
    callrecord integer DEFAULT 0 NOT NULL,
    incallfilter integer DEFAULT 0 NOT NULL,
    enablednd integer DEFAULT 0 NOT NULL,
    enableunc integer DEFAULT 0 NOT NULL,
    destunc character varying(128) DEFAULT ''::character varying NOT NULL,
    enablerna integer DEFAULT 0 NOT NULL,
    destrna character varying(128) DEFAULT ''::character varying NOT NULL,
    enablebusy integer DEFAULT 0 NOT NULL,
    destbusy character varying(128) DEFAULT ''::character varying NOT NULL,
    musiconhold character varying(128) DEFAULT ''::character varying NOT NULL,
    outcallerid character varying(80) DEFAULT ''::character varying NOT NULL,
    mobilephonenumber character varying(128) DEFAULT ''::character varying NOT NULL,
    userfield character varying(128) DEFAULT ''::character varying NOT NULL,
    bsfilter generic_bsfilter DEFAULT 'no'::generic_bsfilter NOT NULL,
    preprocess_subroutine character varying(39),
    timezone character varying(128),
    language character varying(20),
    ringintern character varying(64),
    ringextern character varying(64),
    ringgroup character varying(64),
    ringforward character varying(64),
    rightcallcode character varying(16),
    commented integer DEFAULT 0 NOT NULL,
    description text NOT NULL,
    cti_profile_id integer,
    func_key_template_id integer,
    func_key_private_template_id integer NOT NULL
);


ALTER TABLE public.userfeatures OWNER TO asterisk;

--
-- Name: userfeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE userfeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userfeatures_id_seq OWNER TO asterisk;

--
-- Name: userfeatures_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE userfeatures_id_seq OWNED BY userfeatures.id;


--
-- Name: useriax; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE useriax (
    id integer NOT NULL,
    name character varying(40) NOT NULL,
    username character varying(80),
    secret character varying(80) DEFAULT ''::character varying NOT NULL,
    dbsecret character varying(255) DEFAULT ''::character varying NOT NULL,
    context character varying(39),
    language character varying(20),
    accountcode character varying(20),
    amaflags useriax_amaflags DEFAULT 'default'::useriax_amaflags,
    mailbox character varying(80),
    callerid character varying(160),
    fullname character varying(80),
    cid_number character varying(80),
    trunk integer DEFAULT 0 NOT NULL,
    auth useriax_auth DEFAULT 'plaintext,md5'::useriax_auth NOT NULL,
    encryption useriax_encryption,
    forceencryption useriax_encryption,
    maxauthreq integer,
    inkeys character varying(80),
    outkey character varying(80),
    adsi integer,
    transfer useriax_transfer,
    codecpriority useriax_codecpriority,
    jitterbuffer integer,
    forcejitterbuffer integer,
    sendani integer DEFAULT 0 NOT NULL,
    qualify character varying(4) DEFAULT 'no'::character varying NOT NULL,
    qualifysmoothing integer DEFAULT 0 NOT NULL,
    qualifyfreqok integer DEFAULT 60000 NOT NULL,
    qualifyfreqnotok integer DEFAULT 10000 NOT NULL,
    timezone character varying(80),
    disallow character varying(100),
    allow text,
    mohinterpret character varying(80),
    mohsuggest character varying(80),
    deny character varying(31),
    permit character varying(31),
    defaultip character varying(255),
    sourceaddress character varying(255),
    setvar character varying(100) DEFAULT ''::character varying NOT NULL,
    host character varying(255) DEFAULT 'dynamic'::character varying NOT NULL,
    port integer,
    mask character varying(15),
    regexten character varying(80),
    peercontext character varying(80),
    ipaddr character varying(255) DEFAULT ''::character varying NOT NULL,
    regseconds integer DEFAULT 0 NOT NULL,
    immediate integer,
    parkinglot integer,
    category useriax_category NOT NULL,
    commented integer DEFAULT 0 NOT NULL,
    requirecalltoken character varying(4) DEFAULT 'no'::character varying NOT NULL,
    type useriax_type NOT NULL,
    keyrotate integer,
    protocol trunk_protocol DEFAULT 'iax'::trunk_protocol NOT NULL
);


ALTER TABLE public.useriax OWNER TO asterisk;

--
-- Name: useriax_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE useriax_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.useriax_id_seq OWNER TO asterisk;

--
-- Name: useriax_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE useriax_id_seq OWNED BY useriax.id;


--
-- Name: usersip; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE usersip (
    id integer NOT NULL,
    name character varying(40) NOT NULL,
    username character varying(80),
    secret character varying(80) DEFAULT ''::character varying NOT NULL,
    md5secret character varying(32) DEFAULT ''::character varying NOT NULL,
    context character varying(39),
    language character varying(20),
    accountcode character varying(20),
    amaflags useriax_amaflags DEFAULT 'default'::useriax_amaflags NOT NULL,
    allowtransfer integer,
    fromuser character varying(80),
    fromdomain character varying(255),
    mailbox character varying(80),
    subscribemwi integer DEFAULT 0 NOT NULL,
    buggymwi integer,
    "call-limit" integer DEFAULT 0 NOT NULL,
    callerid character varying(160),
    fullname character varying(80),
    cid_number character varying(80),
    maxcallbitrate integer,
    insecure usersip_insecure,
    promiscredir integer,
    usereqphone integer,
    videosupport usersip_videosupport,
    trustrpid integer,
    allowsubscribe integer,
    allowoverlap integer,
    dtmfmode usersip_dtmfmode,
    rfc2833compensate integer,
    qualify character varying(4),
    g726nonstandard integer,
    disallow character varying(100),
    allow text,
    autoframing integer,
    mohinterpret character varying(80),
    mohsuggest character varying(80),
    useclientcode integer,
    progressinband usersip_progressinband,
    t38pt_udptl integer,
    t38pt_usertpsource integer,
    rtptimeout integer,
    rtpholdtimeout integer,
    rtpkeepalive integer,
    deny character varying(31),
    permit character varying(31),
    defaultip character varying(255),
    setvar character varying(100) DEFAULT ''::character varying NOT NULL,
    host character varying(255) DEFAULT 'dynamic'::character varying NOT NULL,
    port integer,
    regexten character varying(80),
    subscribecontext character varying(80),
    fullcontact character varying(255),
    vmexten character varying(40),
    callingpres integer,
    ipaddr character varying(255) DEFAULT ''::character varying NOT NULL,
    regseconds integer DEFAULT 0 NOT NULL,
    regserver character varying(20),
    lastms character varying(15) DEFAULT ''::character varying NOT NULL,
    parkinglot integer,
    category useriax_category NOT NULL,
    outboundproxy character varying(1024),
    transport character varying(255),
    remotesecret character varying(255),
    directmedia usersip_directmedia,
    callcounter integer,
    busylevel integer,
    ignoresdpversion integer,
    "session-timers" usersip_session_timers,
    "session-expires" integer,
    "session-minse" integer,
    "session-refresher" usersip_session_refresher,
    callbackextension character varying(255),
    registertrying integer,
    timert1 integer,
    timerb integer,
    qualifyfreq integer,
    contactpermit character varying(1024),
    contactdeny character varying(1024),
    unsolicited_mailbox character varying(1024),
    use_q850_reason integer,
    encryption integer,
    snom_aoc_enabled integer,
    maxforwards integer,
    disallowed_methods character varying(1024),
    textsupport integer,
    commented integer DEFAULT 0 NOT NULL,
    type useriax_type NOT NULL,
    protocol trunk_protocol DEFAULT 'sip'::trunk_protocol NOT NULL,
    sendrpid character varying(16),
    nat usersip_nat
);


ALTER TABLE public.usersip OWNER TO asterisk;

--
-- Name: usersip_id_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE usersip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usersip_id_seq OWNER TO asterisk;

--
-- Name: usersip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE usersip_id_seq OWNED BY usersip.id;


--
-- Name: voicemail; Type: TABLE; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE TABLE voicemail (
    uniqueid integer NOT NULL,
    context character varying(39) NOT NULL,
    mailbox character varying(40) NOT NULL,
    password character varying(80) DEFAULT ''::character varying NOT NULL,
    fullname character varying(80) DEFAULT ''::character varying NOT NULL,
    email character varying(80),
    pager character varying(80),
    dialout character varying(39),
    callback character varying(39),
    exitcontext character varying(39),
    language character varying(20),
    tz character varying(80),
    attach integer,
    saycid integer,
    review integer,
    operator integer,
    envelope integer,
    sayduration integer,
    saydurationm integer,
    sendvoicemail integer,
    deletevoicemail integer DEFAULT 0 NOT NULL,
    forcename integer,
    forcegreetings integer,
    hidefromdir voicemail_hidefromdir DEFAULT 'no'::voicemail_hidefromdir NOT NULL,
    maxmsg integer,
    emailsubject character varying(1024),
    emailbody text,
    imapuser character varying(1024),
    imappassword character varying(1024),
    imapfolder character varying(1024),
    imapvmsharedid character varying(1024),
    attachfmt character varying(1024),
    serveremail character varying(1024),
    locale character varying(1024),
    tempgreetwarn integer,
    messagewrap integer,
    moveheard integer,
    minsecs integer,
    maxsecs integer,
    nextaftercmd integer,
    backupdeleted integer,
    volgain double precision,
    passwordlocation voicemail_passwordlocation,
    commented integer DEFAULT 0 NOT NULL,
    skipcheckpass integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.voicemail OWNER TO asterisk;

--
-- Name: voicemail_uniqueid_seq; Type: SEQUENCE; Schema: public; Owner: asterisk
--

CREATE SEQUENCE voicemail_uniqueid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voicemail_uniqueid_seq OWNER TO asterisk;

--
-- Name: voicemail_uniqueid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asterisk
--

ALTER SEQUENCE voicemail_uniqueid_seq OWNED BY voicemail.uniqueid;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY accessfeatures ALTER COLUMN id SET DEFAULT nextval('accessfeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY accesswebservice ALTER COLUMN id SET DEFAULT nextval('accesswebservice_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY agentfeatures ALTER COLUMN id SET DEFAULT nextval('agentfeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY agentglobalparams ALTER COLUMN id SET DEFAULT nextval('agentglobalparams_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY agentgroup ALTER COLUMN id SET DEFAULT nextval('agentgroup_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY attachment ALTER COLUMN id SET DEFAULT nextval('attachment_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY call_log ALTER COLUMN id SET DEFAULT nextval('call_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY callfilter ALTER COLUMN id SET DEFAULT nextval('callfilter_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY callfiltermember ALTER COLUMN id SET DEFAULT nextval('callfiltermember_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cel ALTER COLUMN id SET DEFAULT nextval('cel_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY contexttype ALTER COLUMN id SET DEFAULT nextval('contexttype_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_preference ALTER COLUMN id SET DEFAULT nextval('cti_preference_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile ALTER COLUMN id SET DEFAULT nextval('cti_profile_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_service ALTER COLUMN id SET DEFAULT nextval('cti_service_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_xlet ALTER COLUMN id SET DEFAULT nextval('cti_xlet_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_xlet_layout ALTER COLUMN id SET DEFAULT nextval('cti_xlet_layout_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cticontexts ALTER COLUMN id SET DEFAULT nextval('cticontexts_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctidirectories ALTER COLUMN id SET DEFAULT nextval('ctidirectories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctidisplays ALTER COLUMN id SET DEFAULT nextval('ctidisplays_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctilog ALTER COLUMN id SET DEFAULT nextval('ctilog_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctimain ALTER COLUMN id SET DEFAULT nextval('ctimain_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctiphonehints ALTER COLUMN id SET DEFAULT nextval('ctiphonehints_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctiphonehintsgroup ALTER COLUMN id SET DEFAULT nextval('ctiphonehintsgroup_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctipresences ALTER COLUMN id SET DEFAULT nextval('ctipresences_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctireversedirectories ALTER COLUMN id SET DEFAULT nextval('ctireversedirectories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctisheetactions ALTER COLUMN id SET DEFAULT nextval('ctisheetactions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctisheetevents ALTER COLUMN id SET DEFAULT nextval('ctisheetevents_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ctistatus ALTER COLUMN id SET DEFAULT nextval('ctistatus_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY dhcp ALTER COLUMN id SET DEFAULT nextval('dhcp_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY dialpattern ALTER COLUMN id SET DEFAULT nextval('dialpattern_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY directories ALTER COLUMN id SET DEFAULT nextval('directories_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY entity ALTER COLUMN id SET DEFAULT nextval('entity_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY extensions ALTER COLUMN id SET DEFAULT nextval('extensions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY features ALTER COLUMN id SET DEFAULT nextval('features_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key ALTER COLUMN id SET DEFAULT nextval('func_key_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_destination_type ALTER COLUMN id SET DEFAULT nextval('func_key_destination_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_template ALTER COLUMN id SET DEFAULT nextval('func_key_template_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_type ALTER COLUMN id SET DEFAULT nextval('func_key_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY general ALTER COLUMN id SET DEFAULT nextval('general_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY groupfeatures ALTER COLUMN id SET DEFAULT nextval('groupfeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY iaxcallnumberlimits ALTER COLUMN id SET DEFAULT nextval('iaxcallnumberlimits_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY incall ALTER COLUMN id SET DEFAULT nextval('incall_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ldapfilter ALTER COLUMN id SET DEFAULT nextval('ldapfilter_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY ldapserver ALTER COLUMN id SET DEFAULT nextval('ldapserver_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY linefeatures ALTER COLUMN id SET DEFAULT nextval('linefeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY mail ALTER COLUMN id SET DEFAULT nextval('mail_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY meetmefeatures ALTER COLUMN id SET DEFAULT nextval('meetmefeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY meetmeguest ALTER COLUMN id SET DEFAULT nextval('meetmeguest_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY monitoring ALTER COLUMN id SET DEFAULT nextval('monitoring_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY musiconhold ALTER COLUMN id SET DEFAULT nextval('musiconhold_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY netiface ALTER COLUMN id SET DEFAULT nextval('netiface_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY outcall ALTER COLUMN id SET DEFAULT nextval('outcall_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY paging ALTER COLUMN id SET DEFAULT nextval('paging_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY phonebook ALTER COLUMN id SET DEFAULT nextval('phonebook_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY phonebookaddress ALTER COLUMN id SET DEFAULT nextval('phonebookaddress_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY phonebooknumber ALTER COLUMN id SET DEFAULT nextval('phonebooknumber_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY provisioning ALTER COLUMN id SET DEFAULT nextval('provisioning_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY queue_info ALTER COLUMN id SET DEFAULT nextval('queue_info_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY queue_log ALTER COLUMN id SET DEFAULT nextval('queue_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY queuefeatures ALTER COLUMN id SET DEFAULT nextval('queuefeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY queuepenalty ALTER COLUMN id SET DEFAULT nextval('queuepenalty_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY queueskill ALTER COLUMN id SET DEFAULT nextval('queueskill_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY queueskillcat ALTER COLUMN id SET DEFAULT nextval('queueskillcat_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY queueskillrule ALTER COLUMN id SET DEFAULT nextval('queueskillrule_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY record_campaign ALTER COLUMN id SET DEFAULT nextval('record_campaign_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY resolvconf ALTER COLUMN id SET DEFAULT nextval('resolvconf_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY rightcall ALTER COLUMN id SET DEFAULT nextval('rightcall_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY rightcallexten ALTER COLUMN id SET DEFAULT nextval('rightcallexten_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY rightcallmember ALTER COLUMN id SET DEFAULT nextval('rightcallmember_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY sccpdevice ALTER COLUMN id SET DEFAULT nextval('sccpdevice_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY sccpgeneralsettings ALTER COLUMN id SET DEFAULT nextval('sccpgeneralsettings_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY sccpline ALTER COLUMN id SET DEFAULT nextval('sccpline_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY schedule ALTER COLUMN id SET DEFAULT nextval('schedule_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY schedule_time ALTER COLUMN id SET DEFAULT nextval('schedule_time_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY serverfeatures ALTER COLUMN id SET DEFAULT nextval('serverfeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY sipauthentication ALTER COLUMN id SET DEFAULT nextval('sipauthentication_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_agent ALTER COLUMN id SET DEFAULT nextval('stat_agent_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_agent_periodic ALTER COLUMN id SET DEFAULT nextval('stat_agent_periodic_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_call_on_queue ALTER COLUMN id SET DEFAULT nextval('stat_call_on_queue_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_queue ALTER COLUMN id SET DEFAULT nextval('stat_queue_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_queue_periodic ALTER COLUMN id SET DEFAULT nextval('stat_queue_periodic_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY staticiax ALTER COLUMN id SET DEFAULT nextval('staticiax_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY staticmeetme ALTER COLUMN id SET DEFAULT nextval('staticmeetme_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY staticqueue ALTER COLUMN id SET DEFAULT nextval('staticqueue_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY staticsip ALTER COLUMN id SET DEFAULT nextval('staticsip_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY staticvoicemail ALTER COLUMN id SET DEFAULT nextval('staticvoicemail_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stats_conf ALTER COLUMN id SET DEFAULT nextval('stats_conf_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY trunkfeatures ALTER COLUMN id SET DEFAULT nextval('trunkfeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY "user" ALTER COLUMN id SET DEFAULT nextval('user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY user_line ALTER COLUMN id SET DEFAULT nextval('user_line_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY usercustom ALTER COLUMN id SET DEFAULT nextval('usercustom_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY userfeatures ALTER COLUMN id SET DEFAULT nextval('userfeatures_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY useriax ALTER COLUMN id SET DEFAULT nextval('useriax_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY usersip ALTER COLUMN id SET DEFAULT nextval('usersip_id_seq'::regclass);


--
-- Name: uniqueid; Type: DEFAULT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY voicemail ALTER COLUMN uniqueid SET DEFAULT nextval('voicemail_uniqueid_seq'::regclass);


--
-- Data for Name: accessfeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY accessfeatures (id, host, commented, feature) FROM stdin;
\.


--
-- Name: accessfeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('accessfeatures_id_seq', 1, false);


--
-- Data for Name: accesswebservice; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY accesswebservice (id, name, login, passwd, host, obj, disable, description) FROM stdin;
\.


--
-- Name: accesswebservice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('accesswebservice_id_seq', 1, false);


--
-- Data for Name: agent_login_status; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY agent_login_status (agent_id, login_at, extension, context, interface, state_interface, agent_number) FROM stdin;
\.


--
-- Data for Name: agent_membership_status; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY agent_membership_status (agent_id, queue_id, queue_name, penalty) FROM stdin;
\.


--
-- Data for Name: agentfeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY agentfeatures (id, numgroup, firstname, lastname, number, passwd, context, language, autologoff, "group", description, preprocess_subroutine) FROM stdin;
\.


--
-- Name: agentfeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('agentfeatures_id_seq', 1, false);


--
-- Data for Name: agentglobalparams; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY agentglobalparams (id, category, option_name, option_value) FROM stdin;
2	general	persistentagents	yes
7	general	multiplelogin	no
8	agents	maxlogintries	3
9	agents	endcall	no
\.


--
-- Name: agentglobalparams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('agentglobalparams_id_seq', 9, true);


--
-- Data for Name: agentgroup; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY agentgroup (id, groupid, name, groups, commented, deleted, description) FROM stdin;
1	1	default		0	0	
\.


--
-- Name: agentgroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('agentgroup_id_seq', 1, true);


--
-- Data for Name: agentqueueskill; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY agentqueueskill (agentid, skillid, weight) FROM stdin;
\.


--
-- Data for Name: attachment; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY attachment (id, name, object_type, object_id, file, size, mime) FROM stdin;
\.


--
-- Name: attachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('attachment_id_seq', 1, false);


--
-- Data for Name: call_log; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY call_log (id, date, source_name, source_exten, destination_name, destination_exten, duration, user_field, answered, source_line_identity, destination_line_identity) FROM stdin;
\.


--
-- Name: call_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('call_log_id_seq', 1, false);


--
-- Data for Name: callerid; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY callerid (mode, callerdisplay, type, typeval) FROM stdin;
\.


--
-- Data for Name: callfilter; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY callfilter (id, name, type, bosssecretary, callfrom, ringseconds, commented, description) FROM stdin;
\.


--
-- Name: callfilter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('callfilter_id_seq', 1, false);


--
-- Data for Name: callfiltermember; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY callfiltermember (id, callfilterid, type, typeval, ringseconds, priority, bstype, active) FROM stdin;
\.


--
-- Name: callfiltermember_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('callfiltermember_id_seq', 1, false);


--
-- Data for Name: cel; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cel (id, eventtype, eventtime, userdeftype, cid_name, cid_num, cid_ani, cid_rdnis, cid_dnid, exten, context, channame, appname, appdata, amaflags, accountcode, peeraccount, uniqueid, linkedid, userfield, peer, call_log_id) FROM stdin;
\.


--
-- Name: cel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('cel_id_seq', 1, false);


--
-- Data for Name: context; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY context (name, displayname, entity, contexttype, commented, description) FROM stdin;
__switchboard_directory	Switchboard	xivo_entity	others	0	
\.


--
-- Data for Name: contextinclude; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY contextinclude (context, include, priority) FROM stdin;
\.


--
-- Data for Name: contextmember; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY contextmember (context, type, typeval, varname) FROM stdin;
\.


--
-- Data for Name: contextnumbers; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY contextnumbers (context, type, numberbeg, numberend, didlength) FROM stdin;
\.


--
-- Data for Name: contexttype; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY contexttype (id, name, commented, deletable, description) FROM stdin;
1	internal	0	0	
2	incall	0	0	
3	outcall	0	0	
4	services	0	0	
5	others	0	0	
\.


--
-- Name: contexttype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('contexttype_id_seq', 5, true);


--
-- Data for Name: cti_preference; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_preference (id, option) FROM stdin;
1	loginwindow.url
2	xlet.identity.logagent
3	xlet.identity.pauseagent
4	xlet.agentdetails.noqueueaction
5	xlet.agentdetails.hideastid
6	xlet.agentdetails.hidecontext
7	xlet.agents.fontname
8	xlet.agents.fontsize
9	xlet.agents.iconsize
10	xlet.queues.statsfetchperiod
11	presence.autochangestate
\.


--
-- Name: cti_preference_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('cti_preference_id_seq', 11, true);


--
-- Data for Name: cti_profile; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_profile (id, name, presence_id, phonehints_id) FROM stdin;
2	Client	1	1
1	Agent	1	1
5	Supervisor	1	1
7	Switchboard	1	1
\.


--
-- Name: cti_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('cti_profile_id_seq', 7, true);


--
-- Data for Name: cti_profile_preference; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_profile_preference (profile_id, preference_id, value) FROM stdin;
\.


--
-- Data for Name: cti_profile_service; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_profile_service (profile_id, service_id) FROM stdin;
2	5
2	6
2	7
2	8
\.


--
-- Data for Name: cti_profile_xlet; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_profile_xlet (xlet_id, profile_id, layout_id, closable, movable, floating, scrollable, "order") FROM stdin;
1	1	2	t	t	t	t	0
1	2	2	t	t	t	t	0
1	5	2	t	t	t	t	0
2	2	2	t	t	t	t	2
8	5	1	t	t	t	f	\N
10	2	2	t	t	t	t	1
12	1	1	t	t	f	t	\N
13	5	1	t	t	t	t	\N
14	1	1	t	t	f	t	\N
14	5	1	t	t	t	t	\N
15	1	1	f	t	f	t	\N
15	5	1	f	t	t	t	\N
16	5	1	f	t	t	t	\N
17	5	1	t	t	t	t	\N
1	7	2	t	t	t	t	0
18	7	1	t	t	t	t	1
2	7	1	t	t	t	t	2
4	2	3	t	t	t	t	0
12	2	3	t	t	t	t	1
6	2	3	t	t	t	t	2
3	2	3	t	t	t	t	3
5	2	3	t	t	t	t	4
7	2	3	t	t	t	t	5
11	2	3	t	t	t	t	6
8	2	3	t	t	t	t	7
23	7	1	t	t	t	t	3
\.


--
-- Data for Name: cti_service; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_service (id, key) FROM stdin;
1	enablevm
2	callrecord
3	incallrec
4	incallfilter
5	enablednd
6	fwdunc
7	fwdbusy
8	fwdrna
\.


--
-- Name: cti_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('cti_service_id_seq', 8, true);


--
-- Data for Name: cti_xlet; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_xlet (id, plugin_name) FROM stdin;
1	identity
2	dial
3	history
4	search
6	fax
7	features
8	conference
9	datetime
10	tabber
11	mylocaldir
12	customerinfo
13	agents
14	agentdetails
15	queues
16	queuemembers
17	queueentrydetails
18	switchboard
5	remotedirectory
23	directory
24	agentstatusdashboard
\.


--
-- Name: cti_xlet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('cti_xlet_id_seq', 24, true);


--
-- Data for Name: cti_xlet_layout; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cti_xlet_layout (id, name) FROM stdin;
1	dock
2	grid
3	tab
\.


--
-- Name: cti_xlet_layout_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('cti_xlet_layout_id_seq', 3, true);


--
-- Data for Name: cticontexts; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY cticontexts (id, name, directories, display, description, deletable) FROM stdin;
1	default	xivodir,internal	Display	Contexte par défaut	1
2	__switchboard_directory	xivodir	switchboard		1
\.


--
-- Name: cticontexts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('cticontexts_id_seq', 2, true);


--
-- Data for Name: ctidirectories; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctidirectories (id, name, uri, delimiter, match_direct, match_reverse, description, deletable) FROM stdin;
1	xivodir	phonebook		["phonebook.firstname","phonebook.lastname","phonebook.displayname","phonebook.society","phonebooknumber.office.number"]	["phonebooknumber.office.number","phonebooknumber.mobile.number"]	Répertoire XiVO Externe	1
2	internal	internal		["userfeatures.firstname","userfeatures.lastname"]		Répertoire XiVO Interne	1
\.


--
-- Name: ctidirectories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctidirectories_id_seq', 2, true);


--
-- Data for Name: ctidirectoryfields; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctidirectoryfields (dir_id, fieldname, value) FROM stdin;
1	phone	phonebooknumber.office.number
1	firstname	phonebook.firstname
1	lastname	phonebook.lastname
1	fullname	phonebook.fullname
1	company	phonebook.society
1	mail	phonebook.email
1	reverse	phonebook.fullname
2	firstname	userfeatures.firstname
2	lastname	userfeatures.lastname
2	phone	extensions.exten
\.


--
-- Data for Name: ctidisplays; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctidisplays (id, name, data, deletable, description) FROM stdin;
1	Display	{"10": [ "Nom","","","{db-firstname} {db-lastname}" ],"20": [ "Numéro","phone","","{db-phone}" ],"30": [ "Entreprise","","Inconnue","{db-company}" ],"40": [ "E-mail","","","{db-mail}" ], "50": [ "Source","","","{xivo-directory}" ]}	1	Affichage par défaut
2	switchboard	{ "10": [ "", "status", "", ""],"20": [ "Name", "name", "", "{db-firstname} {db-lastname}"],"30": [ "Number", "number_office", "", "{db-phone}"]}	1	
\.


--
-- Name: ctidisplays_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctidisplays_id_seq', 2, true);


--
-- Data for Name: ctilog; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctilog (id, eventdate, loginclient, company, status, action, arguments, callduration) FROM stdin;
\.


--
-- Name: ctilog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctilog_id_seq', 1, false);


--
-- Data for Name: ctimain; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctimain (id, commandset, ami_ip, ami_port, ami_login, ami_password, cti_ip, cti_port, cti_active, ctis_ip, ctis_port, ctis_active, webi_ip, webi_port, webi_active, info_ip, info_port, info_active, tlscertfile, tlsprivkeyfile, socket_timeout, login_timeout, context_separation, live_reload_conf) FROM stdin;
1	xivocti	127.0.0.1	5038	xivo_cti_user	phaickbebs9	0.0.0.0	5003	1	0.0.0.0	5013	1	127.0.0.1	5004	1	127.0.0.1	5005	1			10	5	1	1
\.


--
-- Name: ctimain_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctimain_id_seq', 1, true);


--
-- Data for Name: ctiphonehints; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctiphonehints (id, idgroup, number, name, color) FROM stdin;
1	1	-2	Inexistant	#030303
2	1	-1	Désactivé	#000000
3	1	0	Disponible	#0DFF25
4	1	1	En ligne OU appelle	#FF032D
5	1	2	Occupé	#FF0008
6	1	4	Indisponible	#FFFFFF
7	1	8	Sonne	#1B0AFF
8	1	9	(En Ligne OU Appelle) ET Sonne	#FF0526
9	1	16	En Attente	#F7FF05
\.


--
-- Name: ctiphonehints_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctiphonehints_id_seq', 9, true);


--
-- Data for Name: ctiphonehintsgroup; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctiphonehintsgroup (id, name, description, deletable) FROM stdin;
1	xivo	De base non supprimable	0
\.


--
-- Name: ctiphonehintsgroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctiphonehintsgroup_id_seq', 1, true);


--
-- Data for Name: ctipresences; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctipresences (id, name, description, deletable) FROM stdin;
1	xivo	De base non supprimable	0
\.


--
-- Name: ctipresences_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctipresences_id_seq', 1, true);


--
-- Data for Name: ctireversedirectories; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctireversedirectories (id, directories) FROM stdin;
1	["xivodir"]
\.


--
-- Name: ctireversedirectories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctireversedirectories_id_seq', 1, true);


--
-- Data for Name: ctisheetactions; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctisheetactions (id, name, description, whom, sheet_info, systray_info, sheet_qtui, action_info, focus, deletable, disable) FROM stdin;
4	XiVO	Modèle de fiche de base.	dest	{"10": [ "Nom","title","","{xivo-calleridname}",0 ],"20": [ "Numéro","text","","{xivo-calleridnum}",0 ],"30": [ "Origine","text","","{xivo-origin}",0 ]}	{"10": [ "Nom","title","","{xivo-calledidname}" ],"20": [ "Numéro","body","","{xivo-calleridnum}" ],"30": [ "Origine","body","","{xivo-origin}" ]}		{}	0	1	1
1	dial	sheet_action_dial	dest	{}	{}		{}	0	1	0
3	custom1	sheet_action_custom1	all	{}	{}		{}	0	1	0
2	queue	sheet_action_queue	dest	{}	{}	file:///etc/xivo/ctiservers/form.ui	{}	0	1	0
\.


--
-- Name: ctisheetactions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctisheetactions_id_seq', 4, true);


--
-- Data for Name: ctisheetevents; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctisheetevents (id, incomingdid, dial, link, unlink, hangup) FROM stdin;
1		dial			\N
\.


--
-- Name: ctisheetevents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctisheetevents_id_seq', 1, true);


--
-- Data for Name: ctistatus; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ctistatus (id, presence_id, name, display_name, actions, color, access_status, deletable) FROM stdin;
1	1	available	Disponible	enablednd(false)	#08FD20	1,2,3,4,5	0
4	1	donotdisturb	Ne pas déranger	enablednd(true)	#FF032D	1,2,3,4,5	1
2	1	away	Sorti	enablednd(false)	#FDE50A	1,2,3,4,5	1
3	1	outtolunch	Parti Manger	enablednd(false)	#001AFF	1,2,3,4,5	1
5	1	berightback	Bientôt de retour	enablednd(false)	#FFB545	1,2,3,4,5	1
6	1	disconnected	Déconnecté	agentlogoff()	#202020		0
\.


--
-- Name: ctistatus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ctistatus_id_seq', 6, true);


--
-- Data for Name: dhcp; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY dhcp (id, active, pool_start, pool_end, extra_ifaces) FROM stdin;
1	0			
\.


--
-- Name: dhcp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('dhcp_id_seq', 2, true);


--
-- Data for Name: dialaction; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY dialaction (category, categoryval, action, actionarg1, actionarg2, linked, event) FROM stdin;
\.


--
-- Data for Name: dialpattern; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY dialpattern (id, type, typeid, externprefix, prefix, exten, stripnum, callerid) FROM stdin;
\.


--
-- Name: dialpattern_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('dialpattern_id_seq', 1, false);


--
-- Data for Name: directories; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY directories (id, uri, dirtype, name, tablename, description) FROM stdin;
1	internal	\N	internal		XiVO internal users
2	phonebook	\N	phonebook		XiVO phonebook
\.


--
-- Name: directories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('directories_id_seq', 3, true);


--
-- Data for Name: entity; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY entity (id, name, displayname, phonenumber, faxnumber, email, url, address1, address2, city, state, zipcode, country, disable, dcreate, description) FROM stdin;
1													0	0	simulate wizard passed
\.


--
-- Name: entity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('entity_id_seq', 2, false);


--
-- Data for Name: extensions; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY extensions (id, commented, context, exten, type, typeval) FROM stdin;
2	1	xivo-features	_*31.	extenfeatures	agentstaticlogin
3	1	xivo-features	_*32.	extenfeatures	agentstaticlogoff
4	1	xivo-features	_*30.	extenfeatures	agentstaticlogtoggle
5	0	xivo-features	_*37.	extenfeatures	bsfilter
6	0	xivo-features	_*664.	extenfeatures	callgroup
7	1	xivo-features	*34	extenfeatures	calllistening
8	0	xivo-features	_*667.	extenfeatures	callmeetme
9	0	xivo-features	_*665.	extenfeatures	callqueue
10	1	xivo-features	*26	extenfeatures	callrecord
11	0	xivo-features	_*666.	extenfeatures	calluser
12	0	xivo-features	*36	extenfeatures	directoryaccess
13	0	xivo-features	*25	extenfeatures	enablednd
14	0	xivo-features	*90	extenfeatures	enablevm
17	0	xivo-features	_*90.	extenfeatures	enablevmslt
18	0	xivo-features	_*23.	extenfeatures	fwdbusy
19	0	xivo-features	_*22.	extenfeatures	fwdrna
20	0	xivo-features	_*21.	extenfeatures	fwdunc
21	0	xivo-features	*20	extenfeatures	fwdundoall
25	0	xivo-features	*48378	extenfeatures	autoprov
26	0	xivo-features	*27	extenfeatures	incallfilter
27	0	xivo-features	*10	extenfeatures	phonestatus
28	0	xivo-features	_*735.	extenfeatures	phoneprogfunckey
29	0	xivo-features	_*8.	extenfeatures	pickup
33	0	xivo-features	*9	extenfeatures	recsnd
34	0	xivo-features	_*99.	extenfeatures	vmboxmsgslt
35	1	xivo-features	_*93.	extenfeatures	vmboxpurgeslt
37	0	xivo-features	*98	extenfeatures	vmusermsg
36	0	xivo-features	_*97.	extenfeatures	vmboxslt
38	1	xivo-features	*92	extenfeatures	vmuserpurge
39	1	xivo-features	_*92.	extenfeatures	vmuserpurgeslt
40	0	xivo-features	_*96.	extenfeatures	vmuserslt
41	0	xivo-features	_*11.	extenfeatures	paging
\.


--
-- Name: extensions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('extensions_id_seq', 43, true);


--
-- Data for Name: features; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY features (id, cat_metric, var_metric, commented, filename, category, var_name, var_val) FROM stdin;
1	0	0	0	features.conf	general	parkext	700
2	0	0	0	features.conf	general	parkpos	701-750
3	0	0	0	features.conf	general	context	parkedcalls
4	0	0	0	features.conf	general	parkinghints	no
5	0	0	0	features.conf	general	parkingtime	45
6	0	0	0	features.conf	general	comebacktoorigin	no
7	0	0	1	features.conf	general	courtesytone	\N
8	0	0	0	features.conf	general	parkedplay	caller
9	0	0	0	features.conf	general	parkedcalltransfers	no
10	0	0	0	features.conf	general	parkedcallreparking	no
11	0	0	0	features.conf	general	parkedcallhangup	no
12	0	0	0	features.conf	general	parkedcallrecording	no
13	0	0	0	features.conf	general	parkeddynamic	no
14	0	0	0	features.conf	general	adsipark	no
15	0	0	0	features.conf	general	findslot	next
16	0	0	0	features.conf	general	parkedmusicclass	default
18	0	0	1	features.conf	general	xfersound	\N
19	0	0	1	features.conf	general	xferfailsound	\N
20	0	0	0	features.conf	general	pickupexten	*8
24	0	0	0	features.conf	general	atxfernoanswertimeout	15
25	0	0	0	features.conf	general	atxferdropcall	no
26	0	0	0	features.conf	general	atxferloopdelay	10
27	0	0	0	features.conf	general	atxfercallbackretries	2
28	1	0	0	features.conf	featuremap	blindxfer	#1
29	1	0	0	features.conf	featuremap	disconnect	*0
30	1	0	0	features.conf	featuremap	automon	*1
31	1	0	0	features.conf	featuremap	atxfer	*2
32	1	0	0	features.conf	featuremap	parkcall	#72
17	0	0	1	features.conf	general	transferdigittimeout	5
23	0	0	1	features.conf	general	featuredigittimeout	1500
\.


--
-- Name: features_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('features_id_seq', 33, true);


--
-- Data for Name: func_key; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key (id, type_id, destination_type_id) FROM stdin;
\.


--
-- Data for Name: func_key_dest_conference; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_dest_conference (func_key_id, destination_type_id, conference_id) FROM stdin;
\.


--
-- Data for Name: func_key_dest_group; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_dest_group (func_key_id, destination_type_id, group_id) FROM stdin;
\.


--
-- Data for Name: func_key_dest_queue; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_dest_queue (func_key_id, destination_type_id, queue_id) FROM stdin;
\.


--
-- Data for Name: func_key_dest_user; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_dest_user (func_key_id, user_id, destination_type_id) FROM stdin;
\.


--
-- Data for Name: func_key_destination_type; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_destination_type (id, name) FROM stdin;
1	user
2	group
3	queue
4	conference
\.


--
-- Name: func_key_destination_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('func_key_destination_type_id_seq', 1, false);


--
-- Name: func_key_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('func_key_id_seq', 1, false);


--
-- Data for Name: func_key_mapping; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_mapping (template_id, func_key_id, destination_type_id, label, "position", blf) FROM stdin;
\.


--
-- Data for Name: func_key_template; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_template (id, name, private) FROM stdin;
\.


--
-- Name: func_key_template_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('func_key_template_id_seq', 1, false);


--
-- Data for Name: func_key_type; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY func_key_type (id, name) FROM stdin;
1	speeddial
\.


--
-- Name: func_key_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('func_key_type_id_seq', 1, true);


--
-- Data for Name: general; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY general (id, timezone, exchange_trunkid, exchange_exten, dundi) FROM stdin;
1	Europe/Paris	\N	\N	0
\.


--
-- Name: general_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('general_id_seq', 1, true);


--
-- Data for Name: groupfeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY groupfeatures (id, name, number, context, transfer_user, transfer_call, write_caller, write_calling, timeout, preprocess_subroutine, deleted) FROM stdin;
\.


--
-- Name: groupfeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('groupfeatures_id_seq', 1, false);


--
-- Data for Name: iaxcallnumberlimits; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY iaxcallnumberlimits (id, destination, netmask, calllimits) FROM stdin;
\.


--
-- Name: iaxcallnumberlimits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('iaxcallnumberlimits_id_seq', 1, false);


--
-- Data for Name: incall; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY incall (id, exten, context, preprocess_subroutine, commented, description) FROM stdin;
\.


--
-- Name: incall_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('incall_id_seq', 1, false);


--
-- Data for Name: ldapfilter; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ldapfilter (id, ldapserverid, name, "user", passwd, basedn, filter, attrdisplayname, attrphonenumber, additionaltype, additionaltext, commented, description) FROM stdin;
\.


--
-- Name: ldapfilter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ldapfilter_id_seq', 1, false);


--
-- Data for Name: ldapserver; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY ldapserver (id, name, host, port, securitylayer, protocolversion, disable, dcreate, description) FROM stdin;
\.


--
-- Name: ldapserver_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('ldapserver_id_seq', 1, false);


--
-- Data for Name: linefeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY linefeatures (id, protocolid, device, configregistrar, name, number, context, provisioningid, num, ipfrom, commented, description, protocol) FROM stdin;
\.


--
-- Name: linefeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('linefeatures_id_seq', 1, false);


--
-- Data for Name: mail; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY mail (id, mydomain, origin, relayhost, fallback_relayhost, canonical) FROM stdin;
1		xivo-clients.proformatique.com			
\.


--
-- Name: mail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('mail_id_seq', 2, true);


--
-- Data for Name: meetmefeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY meetmefeatures (id, meetmeid, name, confno, context, admin_typefrom, admin_internalid, admin_externalid, admin_identification, admin_mode, admin_announceusercount, admin_announcejoinleave, admin_moderationmode, admin_initiallymuted, admin_musiconhold, admin_poundexit, admin_quiet, admin_starmenu, admin_closeconflastmarkedexit, admin_enableexitcontext, admin_exitcontext, user_mode, user_announceusercount, user_hiddencalls, user_announcejoinleave, user_initiallymuted, user_musiconhold, user_poundexit, user_quiet, user_starmenu, user_enableexitcontext, user_exitcontext, talkeroptimization, record, talkerdetection, noplaymsgfirstenter, durationm, closeconfdurationexceeded, nbuserstartdeductduration, timeannounceclose, maxusers, startdate, emailfrom, emailfromname, emailsubject, emailbody, preprocess_subroutine, description, commented) FROM stdin;
\.


--
-- Name: meetmefeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('meetmefeatures_id_seq', 1, false);


--
-- Data for Name: meetmeguest; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY meetmeguest (id, meetmefeaturesid, fullname, telephonenumber, email) FROM stdin;
\.


--
-- Name: meetmeguest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('meetmeguest_id_seq', 1, false);


--
-- Data for Name: monitoring; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY monitoring (id, maintenance, alert_emails, dahdi_monitor_ports, max_call_duration) FROM stdin;
1	0	\N	\N	\N
\.


--
-- Name: monitoring_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('monitoring_id_seq', 2, true);


--
-- Data for Name: musiconhold; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY musiconhold (id, cat_metric, var_metric, commented, filename, category, var_name, var_val) FROM stdin;
1	0	0	0	musiconhold.conf	default	mode	files
2	0	0	1	musiconhold.conf	default	application	
3	0	0	0	musiconhold.conf	default	random	no
4	0	0	0	musiconhold.conf	default	directory	/var/lib/xivo/moh/default
\.


--
-- Name: musiconhold_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('musiconhold_id_seq', 4, true);


--
-- Data for Name: netiface; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY netiface (id, ifname, hwtypeid, networktype, type, family, address, netmask, broadcast, gateway, mtu, vlanrawdevice, vlanid, options, disable, dcreate, description, method) FROM stdin;
\.


--
-- Name: netiface_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('netiface_id_seq', 1, false);


--
-- Data for Name: outcall; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY outcall (id, name, context, useenum, internal, preprocess_subroutine, hangupringtime, commented, description) FROM stdin;
\.


--
-- Name: outcall_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('outcall_id_seq', 1, false);


--
-- Data for Name: outcalltrunk; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY outcalltrunk (outcallid, trunkfeaturesid, priority) FROM stdin;
\.


--
-- Data for Name: paging; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY paging (id, number, duplex, ignore, record, quiet, timeout, announcement_file, announcement_play, announcement_caller, commented, description) FROM stdin;
\.


--
-- Name: paging_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('paging_id_seq', 1, false);


--
-- Data for Name: paginguser; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY paginguser (pagingid, userfeaturesid, caller) FROM stdin;
\.


--
-- Data for Name: phonebook; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY phonebook (id, title, firstname, lastname, displayname, society, email, url, image, description) FROM stdin;
\.


--
-- Name: phonebook_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('phonebook_id_seq', 1, false);


--
-- Data for Name: phonebookaddress; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY phonebookaddress (id, phonebookid, address1, address2, city, state, zipcode, country, type) FROM stdin;
\.


--
-- Name: phonebookaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('phonebookaddress_id_seq', 1, false);


--
-- Data for Name: phonebooknumber; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY phonebooknumber (id, phonebookid, number, type) FROM stdin;
\.


--
-- Name: phonebooknumber_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('phonebooknumber_id_seq', 1, false);


--
-- Data for Name: phonefunckey; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY phonefunckey (iduserfeatures, fknum, exten, typeextenumbers, typevalextenumbers, typevalextenumbersright, label, supervision, progfunckey, typeextenumbersright) FROM stdin;
\.


--
-- Data for Name: pickup; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY pickup (id, name, commented, description) FROM stdin;
\.


--
-- Data for Name: pickupmember; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY pickupmember (pickupid, category, membertype, memberid) FROM stdin;
\.


--
-- Data for Name: provisioning; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY provisioning (id, net4_ip, net4_ip_rest, username, password, dhcp_integration, rest_port, http_port, private, secure) FROM stdin;
1		127.0.0.1	admin	admin	0	8666	8667	0	0
\.


--
-- Name: provisioning_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('provisioning_id_seq', 2, true);


--
-- Data for Name: queue; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queue (name, musicclass, announce, context, timeout, "monitor-type", "monitor-format", "queue-youarenext", "queue-thereare", "queue-callswaiting", "queue-holdtime", "queue-minutes", "queue-seconds", "queue-thankyou", "queue-reporthold", "periodic-announce", "announce-frequency", "periodic-announce-frequency", "announce-round-seconds", "announce-holdtime", retry, wrapuptime, maxlen, servicelevel, strategy, joinempty, leavewhenempty, eventmemberstatus, eventwhencalled, ringinuse, reportholdtime, memberdelay, weight, timeoutrestart, commented, category, timeoutpriority, autofill, autopause, setinterfacevar, setqueueentryvar, setqueuevar, membermacro, "min-announce-frequency", "random-periodic-announce", "announce-position", "announce-position-limit", defaultrule) FROM stdin;
\.


--
-- Data for Name: queue_info; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queue_info (id, call_time_t, queue_name, caller, caller_uniqueid, call_picker, hold_time, talk_time) FROM stdin;
\.


--
-- Name: queue_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('queue_info_id_seq', 1, false);


--
-- Data for Name: queue_log; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queue_log ("time", callid, queuename, agent, event, data1, data2, data3, data4, data5, id) FROM stdin;
\.


--
-- Name: queue_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('queue_log_id_seq', 1, false);


--
-- Data for Name: queuefeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queuefeatures (id, name, displayname, number, context, data_quality, hitting_callee, hitting_caller, retries, ring, transfer_user, transfer_call, write_caller, write_calling, url, announceoverride, timeout, preprocess_subroutine, announce_holdtime, waittime, waitratio) FROM stdin;
\.


--
-- Name: queuefeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('queuefeatures_id_seq', 1, false);


--
-- Data for Name: queuemember; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queuemember (queue_name, interface, penalty, commented, usertype, userid, channel, category, "position") FROM stdin;
\.


--
-- Data for Name: queuepenalty; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queuepenalty (id, name, commented, description) FROM stdin;
\.


--
-- Name: queuepenalty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('queuepenalty_id_seq', 1, false);


--
-- Data for Name: queuepenaltychange; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queuepenaltychange (queuepenalty_id, seconds, maxp_sign, maxp_value, minp_sign, minp_value) FROM stdin;
\.


--
-- Data for Name: queueskill; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queueskill (id, catid, name, description, printscreen) FROM stdin;
\.


--
-- Name: queueskill_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('queueskill_id_seq', 1, false);


--
-- Data for Name: queueskillcat; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queueskillcat (id, name) FROM stdin;
\.


--
-- Name: queueskillcat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('queueskillcat_id_seq', 1, false);


--
-- Data for Name: queueskillrule; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY queueskillrule (id, name, rule) FROM stdin;
\.


--
-- Name: queueskillrule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('queueskillrule_id_seq', 1, false);


--
-- Data for Name: record_campaign; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY record_campaign (id, campaign_name, activated, base_filename, queue_id, start_date, end_date) FROM stdin;
\.


--
-- Name: record_campaign_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('record_campaign_id_seq', 1, false);


--
-- Data for Name: recording; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY recording (cid, start_time, end_time, caller, client_id, callee, filename, campaign_id, agent_id) FROM stdin;
\.


--
-- Data for Name: resolvconf; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY resolvconf (id, hostname, domain, nameserver1, nameserver2, nameserver3, search, description) FROM stdin;
1			\N	\N	\N	\N	
\.


--
-- Name: resolvconf_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('resolvconf_id_seq', 2, true);


--
-- Data for Name: rightcall; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY rightcall (id, name, passwd, "authorization", commented, description) FROM stdin;
\.


--
-- Name: rightcall_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('rightcall_id_seq', 1, false);


--
-- Data for Name: rightcallexten; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY rightcallexten (id, rightcallid, exten) FROM stdin;
\.


--
-- Name: rightcallexten_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('rightcallexten_id_seq', 1, false);


--
-- Data for Name: rightcallmember; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY rightcallmember (id, rightcallid, type, typeval) FROM stdin;
\.


--
-- Name: rightcallmember_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('rightcallmember_id_seq', 1, false);


--
-- Data for Name: sccpdevice; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY sccpdevice (id, name, device, line, voicemail) FROM stdin;
\.


--
-- Name: sccpdevice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('sccpdevice_id_seq', 1, false);


--
-- Data for Name: sccpgeneralsettings; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY sccpgeneralsettings (id, option_name, option_value) FROM stdin;
1	directmedia	no
2	dialtimeout	5
3	language	en_US
4	allow	
5	keepalive	10
\.


--
-- Name: sccpgeneralsettings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('sccpgeneralsettings_id_seq', 5, true);


--
-- Data for Name: sccpline; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY sccpline (id, name, cid_name, cid_num, context, commented, protocol, disallow, allow) FROM stdin;
\.


--
-- Name: sccpline_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('sccpline_id_seq', 1, false);


--
-- Data for Name: schedule; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY schedule (id, name, timezone, fallback_action, fallback_actionid, fallback_actionargs, description, commented) FROM stdin;
\.


--
-- Name: schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('schedule_id_seq', 1, false);


--
-- Data for Name: schedule_path; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY schedule_path (schedule_id, path, pathid, "order") FROM stdin;
\.


--
-- Data for Name: schedule_time; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY schedule_time (id, schedule_id, mode, hours, weekdays, monthdays, months, action, actionid, actionargs, commented) FROM stdin;
\.


--
-- Name: schedule_time_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('schedule_time_id_seq', 1, false);


--
-- Data for Name: serverfeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY serverfeatures (id, serverid, type, commented, feature) FROM stdin;
\.


--
-- Name: serverfeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('serverfeatures_id_seq', 1, false);


--
-- Data for Name: session; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY session (sessid, start, expire, identifier, data) FROM stdin;
\.


--
-- Data for Name: sipauthentication; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY sipauthentication (id, usersip_id, "user", secretmode, secret, realm) FROM stdin;
\.


--
-- Name: sipauthentication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('sipauthentication_id_seq', 1, false);


--
-- Data for Name: stat_agent; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stat_agent (id, name) FROM stdin;
\.


--
-- Name: stat_agent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('stat_agent_id_seq', 1, false);


--
-- Data for Name: stat_agent_periodic; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stat_agent_periodic (id, "time", login_time, agent_id, pause_time, wrapup_time) FROM stdin;
\.


--
-- Name: stat_agent_periodic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('stat_agent_periodic_id_seq', 1, false);


--
-- Data for Name: stat_call_on_queue; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stat_call_on_queue (id, callid, "time", ringtime, talktime, waittime, queue_id, agent_id, status) FROM stdin;
\.


--
-- Name: stat_call_on_queue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('stat_call_on_queue_id_seq', 1, false);


--
-- Data for Name: stat_queue; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stat_queue (id, name) FROM stdin;
\.


--
-- Name: stat_queue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('stat_queue_id_seq', 1, false);


--
-- Data for Name: stat_queue_periodic; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stat_queue_periodic (id, "time", answered, abandoned, total, "full", closed, joinempty, leaveempty, timeout, queue_id, divert_ca_ratio, divert_waittime) FROM stdin;
\.


--
-- Name: stat_queue_periodic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('stat_queue_periodic_id_seq', 1, false);


--
-- Data for Name: staticiax; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY staticiax (id, cat_metric, var_metric, commented, filename, category, var_name, var_val) FROM stdin;
1	0	0	0	iax.conf	general	bindport	4569
2	0	0	0	iax.conf	general	bindaddr	0.0.0.0
3	0	0	0	iax.conf	general	iaxthreadcount	10
4	0	0	0	iax.conf	general	iaxmaxthreadcount	100
5	0	0	0	iax.conf	general	iaxcompat	no
6	0	0	0	iax.conf	general	authdebug	yes
7	0	0	0	iax.conf	general	delayreject	no
8	0	0	0	iax.conf	general	trunkfreq	20
9	0	0	0	iax.conf	general	trunktimestamps	yes
10	0	0	1	iax.conf	general	regcontext	\N
11	0	0	0	iax.conf	general	minregexpire	60
12	0	0	0	iax.conf	general	maxregexpire	60
13	0	0	0	iax.conf	general	bandwidth	high
14	0	0	1	iax.conf	general	tos	\N
15	0	0	0	iax.conf	general	jitterbuffer	no
16	0	0	0	iax.conf	general	forcejitterbuffer	no
17	0	0	0	iax.conf	general	maxjitterbuffer	1000
18	0	0	0	iax.conf	general	maxjitterinterps	10
19	0	0	0	iax.conf	general	resyncthreshold	1000
20	0	0	1	iax.conf	general	accountcode	\N
21	0	0	0	iax.conf	general	amaflags	default
22	0	0	0	iax.conf	general	adsi	no
23	0	0	0	iax.conf	general	transfer	yes
24	0	0	0	iax.conf	general	language	fr_FR
25	0	0	0	iax.conf	general	mohinterpret	default
26	0	0	1	iax.conf	general	mohsuggest	\N
27	0	0	0	iax.conf	general	encryption	no
28	0	0	0	iax.conf	general	maxauthreq	3
29	0	0	0	iax.conf	general	codecpriority	host
30	0	0	1	iax.conf	general	disallow	\N
31	0	0	1	iax.conf	general	allow	\N
32	0	0	0	iax.conf	general	rtcachefriends	yes
33	0	0	0	iax.conf	general	rtupdate	yes
34	0	0	0	iax.conf	general	rtignoreregexpire	yes
35	0	0	0	iax.conf	general	rtautoclear	no
36	0	0	0	iax.conf	general	pingtime	20
37	0	0	0	iax.conf	general	lagrqtime	10
38	0	0	0	iax.conf	general	nochecksums	no
39	0	0	0	iax.conf	general	autokill	yes
40	0	0	0	iax.conf	general	calltokenoptional	0.0.0.0
41	0	0	0	iax.conf	general	srvlookup	\N
42	0	0	0	iax.conf	general	jittertargetextra	\N
43	0	0	0	iax.conf	general	forceencryption	\N
44	0	0	0	iax.conf	general	trunkmaxsize	\N
45	0	0	0	iax.conf	general	trunkmtu	\N
46	0	0	0	iax.conf	general	cos	\N
47	0	0	0	iax.conf	general	allowfwdownload	\N
48	0	0	0	iax.conf	general	parkinglot	\N
49	0	0	0	iax.conf	general	maxcallnumbers	\N
50	0	0	0	iax.conf	general	maxcallnumbers_nonvalidated	\N
51	0	0	0	iax.conf	general	shrinkcallerid	\N
\.


--
-- Name: staticiax_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('staticiax_id_seq', 51, true);


--
-- Data for Name: staticmeetme; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY staticmeetme (id, cat_metric, var_metric, commented, filename, category, var_name, var_val) FROM stdin;
1	0	0	0	meetme.conf	general	audiobuffers	32
2	0	0	0	meetme.conf	general	schedule	yes
3	0	0	0	meetme.conf	general	logmembercount	yes
4	0	0	0	meetme.conf	general	fuzzystart	300
5	0	0	0	meetme.conf	general	earlyalert	3600
6	0	0	0	meetme.conf	general	endalert	120
\.


--
-- Name: staticmeetme_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('staticmeetme_id_seq', 6, true);


--
-- Data for Name: staticqueue; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY staticqueue (id, cat_metric, var_metric, commented, filename, category, var_name, var_val) FROM stdin;
1	0	0	0	queues.conf	general	persistentmembers	yes
2	0	0	0	queues.conf	general	autofill	no
3	0	0	0	queues.conf	general	monitor-type	no
4	0	0	0	queues.conf	general	updatecdr	no
5	0	0	0	queues.conf	general	shared_lastcall	no
\.


--
-- Name: staticqueue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('staticqueue_id_seq', 5, true);


--
-- Data for Name: staticsip; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY staticsip (id, cat_metric, var_metric, commented, filename, category, var_name, var_val) FROM stdin;
1	0	0	0	sip.conf	general	bindport	5060
3	0	0	0	sip.conf	general	autocreate_context	xivo-initconfig
8	0	0	0	sip.conf	general	autocreate_type	friend
10	0	0	0	sip.conf	general	allowsubscribe	yes
11	0	0	0	sip.conf	general	allowoverlap	yes
12	0	0	0	sip.conf	general	promiscredir	no
13	0	0	0	sip.conf	general	autodomain	no
14	0	0	1	sip.conf	general	domain	\N
15	0	0	0	sip.conf	general	allowexternaldomains	yes
16	0	0	0	sip.conf	general	usereqphone	no
17	0	0	0	sip.conf	general	realm	xivo
18	0	0	0	sip.conf	general	alwaysauthreject	no
19	0	0	0	sip.conf	general	useragent	XiVO PBX
20	0	0	0	sip.conf	general	buggymwi	no
21	0	0	1	sip.conf	general	regcontext	\N
22	0	0	0	sip.conf	general	callerid	xivo
23	0	0	1	sip.conf	general	fromdomain	\N
24	0	0	0	sip.conf	general	sipdebug	no
25	0	0	0	sip.conf	general	dumphistory	no
26	0	0	0	sip.conf	general	recordhistory	no
27	0	0	0	sip.conf	general	callevents	yes
28	0	0	1	sip.conf	general	tos_sip	\N
29	0	0	1	sip.conf	general	tos_audio	\N
30	0	0	1	sip.conf	general	tos_video	\N
31	0	0	0	sip.conf	general	t38pt_udptl	no
32	0	0	0	sip.conf	general	t38pt_usertpsource	no
33	0	0	1	sip.conf	general	localnet	\N
34	0	0	1	sip.conf	general	externip	\N
35	0	0	1	sip.conf	general	externhost	\N
36	0	0	0	sip.conf	general	externrefresh	10
37	0	0	0	sip.conf	general	matchexterniplocally	no
38	0	0	1	sip.conf	general	outboundproxy	\N
39	0	0	0	sip.conf	general	g726nonstandard	no
40	0	0	1	sip.conf	general	disallow	\N
41	0	0	1	sip.conf	general	allow	\N
42	0	0	0	sip.conf	general	t1min	100
43	0	0	0	sip.conf	general	relaxdtmf	no
44	0	0	0	sip.conf	general	rfc2833compensate	no
45	0	0	0	sip.conf	general	compactheaders	no
46	0	0	0	sip.conf	general	rtptimeout	0
47	0	0	0	sip.conf	general	rtpholdtimeout	0
48	0	0	0	sip.conf	general	rtpkeepalive	0
49	0	0	0	sip.conf	general	directrtpsetup	no
50	0	0	0	sip.conf	general	notifymimetype	application/simple-message-summary
51	0	0	0	sip.conf	general	srvlookup	no
52	0	0	0	sip.conf	general	pedantic	no
53	0	0	0	sip.conf	general	minexpiry	60
54	0	0	0	sip.conf	general	maxexpiry	3600
55	0	0	0	sip.conf	general	defaultexpiry	120
56	0	0	0	sip.conf	general	registertimeout	20
57	0	0	0	sip.conf	general	registerattempts	0
58	0	0	0	sip.conf	general	notifyringing	yes
59	0	0	0	sip.conf	general	notifyhold	no
60	0	0	0	sip.conf	general	allowtransfer	yes
61	0	0	0	sip.conf	general	maxcallbitrate	384
62	0	0	0	sip.conf	general	autoframing	yes
63	0	0	0	sip.conf	general	jbenable	no
64	0	0	0	sip.conf	general	jbforce	no
65	0	0	0	sip.conf	general	jbmaxsize	200
66	0	0	0	sip.conf	general	jbresyncthreshold	1000
67	0	0	0	sip.conf	general	jbimpl	fixed
68	0	0	0	sip.conf	general	jblog	no
69	0	0	1	sip.conf	general	context	\N
70	0	0	0	sip.conf	general	nat	no
71	0	0	0	sip.conf	general	dtmfmode	info
72	0	0	0	sip.conf	general	qualify	no
73	0	0	0	sip.conf	general	useclientcode	no
74	0	0	0	sip.conf	general	progressinband	never
75	0	0	0	sip.conf	general	language	fr_FR
76	0	0	0	sip.conf	general	mohinterpret	default
77	0	0	1	sip.conf	general	mohsuggest	\N
78	0	0	0	sip.conf	general	vmexten	*98
79	0	0	0	sip.conf	general	trustrpid	no
80	0	0	0	sip.conf	general	sendrpid	no
81	0	0	0	sip.conf	general	insecure	no
82	0	0	0	sip.conf	general	rtcachefriends	no
83	0	0	0	sip.conf	general	rtupdate	no
84	0	0	0	sip.conf	general	ignoreregexpire	no
85	0	0	0	sip.conf	general	rtsavesysname	no
86	0	0	0	sip.conf	general	rtautoclear	no
87	0	0	1	sip.conf	general	subscribecontext	\N
88	0	0	0	sip.conf	general	match_auth_username	no
89	0	0	0	sip.conf	general	udpbindaddr	0.0.0.0
90	0	0	0	sip.conf	general	tcpenable	no
91	0	0	0	sip.conf	general	tcpbindaddr	\N
92	0	0	0	sip.conf	general	tlsenable	no
93	0	0	0	sip.conf	general	tlsbindaddr	\N
94	0	0	0	sip.conf	general	tlscertfile	\N
95	0	0	0	sip.conf	general	tlscafile	\N
96	0	0	0	sip.conf	general	tlscadir	/var/lib/asterisk/certs/cadir
97	0	0	0	sip.conf	general	tlsdontverifyserver	no
98	0	0	0	sip.conf	general	tlscipher	\N
99	0	0	0	sip.conf	general	tos_text	\N
100	0	0	0	sip.conf	general	cos_sip	\N
101	0	0	0	sip.conf	general	cos_audio	\N
2	0	0	0	sip.conf	general	autocreatepeer	persist
102	0	0	0	sip.conf	general	cos_video	\N
103	0	0	0	sip.conf	general	cos_text	\N
104	0	0	0	sip.conf	general	mwiexpiry	3600
105	0	0	0	sip.conf	general	qualifyfreq	60
106	0	0	0	sip.conf	general	qualifygap	100
107	0	0	0	sip.conf	general	qualifypeers	1
108	0	0	0	sip.conf	general	parkinglot	\N
109	0	0	0	sip.conf	general	permaturemedia	\N
110	0	0	0	sip.conf	general	sdpsession	\N
111	0	0	0	sip.conf	general	sdpowner	\N
112	0	0	0	sip.conf	general	authfailureevents	no
113	0	0	0	sip.conf	general	dynamic_exclude_static	no
114	0	0	0	sip.conf	general	contactdeny	\N
115	0	0	0	sip.conf	general	contactpermit	\N
116	0	0	0	sip.conf	general	shrinkcallerid	yes
117	0	0	0	sip.conf	general	regextenonqualify	no
118	0	0	0	sip.conf	general	timer1	500
119	0	0	0	sip.conf	general	timerb	32000
120	0	0	0	sip.conf	general	session-timers	\N
121	0	0	0	sip.conf	general	session-expires	600
122	0	0	0	sip.conf	general	session-minse	90
123	0	0	0	sip.conf	general	session-refresher	uas
124	0	0	0	sip.conf	general	hash_users	\N
125	0	0	0	sip.conf	general	hash_peers	\N
126	0	0	0	sip.conf	general	hash_dialogs	\N
127	0	0	0	sip.conf	general	notifycid	no
128	0	0	0	sip.conf	general	callcounter	no
130	0	0	0	sip.conf	general	stunaddr	\N
131	0	0	0	sip.conf	general	directmedia	yes
132	0	0	0	sip.conf	general	ignoresdpversion	no
133	0	0	0	sip.conf	general	jbtargetextra	\N
135	0	0	0	sip.conf	general	externtcpport	\N
136	0	0	0	sip.conf	general	externtlsport	\N
137	0	0	0	sip.conf	general	media_address	\N
138	0	0	0	sip.conf	general	use_q850_reason	no
139	0	0	0	sip.conf	general	snom_aoc_enabled	no
140	0	0	0	sip.conf	general	subscribe_network_change_event	yes
141	0	0	0	sip.conf	general	maxforwards	\N
142	0	0	0	sip.conf	general	disallowed_methods	\N
143	0	0	0	sip.conf	general	domainsasrealm	\N
144	0	0	0	sip.conf	general	textsupport	\N
145	0	0	0	sip.conf	general	videosupport	\N
146	0	0	0	sip.conf	general	auth_options_requests	no
147	0	0	0	sip.conf	general	transport	udp
148	0	0	0	sip.conf	general	allowguest	no
134	0	0	0	sip.conf	general	encryption	no
\.


--
-- Name: staticsip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('staticsip_id_seq', 148, true);


--
-- Data for Name: staticvoicemail; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY staticvoicemail (id, cat_metric, var_metric, commented, filename, category, var_name, var_val) FROM stdin;
1	0	0	0	voicemail.conf	general	maxmsg	100
2	0	0	0	voicemail.conf	general	silencethreshold	256
3	0	0	0	voicemail.conf	general	minsecs	0
4	0	0	0	voicemail.conf	general	maxsecs	0
5	0	0	0	voicemail.conf	general	maxsilence	15
6	0	0	0	voicemail.conf	general	review	yes
7	0	0	0	voicemail.conf	general	operator	yes
8	0	0	0	voicemail.conf	general	format	wav
9	0	0	0	voicemail.conf	general	maxlogins	3
10	0	0	0	voicemail.conf	general	envelope	yes
11	0	0	0	voicemail.conf	general	saycid	no
12	0	0	1	voicemail.conf	general	cidinternalcontexts	\N
13	0	0	0	voicemail.conf	general	sayduration	yes
14	0	0	0	voicemail.conf	general	saydurationm	2
15	0	0	0	voicemail.conf	general	forcename	no
16	0	0	0	voicemail.conf	general	forcegreetings	no
17	0	0	0	voicemail.conf	general	tempgreetwarn	yes
18	0	0	0	voicemail.conf	general	maxgreet	0
19	0	0	0	voicemail.conf	general	skipms	3000
20	0	0	0	voicemail.conf	general	sendvoicemail	no
21	0	0	0	voicemail.conf	general	usedirectory	yes
22	0	0	0	voicemail.conf	general	nextaftercmd	yes
23	0	0	1	voicemail.conf	general	dialout	\N
24	0	0	1	voicemail.conf	general	callback	\N
25	0	0	1	voicemail.conf	general	exitcontext	\N
26	0	0	0	voicemail.conf	general	attach	yes
27	0	0	0	voicemail.conf	general	volgain	0
28	0	0	0	voicemail.conf	general	mailcmd	/usr/sbin/sendmail -t
29	0	0	0	voicemail.conf	general	serveremail	xivo
30	0	0	0	voicemail.conf	general	charset	UTF-8
31	0	0	0	voicemail.conf	general	fromstring	XiVO PBX
33	0	0	0	voicemail.conf	general	pbxskip	no
34	0	0	0	voicemail.conf	general	emailsubject	Messagerie XiVO
35	0	0	0	voicemail.conf	general	emailbody	Bonjour ${VM_NAME},\n\nVous avez reçu un message d'une durée de ${VM_DUR} minute(s), il vous reste actuellement ${VM_MSGNUM} message(s) non lu(s) sur votre messagerie vocale : ${VM_MAILBOX}.\n\nLe dernier a été envoyé par ${VM_CALLERID}, le ${VM_DATE}. Si vous le souhaitez vous pouvez l'écouter ou le consulter en tapant le *98 sur votre téléphone.\n\nMerci.\n\n-- Messagerie XiVO --
36	0	0	0	voicemail.conf	general	pagerfromstring	XiVO PBX
37	0	0	1	voicemail.conf	general	pagersubject	\N
38	0	0	1	voicemail.conf	general	pagerbody	\N
39	0	0	0	voicemail.conf	general	adsifdn	0000000F
40	0	0	0	voicemail.conf	general	adsisec	9BDBF7AC
41	0	0	0	voicemail.conf	general	adsiver	1
42	0	0	0	voicemail.conf	general	searchcontexts	no
43	0	0	0	voicemail.conf	general	externpass	/usr/share/asterisk/bin/change-pass-vm
44	0	0	1	voicemail.conf	general	externnotify	\N
45	0	0	1	voicemail.conf	general	smdiport	\N
46	0	0	1	voicemail.conf	general	odbcstorage	\N
47	0	0	1	voicemail.conf	general	odbctable	\N
48	1	0	0	voicemail.conf	zonemessages	eu-fr	Europe/Paris|'vm-received' q 'digits/at' kM
49	0	0	1	voicemail.conf	general	moveheard	\N
50	0	0	1	voicemail.conf	general	forward_urgent_auto	\N
51	0	0	1	voicemail.conf	general	userscontext	\N
52	0	0	1	voicemail.conf	general	smdienable	\N
53	0	0	1	voicemail.conf	general	externpassnotify	\N
54	0	0	1	voicemail.conf	general	externpasscheck	\N
55	0	0	1	voicemail.conf	general	directoryinfo	\N
56	0	0	1	voicemail.conf	general	pollmailboxes	\N
57	0	0	1	voicemail.conf	general	pollfreq	\N
58	0	0	1	voicemail.conf	general	imapgreetings	\N
59	0	0	1	voicemail.conf	general	greetingsfolder	\N
60	0	0	1	voicemail.conf	general	imapparentfolder	\N
61	0	0	1	voicemail.conf	general	tz	\N
62	0	0	1	voicemail.conf	general	hidefromdir	\N
63	0	0	1	voicemail.conf	general	messagewrap	\N
64	0	0	1	voicemail.conf	general	minpassword	\N
65	0	0	1	voicemail.conf	general	vm-password	\N
66	0	0	1	voicemail.conf	general	vm-newpassword	\N
67	0	0	1	voicemail.conf	general	vm-passchanged	\N
68	0	0	1	voicemail.conf	general	vm-reenterpassword	\N
69	0	0	1	voicemail.conf	general	vm-mismatch	\N
70	0	0	1	voicemail.conf	general	vm-invalid-password	\N
71	0	0	1	voicemail.conf	general	vm-pls-try-again	\N
72	0	0	1	voicemail.conf	general	listen-control-forward-key	\N
73	0	0	1	voicemail.conf	general	listen-control-reverse-key	\N
74	0	0	1	voicemail.conf	general	listen-control-pause-key	\N
75	0	0	1	voicemail.conf	general	listen-control-restart-key	\N
76	0	0	1	voicemail.conf	general	listen-control-stop-key	\N
77	0	0	1	voicemail.conf	general	backupdeleted	\N
32	0	0	0	voicemail.conf	general	emaildateformat	%Y-%m-%d à %H:%M:%S
\.


--
-- Name: staticvoicemail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('staticvoicemail_id_seq', 77, true);


--
-- Data for Name: stats_conf; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stats_conf (id, name, hour_start, hour_end, homepage, timezone, default_delta, monday, tuesday, wednesday, thursday, friday, saturday, sunday, period1, period2, period3, period4, period5, dbegcache, dendcache, dgenercache, dcreate, dupdate, disable, description) FROM stdin;
\.


--
-- Data for Name: stats_conf_agent; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stats_conf_agent (stats_conf_id, agentfeatures_id) FROM stdin;
\.


--
-- Data for Name: stats_conf_group; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stats_conf_group (stats_conf_id, groupfeatures_id) FROM stdin;
\.


--
-- Name: stats_conf_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('stats_conf_id_seq', 1, false);


--
-- Data for Name: stats_conf_incall; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stats_conf_incall (stats_conf_id, incall_id) FROM stdin;
\.


--
-- Data for Name: stats_conf_queue; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stats_conf_queue (stats_conf_id, queuefeatures_id, qos) FROM stdin;
\.


--
-- Data for Name: stats_conf_user; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stats_conf_user (stats_conf_id, userfeatures_id) FROM stdin;
\.


--
-- Data for Name: stats_conf_xivouser; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY stats_conf_xivouser (stats_conf_id, user_id) FROM stdin;
\.


--
-- Data for Name: trunkfeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY trunkfeatures (id, protocolid, registerid, registercommented, description, protocol) FROM stdin;
\.


--
-- Name: trunkfeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('trunkfeatures_id_seq', 1, false);


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY "user" (id, login, passwd, meta, valid, "time", dcreate, dupdate, obj, entity_id) FROM stdin;
1	root	proformatique	root	1	0	1409084546	0		\N
\.


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('user_id_seq', 2, true);


--
-- Data for Name: user_line; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY user_line (id, user_id, line_id, extension_id, main_user, main_line) FROM stdin;
\.


--
-- Name: user_line_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('user_line_id_seq', 1, false);


--
-- Data for Name: usercustom; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY usercustom (id, name, context, interface, intfsuffix, commented, category, protocol) FROM stdin;
\.


--
-- Name: usercustom_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('usercustom_id_seq', 1, false);


--
-- Data for Name: userfeatures; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY userfeatures (id, firstname, lastname, voicemailtype, voicemailid, agentid, pictureid, entityid, callerid, ringseconds, simultcalls, enableclient, loginclient, passwdclient, enablehint, enablevoicemail, enablexfer, enableautomon, callrecord, incallfilter, enablednd, enableunc, destunc, enablerna, destrna, enablebusy, destbusy, musiconhold, outcallerid, mobilephonenumber, userfield, bsfilter, preprocess_subroutine, timezone, language, ringintern, ringextern, ringgroup, ringforward, rightcallcode, commented, description, cti_profile_id, func_key_template_id, func_key_private_template_id) FROM stdin;
\.


--
-- Name: userfeatures_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('userfeatures_id_seq', 1, false);


--
-- Data for Name: useriax; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY useriax (id, name, username, secret, dbsecret, context, language, accountcode, amaflags, mailbox, callerid, fullname, cid_number, trunk, auth, encryption, forceencryption, maxauthreq, inkeys, outkey, adsi, transfer, codecpriority, jitterbuffer, forcejitterbuffer, sendani, qualify, qualifysmoothing, qualifyfreqok, qualifyfreqnotok, timezone, disallow, allow, mohinterpret, mohsuggest, deny, permit, defaultip, sourceaddress, setvar, host, port, mask, regexten, peercontext, ipaddr, regseconds, immediate, parkinglot, category, commented, requirecalltoken, type, keyrotate, protocol) FROM stdin;
\.


--
-- Name: useriax_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('useriax_id_seq', 1, false);


--
-- Data for Name: usersip; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY usersip (id, name, username, secret, md5secret, context, language, accountcode, amaflags, allowtransfer, fromuser, fromdomain, mailbox, subscribemwi, buggymwi, "call-limit", callerid, fullname, cid_number, maxcallbitrate, insecure, promiscredir, usereqphone, videosupport, trustrpid, allowsubscribe, allowoverlap, dtmfmode, rfc2833compensate, qualify, g726nonstandard, disallow, allow, autoframing, mohinterpret, mohsuggest, useclientcode, progressinband, t38pt_udptl, t38pt_usertpsource, rtptimeout, rtpholdtimeout, rtpkeepalive, deny, permit, defaultip, setvar, host, port, regexten, subscribecontext, fullcontact, vmexten, callingpres, ipaddr, regseconds, regserver, lastms, parkinglot, category, outboundproxy, transport, remotesecret, directmedia, callcounter, busylevel, ignoresdpversion, "session-timers", "session-expires", "session-minse", "session-refresher", callbackextension, registertrying, timert1, timerb, qualifyfreq, contactpermit, contactdeny, unsolicited_mailbox, use_q850_reason, encryption, snom_aoc_enabled, maxforwards, disallowed_methods, textsupport, commented, type, protocol, sendrpid, nat) FROM stdin;
\.


--
-- Name: usersip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('usersip_id_seq', 1, false);


--
-- Data for Name: voicemail; Type: TABLE DATA; Schema: public; Owner: asterisk
--

COPY voicemail (uniqueid, context, mailbox, password, fullname, email, pager, dialout, callback, exitcontext, language, tz, attach, saycid, review, operator, envelope, sayduration, saydurationm, sendvoicemail, deletevoicemail, forcename, forcegreetings, hidefromdir, maxmsg, emailsubject, emailbody, imapuser, imappassword, imapfolder, imapvmsharedid, attachfmt, serveremail, locale, tempgreetwarn, messagewrap, moveheard, minsecs, maxsecs, nextaftercmd, backupdeleted, volgain, passwordlocation, commented, skipcheckpass) FROM stdin;
\.


--
-- Name: voicemail_uniqueid_seq; Type: SEQUENCE SET; Schema: public; Owner: asterisk
--

SELECT pg_catalog.setval('voicemail_uniqueid_seq', 1, false);


--
-- Name: accessfeatures_host_feature_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY accessfeatures
    ADD CONSTRAINT accessfeatures_host_feature_key UNIQUE (host, feature);


--
-- Name: accessfeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY accessfeatures
    ADD CONSTRAINT accessfeatures_pkey PRIMARY KEY (id);


--
-- Name: accesswebservice_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY accesswebservice
    ADD CONSTRAINT accesswebservice_name_key UNIQUE (name);


--
-- Name: accesswebservice_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY accesswebservice
    ADD CONSTRAINT accesswebservice_pkey PRIMARY KEY (id);


--
-- Name: agent_login_status_extension_context_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agent_login_status
    ADD CONSTRAINT agent_login_status_extension_context_key UNIQUE (extension, context);


--
-- Name: agent_login_status_interface_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agent_login_status
    ADD CONSTRAINT agent_login_status_interface_key UNIQUE (interface);


--
-- Name: agent_login_status_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agent_login_status
    ADD CONSTRAINT agent_login_status_pkey PRIMARY KEY (agent_id);


--
-- Name: agent_membership_status_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agent_membership_status
    ADD CONSTRAINT agent_membership_status_pkey PRIMARY KEY (agent_id, queue_id);


--
-- Name: agentfeatures_number_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agentfeatures
    ADD CONSTRAINT agentfeatures_number_key UNIQUE (number);


--
-- Name: agentfeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agentfeatures
    ADD CONSTRAINT agentfeatures_pkey PRIMARY KEY (id);


--
-- Name: agentglobalparams_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agentglobalparams
    ADD CONSTRAINT agentglobalparams_pkey PRIMARY KEY (id);


--
-- Name: agentgroup_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agentgroup
    ADD CONSTRAINT agentgroup_pkey PRIMARY KEY (id);


--
-- Name: agentqueueskill_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY agentqueueskill
    ADD CONSTRAINT agentqueueskill_pkey PRIMARY KEY (agentid, skillid);


--
-- Name: attachment_object_type_object_id_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY attachment
    ADD CONSTRAINT attachment_object_type_object_id_key UNIQUE (object_type, object_id);


--
-- Name: attachment_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY attachment
    ADD CONSTRAINT attachment_pkey PRIMARY KEY (id);


--
-- Name: call_log_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY call_log
    ADD CONSTRAINT call_log_pkey PRIMARY KEY (id);


--
-- Name: callerid_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY callerid
    ADD CONSTRAINT callerid_pkey PRIMARY KEY (type, typeval);


--
-- Name: callfilter_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY callfilter
    ADD CONSTRAINT callfilter_name_key UNIQUE (name);


--
-- Name: callfilter_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY callfilter
    ADD CONSTRAINT callfilter_pkey PRIMARY KEY (id);


--
-- Name: callfiltermember_callfilterid_type_typeval_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY callfiltermember
    ADD CONSTRAINT callfiltermember_callfilterid_type_typeval_key UNIQUE (callfilterid, type, typeval);


--
-- Name: callfiltermember_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY callfiltermember
    ADD CONSTRAINT callfiltermember_pkey PRIMARY KEY (id);


--
-- Name: cel_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cel
    ADD CONSTRAINT cel_pkey PRIMARY KEY (id);


--
-- Name: context_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY context
    ADD CONSTRAINT context_pkey PRIMARY KEY (name);


--
-- Name: contextinclude_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY contextinclude
    ADD CONSTRAINT contextinclude_pkey PRIMARY KEY (context, include);


--
-- Name: contextmember_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY contextmember
    ADD CONSTRAINT contextmember_pkey PRIMARY KEY (context, type, typeval, varname);


--
-- Name: contextnumbers_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY contextnumbers
    ADD CONSTRAINT contextnumbers_pkey PRIMARY KEY (context, type, numberbeg, numberend);


--
-- Name: contexttype_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY contexttype
    ADD CONSTRAINT contexttype_name_key UNIQUE (name);


--
-- Name: contexttype_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY contexttype
    ADD CONSTRAINT contexttype_pkey PRIMARY KEY (id);


--
-- Name: cti_preference_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_preference
    ADD CONSTRAINT cti_preference_pkey PRIMARY KEY (id);


--
-- Name: cti_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_profile
    ADD CONSTRAINT cti_profile_pkey PRIMARY KEY (id);


--
-- Name: cti_profile_preference_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_profile_preference
    ADD CONSTRAINT cti_profile_preference_pkey PRIMARY KEY (profile_id, preference_id);


--
-- Name: cti_profile_service_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_profile_service
    ADD CONSTRAINT cti_profile_service_pkey PRIMARY KEY (profile_id, service_id);


--
-- Name: cti_profile_xlet_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_profile_xlet
    ADD CONSTRAINT cti_profile_xlet_pkey PRIMARY KEY (xlet_id, profile_id);


--
-- Name: cti_service_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_service
    ADD CONSTRAINT cti_service_pkey PRIMARY KEY (id);


--
-- Name: cti_xlet_layout_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_xlet_layout
    ADD CONSTRAINT cti_xlet_layout_pkey PRIMARY KEY (id);


--
-- Name: cti_xlet_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cti_xlet
    ADD CONSTRAINT cti_xlet_pkey PRIMARY KEY (id);


--
-- Name: cticontexts_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY cticontexts
    ADD CONSTRAINT cticontexts_pkey PRIMARY KEY (id);


--
-- Name: ctidirectories_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctidirectories
    ADD CONSTRAINT ctidirectories_pkey PRIMARY KEY (id);


--
-- Name: ctidirectoryfields_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctidirectoryfields
    ADD CONSTRAINT ctidirectoryfields_pkey PRIMARY KEY (dir_id, fieldname);


--
-- Name: ctidisplays_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctidisplays
    ADD CONSTRAINT ctidisplays_pkey PRIMARY KEY (id);


--
-- Name: ctilog_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctilog
    ADD CONSTRAINT ctilog_pkey PRIMARY KEY (id);


--
-- Name: ctimain_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctimain
    ADD CONSTRAINT ctimain_pkey PRIMARY KEY (id);


--
-- Name: ctiphonehints_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctiphonehints
    ADD CONSTRAINT ctiphonehints_pkey PRIMARY KEY (id);


--
-- Name: ctiphonehintsgroup_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctiphonehintsgroup
    ADD CONSTRAINT ctiphonehintsgroup_pkey PRIMARY KEY (id);


--
-- Name: ctipresences_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctipresences
    ADD CONSTRAINT ctipresences_pkey PRIMARY KEY (id);


--
-- Name: ctireversedirectories_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctireversedirectories
    ADD CONSTRAINT ctireversedirectories_pkey PRIMARY KEY (id);


--
-- Name: ctisheetactions_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctisheetactions
    ADD CONSTRAINT ctisheetactions_pkey PRIMARY KEY (id);


--
-- Name: ctisheetevents_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctisheetevents
    ADD CONSTRAINT ctisheetevents_pkey PRIMARY KEY (id);


--
-- Name: ctistatus_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctistatus
    ADD CONSTRAINT ctistatus_pkey PRIMARY KEY (id);


--
-- Name: ctistatus_presence_id_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ctistatus
    ADD CONSTRAINT ctistatus_presence_id_name_key UNIQUE (presence_id, name);


--
-- Name: dhcp_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY dhcp
    ADD CONSTRAINT dhcp_pkey PRIMARY KEY (id);


--
-- Name: dialaction_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY dialaction
    ADD CONSTRAINT dialaction_pkey PRIMARY KEY (event, category, categoryval);


--
-- Name: dialpattern_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY dialpattern
    ADD CONSTRAINT dialpattern_pkey PRIMARY KEY (id);


--
-- Name: directories_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY directories
    ADD CONSTRAINT directories_pkey PRIMARY KEY (id);


--
-- Name: entity_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY entity
    ADD CONSTRAINT entity_name_key UNIQUE (name);


--
-- Name: entity_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY entity
    ADD CONSTRAINT entity_pkey PRIMARY KEY (id);


--
-- Name: extensions_exten_context_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY extensions
    ADD CONSTRAINT extensions_exten_context_key UNIQUE (exten, context);


--
-- Name: extensions_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY extensions
    ADD CONSTRAINT extensions_pkey PRIMARY KEY (id);


--
-- Name: features_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY features
    ADD CONSTRAINT features_pkey PRIMARY KEY (id);


--
-- Name: func_key_dest_conference_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_dest_conference
    ADD CONSTRAINT func_key_dest_conference_pkey PRIMARY KEY (func_key_id, destination_type_id, conference_id);


--
-- Name: func_key_dest_group_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_dest_group
    ADD CONSTRAINT func_key_dest_group_pkey PRIMARY KEY (func_key_id, destination_type_id, group_id);


--
-- Name: func_key_dest_queue_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_dest_queue
    ADD CONSTRAINT func_key_dest_queue_pkey PRIMARY KEY (func_key_id, destination_type_id, queue_id);


--
-- Name: func_key_dest_user_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_dest_user
    ADD CONSTRAINT func_key_dest_user_pkey PRIMARY KEY (func_key_id, user_id, destination_type_id);


--
-- Name: func_key_destination_type_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_destination_type
    ADD CONSTRAINT func_key_destination_type_pkey PRIMARY KEY (id);


--
-- Name: func_key_mapping_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_mapping
    ADD CONSTRAINT func_key_mapping_pkey PRIMARY KEY (template_id, func_key_id, destination_type_id);


--
-- Name: func_key_mapping_template_id_position_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_mapping
    ADD CONSTRAINT func_key_mapping_template_id_position_key UNIQUE (template_id, "position");


--
-- Name: func_key_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key
    ADD CONSTRAINT func_key_pkey PRIMARY KEY (id, destination_type_id);


--
-- Name: func_key_template_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_template
    ADD CONSTRAINT func_key_template_pkey PRIMARY KEY (id);


--
-- Name: func_key_type_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY func_key_type
    ADD CONSTRAINT func_key_type_pkey PRIMARY KEY (id);


--
-- Name: general_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY general
    ADD CONSTRAINT general_pkey PRIMARY KEY (id);


--
-- Name: groupfeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY groupfeatures
    ADD CONSTRAINT groupfeatures_pkey PRIMARY KEY (id);


--
-- Name: iaxcallnumberlimits_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY iaxcallnumberlimits
    ADD CONSTRAINT iaxcallnumberlimits_pkey PRIMARY KEY (id);


--
-- Name: incall_exten_context_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY incall
    ADD CONSTRAINT incall_exten_context_key UNIQUE (exten, context);


--
-- Name: incall_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY incall
    ADD CONSTRAINT incall_pkey PRIMARY KEY (id);


--
-- Name: ldapfilter_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ldapfilter
    ADD CONSTRAINT ldapfilter_name_key UNIQUE (name);


--
-- Name: ldapfilter_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ldapfilter
    ADD CONSTRAINT ldapfilter_pkey PRIMARY KEY (id);


--
-- Name: ldapserver_host_port_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ldapserver
    ADD CONSTRAINT ldapserver_host_port_key UNIQUE (host, port);


--
-- Name: ldapserver_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ldapserver
    ADD CONSTRAINT ldapserver_name_key UNIQUE (name);


--
-- Name: ldapserver_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY ldapserver
    ADD CONSTRAINT ldapserver_pkey PRIMARY KEY (id);


--
-- Name: linefeatures_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY linefeatures
    ADD CONSTRAINT linefeatures_name_key UNIQUE (name);


--
-- Name: linefeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY linefeatures
    ADD CONSTRAINT linefeatures_pkey PRIMARY KEY (id);


--
-- Name: linefeatures_protocol_protocolid_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY linefeatures
    ADD CONSTRAINT linefeatures_protocol_protocolid_key UNIQUE (protocol, protocolid);


--
-- Name: mail_origin_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY mail
    ADD CONSTRAINT mail_origin_key UNIQUE (origin);


--
-- Name: mail_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY mail
    ADD CONSTRAINT mail_pkey PRIMARY KEY (id);


--
-- Name: meetmefeatures_meetmeid_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY meetmefeatures
    ADD CONSTRAINT meetmefeatures_meetmeid_key UNIQUE (meetmeid);


--
-- Name: meetmefeatures_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY meetmefeatures
    ADD CONSTRAINT meetmefeatures_name_key UNIQUE (name);


--
-- Name: meetmefeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY meetmefeatures
    ADD CONSTRAINT meetmefeatures_pkey PRIMARY KEY (id);


--
-- Name: meetmeguest_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY meetmeguest
    ADD CONSTRAINT meetmeguest_pkey PRIMARY KEY (id);


--
-- Name: monitoring_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY monitoring
    ADD CONSTRAINT monitoring_pkey PRIMARY KEY (id);


--
-- Name: musiconhold_filename_category_var_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY musiconhold
    ADD CONSTRAINT musiconhold_filename_category_var_name_key UNIQUE (filename, category, var_name);


--
-- Name: musiconhold_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY musiconhold
    ADD CONSTRAINT musiconhold_pkey PRIMARY KEY (id);


--
-- Name: netiface_ifname_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY netiface
    ADD CONSTRAINT netiface_ifname_key UNIQUE (ifname);


--
-- Name: netiface_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY netiface
    ADD CONSTRAINT netiface_pkey PRIMARY KEY (id);


--
-- Name: outcall_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY outcall
    ADD CONSTRAINT outcall_name_key UNIQUE (name);


--
-- Name: outcall_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY outcall
    ADD CONSTRAINT outcall_pkey PRIMARY KEY (id);


--
-- Name: outcalltrunk_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY outcalltrunk
    ADD CONSTRAINT outcalltrunk_pkey PRIMARY KEY (outcallid, trunkfeaturesid);


--
-- Name: paging_number_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY paging
    ADD CONSTRAINT paging_number_key UNIQUE (number);


--
-- Name: paging_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY paging
    ADD CONSTRAINT paging_pkey PRIMARY KEY (id);


--
-- Name: paginguser_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY paginguser
    ADD CONSTRAINT paginguser_pkey PRIMARY KEY (pagingid, userfeaturesid, caller);


--
-- Name: phonebook_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY phonebook
    ADD CONSTRAINT phonebook_pkey PRIMARY KEY (id);


--
-- Name: phonebookaddress_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY phonebookaddress
    ADD CONSTRAINT phonebookaddress_pkey PRIMARY KEY (id);


--
-- Name: phonebooknumber_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY phonebooknumber
    ADD CONSTRAINT phonebooknumber_pkey PRIMARY KEY (id);


--
-- Name: phonefunckey_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY phonefunckey
    ADD CONSTRAINT phonefunckey_pkey PRIMARY KEY (iduserfeatures, fknum);


--
-- Name: pickup_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY pickup
    ADD CONSTRAINT pickup_name_key UNIQUE (name);


--
-- Name: pickup_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY pickup
    ADD CONSTRAINT pickup_pkey PRIMARY KEY (id);


--
-- Name: pickupmember_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY pickupmember
    ADD CONSTRAINT pickupmember_pkey PRIMARY KEY (pickupid, category, membertype, memberid);


--
-- Name: provisioning_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY provisioning
    ADD CONSTRAINT provisioning_pkey PRIMARY KEY (id);


--
-- Name: queue_info_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queue_info
    ADD CONSTRAINT queue_info_pkey PRIMARY KEY (id);


--
-- Name: queue_log_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queue_log
    ADD CONSTRAINT queue_log_pkey PRIMARY KEY (id);


--
-- Name: queue_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queue
    ADD CONSTRAINT queue_pkey PRIMARY KEY (name);


--
-- Name: queuefeatures_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queuefeatures
    ADD CONSTRAINT queuefeatures_name_key UNIQUE (name);


--
-- Name: queuefeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queuefeatures
    ADD CONSTRAINT queuefeatures_pkey PRIMARY KEY (id);


--
-- Name: queuemember_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queuemember
    ADD CONSTRAINT queuemember_pkey PRIMARY KEY (queue_name, interface);


--
-- Name: queuemember_queue_name_channel_usertype_userid_category_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queuemember
    ADD CONSTRAINT queuemember_queue_name_channel_usertype_userid_category_key UNIQUE (queue_name, channel, usertype, userid, category);


--
-- Name: queuepenalty_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queuepenalty
    ADD CONSTRAINT queuepenalty_name_key UNIQUE (name);


--
-- Name: queuepenalty_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queuepenalty
    ADD CONSTRAINT queuepenalty_pkey PRIMARY KEY (id);


--
-- Name: queuepenaltychange_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queuepenaltychange
    ADD CONSTRAINT queuepenaltychange_pkey PRIMARY KEY (queuepenalty_id, seconds);


--
-- Name: queueskill_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queueskill
    ADD CONSTRAINT queueskill_name_key UNIQUE (name);


--
-- Name: queueskill_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queueskill
    ADD CONSTRAINT queueskill_pkey PRIMARY KEY (id);


--
-- Name: queueskillcat_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queueskillcat
    ADD CONSTRAINT queueskillcat_name_key UNIQUE (name);


--
-- Name: queueskillcat_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queueskillcat
    ADD CONSTRAINT queueskillcat_pkey PRIMARY KEY (id);


--
-- Name: queueskillrule_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY queueskillrule
    ADD CONSTRAINT queueskillrule_pkey PRIMARY KEY (id);


--
-- Name: record_campaign_campaign_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY record_campaign
    ADD CONSTRAINT record_campaign_campaign_name_key UNIQUE (campaign_name);


--
-- Name: record_campaign_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY record_campaign
    ADD CONSTRAINT record_campaign_pkey PRIMARY KEY (id);


--
-- Name: recording_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY recording
    ADD CONSTRAINT recording_pkey PRIMARY KEY (cid);


--
-- Name: resolvconf_domain_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY resolvconf
    ADD CONSTRAINT resolvconf_domain_key UNIQUE (domain);


--
-- Name: resolvconf_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY resolvconf
    ADD CONSTRAINT resolvconf_pkey PRIMARY KEY (id);


--
-- Name: rightcall_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY rightcall
    ADD CONSTRAINT rightcall_name_key UNIQUE (name);


--
-- Name: rightcall_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY rightcall
    ADD CONSTRAINT rightcall_pkey PRIMARY KEY (id);


--
-- Name: rightcallexten_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY rightcallexten
    ADD CONSTRAINT rightcallexten_pkey PRIMARY KEY (id);


--
-- Name: rightcallexten_rightcallid_exten_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY rightcallexten
    ADD CONSTRAINT rightcallexten_rightcallid_exten_key UNIQUE (rightcallid, exten);


--
-- Name: rightcallmember_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY rightcallmember
    ADD CONSTRAINT rightcallmember_pkey PRIMARY KEY (id);


--
-- Name: rightcallmember_rightcallid_type_typeval_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY rightcallmember
    ADD CONSTRAINT rightcallmember_rightcallid_type_typeval_key UNIQUE (rightcallid, type, typeval);


--
-- Name: sccpdevice_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY sccpdevice
    ADD CONSTRAINT sccpdevice_pkey PRIMARY KEY (id);


--
-- Name: sccpgeneralsettings_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY sccpgeneralsettings
    ADD CONSTRAINT sccpgeneralsettings_pkey PRIMARY KEY (id);


--
-- Name: sccpline_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY sccpline
    ADD CONSTRAINT sccpline_pkey PRIMARY KEY (id);


--
-- Name: schedule_path_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY schedule_path
    ADD CONSTRAINT schedule_path_pkey PRIMARY KEY (schedule_id, path, pathid);


--
-- Name: schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY schedule
    ADD CONSTRAINT schedule_pkey PRIMARY KEY (id);


--
-- Name: schedule_time_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY schedule_time
    ADD CONSTRAINT schedule_time_pkey PRIMARY KEY (id);


--
-- Name: serverfeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY serverfeatures
    ADD CONSTRAINT serverfeatures_pkey PRIMARY KEY (id);


--
-- Name: serverfeatures_serverid_feature_type_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY serverfeatures
    ADD CONSTRAINT serverfeatures_serverid_feature_type_key UNIQUE (serverid, feature, type);


--
-- Name: session_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY session
    ADD CONSTRAINT session_pkey PRIMARY KEY (sessid);


--
-- Name: sipauthentication_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY sipauthentication
    ADD CONSTRAINT sipauthentication_pkey PRIMARY KEY (id);


--
-- Name: stat_agent_periodic_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stat_agent_periodic
    ADD CONSTRAINT stat_agent_periodic_pkey PRIMARY KEY (id);


--
-- Name: stat_agent_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stat_agent
    ADD CONSTRAINT stat_agent_pkey PRIMARY KEY (id);


--
-- Name: stat_call_on_queue_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stat_call_on_queue
    ADD CONSTRAINT stat_call_on_queue_pkey PRIMARY KEY (id);


--
-- Name: stat_queue_periodic_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stat_queue_periodic
    ADD CONSTRAINT stat_queue_periodic_pkey PRIMARY KEY (id);


--
-- Name: stat_queue_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stat_queue
    ADD CONSTRAINT stat_queue_pkey PRIMARY KEY (id);


--
-- Name: staticiax_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY staticiax
    ADD CONSTRAINT staticiax_pkey PRIMARY KEY (id);


--
-- Name: staticmeetme_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY staticmeetme
    ADD CONSTRAINT staticmeetme_pkey PRIMARY KEY (id);


--
-- Name: staticqueue_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY staticqueue
    ADD CONSTRAINT staticqueue_pkey PRIMARY KEY (id);


--
-- Name: staticsip_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY staticsip
    ADD CONSTRAINT staticsip_pkey PRIMARY KEY (id);


--
-- Name: staticvoicemail_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY staticvoicemail
    ADD CONSTRAINT staticvoicemail_pkey PRIMARY KEY (id);


--
-- Name: stats_conf_agent_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf_agent
    ADD CONSTRAINT stats_conf_agent_pkey PRIMARY KEY (stats_conf_id, agentfeatures_id);


--
-- Name: stats_conf_group_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf_group
    ADD CONSTRAINT stats_conf_group_pkey PRIMARY KEY (stats_conf_id, groupfeatures_id);


--
-- Name: stats_conf_incall_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf_incall
    ADD CONSTRAINT stats_conf_incall_pkey PRIMARY KEY (stats_conf_id, incall_id);


--
-- Name: stats_conf_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf
    ADD CONSTRAINT stats_conf_name_key UNIQUE (name);


--
-- Name: stats_conf_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf
    ADD CONSTRAINT stats_conf_pkey PRIMARY KEY (id);


--
-- Name: stats_conf_queue_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf_queue
    ADD CONSTRAINT stats_conf_queue_pkey PRIMARY KEY (stats_conf_id, queuefeatures_id);


--
-- Name: stats_conf_user_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf_user
    ADD CONSTRAINT stats_conf_user_pkey PRIMARY KEY (stats_conf_id, userfeatures_id);


--
-- Name: stats_conf_xivouser_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY stats_conf_xivouser
    ADD CONSTRAINT stats_conf_xivouser_pkey PRIMARY KEY (stats_conf_id, user_id);


--
-- Name: trunkfeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY trunkfeatures
    ADD CONSTRAINT trunkfeatures_pkey PRIMARY KEY (id);


--
-- Name: trunkfeatures_protocol_protocolid_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY trunkfeatures
    ADD CONSTRAINT trunkfeatures_protocol_protocolid_key UNIQUE (protocol, protocolid);


--
-- Name: user_line_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY user_line
    ADD CONSTRAINT user_line_pkey PRIMARY KEY (id, line_id);


--
-- Name: user_line_user_id_line_id_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY user_line
    ADD CONSTRAINT user_line_user_id_line_id_key UNIQUE (user_id, line_id);


--
-- Name: user_login_meta_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_login_meta_key UNIQUE (login, meta);


--
-- Name: user_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: usercustom_interface_intfsuffix_category_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY usercustom
    ADD CONSTRAINT usercustom_interface_intfsuffix_category_key UNIQUE (interface, intfsuffix, category);


--
-- Name: usercustom_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY usercustom
    ADD CONSTRAINT usercustom_pkey PRIMARY KEY (id);


--
-- Name: userfeatures_func_key_private_template_id_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY userfeatures
    ADD CONSTRAINT userfeatures_func_key_private_template_id_key UNIQUE (func_key_private_template_id);


--
-- Name: userfeatures_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY userfeatures
    ADD CONSTRAINT userfeatures_pkey PRIMARY KEY (id);


--
-- Name: useriax_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY useriax
    ADD CONSTRAINT useriax_name_key UNIQUE (name);


--
-- Name: useriax_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY useriax
    ADD CONSTRAINT useriax_pkey PRIMARY KEY (id);


--
-- Name: usersip_name_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY usersip
    ADD CONSTRAINT usersip_name_key UNIQUE (name);


--
-- Name: usersip_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY usersip
    ADD CONSTRAINT usersip_pkey PRIMARY KEY (id);


--
-- Name: voicemail_mailbox_context_key; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY voicemail
    ADD CONSTRAINT voicemail_mailbox_context_key UNIQUE (mailbox, context);


--
-- Name: voicemail_pkey; Type: CONSTRAINT; Schema: public; Owner: asterisk; Tablespace: 
--

ALTER TABLE ONLY voicemail
    ADD CONSTRAINT voicemail_pkey PRIMARY KEY (uniqueid);


--
-- Name: accesswebservice__idx__disable; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX accesswebservice__idx__disable ON accesswebservice USING btree (disable);


--
-- Name: accesswebservice__idx__host; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX accesswebservice__idx__host ON accesswebservice USING btree (host);


--
-- Name: accesswebservice__idx__login; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX accesswebservice__idx__login ON accesswebservice USING btree (login);


--
-- Name: accesswebservice__idx__passwd; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX accesswebservice__idx__passwd ON accesswebservice USING btree (passwd);


--
-- Name: cel__idx__call_log_id; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX cel__idx__call_log_id ON cel USING btree (call_log_id);


--
-- Name: cel__idx__eventtime; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX cel__idx__eventtime ON cel USING btree (eventtime);


--
-- Name: cel__idx__linkedid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX cel__idx__linkedid ON cel USING btree (linkedid);


--
-- Name: cel__idx__uniqueid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX cel__idx__uniqueid ON cel USING btree (uniqueid);


--
-- Name: contextmember__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX contextmember__idx__context ON contextmember USING btree (context);


--
-- Name: contextmember__idx__context_type; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX contextmember__idx__context_type ON contextmember USING btree (context, type);


--
-- Name: dialaction__idx__action_actionarg1; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX dialaction__idx__action_actionarg1 ON dialaction USING btree (action, actionarg1);


--
-- Name: extensions__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX extensions__idx__context ON extensions USING btree (context);


--
-- Name: extensions__idx__exten; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX extensions__idx__exten ON extensions USING btree (exten);


--
-- Name: extensions__idx__type; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX extensions__idx__type ON extensions USING btree (type);


--
-- Name: extensions__idx__typeval; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX extensions__idx__typeval ON extensions USING btree (typeval);


--
-- Name: features__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX features__idx__category ON features USING btree (category);


--
-- Name: groupfeatures__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX groupfeatures__idx__context ON groupfeatures USING btree (context);


--
-- Name: groupfeatures__idx__name; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX groupfeatures__idx__name ON groupfeatures USING btree (name);


--
-- Name: groupfeatures__idx__number; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX groupfeatures__idx__number ON groupfeatures USING btree (number);


--
-- Name: incall__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX incall__idx__context ON incall USING btree (context);


--
-- Name: incall__idx__exten; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX incall__idx__exten ON incall USING btree (exten);


--
-- Name: linefeatures__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX linefeatures__idx__context ON linefeatures USING btree (context);


--
-- Name: linefeatures__idx__device; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX linefeatures__idx__device ON linefeatures USING btree (device);


--
-- Name: linefeatures__idx__number; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX linefeatures__idx__number ON linefeatures USING btree (number);


--
-- Name: linefeatures__idx__provisioningid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX linefeatures__idx__provisioningid ON linefeatures USING btree (provisioningid);


--
-- Name: meetmefeatures__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX meetmefeatures__idx__context ON meetmefeatures USING btree (context);


--
-- Name: meetmefeatures__idx__number; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX meetmefeatures__idx__number ON meetmefeatures USING btree (confno);


--
-- Name: outcalltrunk__idx__priority; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX outcalltrunk__idx__priority ON outcalltrunk USING btree (priority);


--
-- Name: paginguser__idx__pagingid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX paginguser__idx__pagingid ON paginguser USING btree (pagingid);


--
-- Name: phonebookaddress__uidx__phonebookid_type; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE UNIQUE INDEX phonebookaddress__uidx__phonebookid_type ON phonebookaddress USING btree (phonebookid, type);


--
-- Name: phonebooknumber__uidx__phonebookid_type; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE UNIQUE INDEX phonebooknumber__uidx__phonebookid_type ON phonebooknumber USING btree (phonebookid, type);


--
-- Name: phonefunckey__idx__exten; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX phonefunckey__idx__exten ON phonefunckey USING btree (exten);


--
-- Name: phonefunckey__idx__progfunckey; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX phonefunckey__idx__progfunckey ON phonefunckey USING btree (progfunckey);


--
-- Name: phonefunckey__idx__typeextenumbers_typevalextenumbers; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX phonefunckey__idx__typeextenumbers_typevalextenumbers ON phonefunckey USING btree (typeextenumbers, typevalextenumbers);


--
-- Name: phonefunckey__idx__typeextenumbersright_typevalextenumbersright; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX phonefunckey__idx__typeextenumbersright_typevalextenumbersright ON phonefunckey USING btree (typeextenumbersright, typevalextenumbersright);


--
-- Name: queue__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue__idx__category ON queue USING btree (category);


--
-- Name: queue_info_call_time_t_index; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue_info_call_time_t_index ON queue_info USING btree (call_time_t);


--
-- Name: queue_info_queue_name_index; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue_info_queue_name_index ON queue_info USING btree (queue_name);


--
-- Name: queue_log__idx_agent; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue_log__idx_agent ON queue_log USING btree (agent);


--
-- Name: queue_log__idx_callid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue_log__idx_callid ON queue_log USING btree (callid);


--
-- Name: queue_log__idx_event; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue_log__idx_event ON queue_log USING btree (event);


--
-- Name: queue_log__idx_queuename; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue_log__idx_queuename ON queue_log USING btree (queuename);


--
-- Name: queue_log__idx_time; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queue_log__idx_time ON queue_log USING btree ("time");


--
-- Name: queuefeatures__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queuefeatures__idx__context ON queuefeatures USING btree (context);


--
-- Name: queuefeatures__idx__number; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queuefeatures__idx__number ON queuefeatures USING btree (number);


--
-- Name: queuemember__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queuemember__idx__category ON queuemember USING btree (category);


--
-- Name: queuemember__idx__channel; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queuemember__idx__channel ON queuemember USING btree (channel);


--
-- Name: queuemember__idx__userid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queuemember__idx__userid ON queuemember USING btree (userid);


--
-- Name: queuemember__idx__usertype; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX queuemember__idx__usertype ON queuemember USING btree (usertype);


--
-- Name: schedule_path_path; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX schedule_path_path ON schedule_path USING btree (path, pathid);


--
-- Name: schedule_time__idx__scheduleid_commented; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX schedule_time__idx__scheduleid_commented ON schedule_time USING btree (schedule_id, commented);


--
-- Name: session__idx__expire; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX session__idx__expire ON session USING btree (expire);


--
-- Name: session__idx__identifier; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX session__idx__identifier ON session USING btree (identifier);


--
-- Name: sipauthentication__idx__usersip_id; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX sipauthentication__idx__usersip_id ON sipauthentication USING btree (usersip_id);


--
-- Name: stat_agent__idx_name; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX stat_agent__idx_name ON stat_agent USING btree (name);


--
-- Name: stat_agent_periodic__idx__agent_id; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX stat_agent_periodic__idx__agent_id ON stat_agent_periodic USING btree (agent_id);


--
-- Name: stat_agent_periodic__idx__time; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX stat_agent_periodic__idx__time ON stat_agent_periodic USING btree ("time");


--
-- Name: stat_queue__idx_name; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX stat_queue__idx_name ON stat_queue USING btree (name);


--
-- Name: staticiax__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX staticiax__idx__category ON staticiax USING btree (category);


--
-- Name: staticmeetme__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX staticmeetme__idx__category ON staticmeetme USING btree (category);


--
-- Name: staticqueue__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX staticqueue__idx__category ON staticqueue USING btree (category);


--
-- Name: staticsip__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX staticsip__idx__category ON staticsip USING btree (category);


--
-- Name: staticvoicemail__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX staticvoicemail__idx__category ON staticvoicemail USING btree (category);


--
-- Name: stats_conf__idx__disable; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX stats_conf__idx__disable ON stats_conf USING btree (disable);


--
-- Name: trunkfeatures__idx__registercommented; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX trunkfeatures__idx__registercommented ON trunkfeatures USING btree (registercommented);


--
-- Name: trunkfeatures__idx__registerid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX trunkfeatures__idx__registerid ON trunkfeatures USING btree (registerid);


--
-- Name: usercustom__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX usercustom__idx__category ON usercustom USING btree (category);


--
-- Name: usercustom__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX usercustom__idx__context ON usercustom USING btree (context);


--
-- Name: usercustom__idx__name; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX usercustom__idx__name ON usercustom USING btree (name);


--
-- Name: userfeatures__idx__agentid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX userfeatures__idx__agentid ON userfeatures USING btree (agentid);


--
-- Name: userfeatures__idx__entityid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX userfeatures__idx__entityid ON userfeatures USING btree (entityid);


--
-- Name: userfeatures__idx__firstname; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX userfeatures__idx__firstname ON userfeatures USING btree (firstname);


--
-- Name: userfeatures__idx__lastname; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX userfeatures__idx__lastname ON userfeatures USING btree (lastname);


--
-- Name: userfeatures__idx__loginclient; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX userfeatures__idx__loginclient ON userfeatures USING btree (loginclient);


--
-- Name: userfeatures__idx__musiconhold; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX userfeatures__idx__musiconhold ON userfeatures USING btree (musiconhold);


--
-- Name: userfeatures__idx__voicemailid; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX userfeatures__idx__voicemailid ON userfeatures USING btree (voicemailid);


--
-- Name: useriax__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX useriax__idx__category ON useriax USING btree (category);


--
-- Name: useriax__idx__mailbox; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX useriax__idx__mailbox ON useriax USING btree (mailbox);


--
-- Name: usersip__idx__category; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX usersip__idx__category ON usersip USING btree (category);


--
-- Name: usersip__idx__mailbox; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX usersip__idx__mailbox ON usersip USING btree (mailbox);


--
-- Name: voicemail__idx__context; Type: INDEX; Schema: public; Owner: asterisk; Tablespace: 
--

CREATE INDEX voicemail__idx__context ON voicemail USING btree (context);


--
-- Name: change_queue_log_agent; Type: TRIGGER; Schema: public; Owner: asterisk
--

CREATE TRIGGER change_queue_log_agent BEFORE INSERT ON queue_log FOR EACH ROW WHEN ((((new.event)::text = 'PAUSEALL'::text) OR ((new.event)::text = 'UNPAUSEALL'::text))) EXECUTE PROCEDURE set_agent_on_pauseall();


--
-- Name: cel_call_log_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cel
    ADD CONSTRAINT cel_call_log_id_fkey FOREIGN KEY (call_log_id) REFERENCES call_log(id) ON DELETE SET NULL;


--
-- Name: cti_profile_phonehints_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile
    ADD CONSTRAINT cti_profile_phonehints_id_fkey FOREIGN KEY (phonehints_id) REFERENCES ctiphonehintsgroup(id) ON DELETE RESTRICT;


--
-- Name: cti_profile_preference_preference_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile_preference
    ADD CONSTRAINT cti_profile_preference_preference_id_fkey FOREIGN KEY (preference_id) REFERENCES cti_preference(id) ON DELETE CASCADE;


--
-- Name: cti_profile_preference_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile_preference
    ADD CONSTRAINT cti_profile_preference_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES cti_profile(id) ON DELETE CASCADE;


--
-- Name: cti_profile_presence_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile
    ADD CONSTRAINT cti_profile_presence_id_fkey FOREIGN KEY (presence_id) REFERENCES ctipresences(id) ON DELETE RESTRICT;


--
-- Name: cti_profile_service_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile_service
    ADD CONSTRAINT cti_profile_service_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES cti_profile(id) ON DELETE CASCADE;


--
-- Name: cti_profile_service_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile_service
    ADD CONSTRAINT cti_profile_service_service_id_fkey FOREIGN KEY (service_id) REFERENCES cti_service(id) ON DELETE CASCADE;


--
-- Name: cti_profile_xlet_layout_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile_xlet
    ADD CONSTRAINT cti_profile_xlet_layout_id_fkey FOREIGN KEY (layout_id) REFERENCES cti_xlet_layout(id) ON DELETE RESTRICT;


--
-- Name: cti_profile_xlet_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile_xlet
    ADD CONSTRAINT cti_profile_xlet_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES cti_profile(id) ON DELETE CASCADE;


--
-- Name: cti_profile_xlet_xlet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY cti_profile_xlet
    ADD CONSTRAINT cti_profile_xlet_xlet_id_fkey FOREIGN KEY (xlet_id) REFERENCES cti_xlet(id) ON DELETE CASCADE;


--
-- Name: func_key_dest_conference_conference_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_conference
    ADD CONSTRAINT func_key_dest_conference_conference_id_fkey FOREIGN KEY (conference_id) REFERENCES meetmefeatures(id);


--
-- Name: func_key_dest_conference_func_key_id_destination_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_conference
    ADD CONSTRAINT func_key_dest_conference_func_key_id_destination_type_id_fkey FOREIGN KEY (func_key_id, destination_type_id) REFERENCES func_key(id, destination_type_id);


--
-- Name: func_key_dest_group_func_key_id_destination_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_group
    ADD CONSTRAINT func_key_dest_group_func_key_id_destination_type_id_fkey FOREIGN KEY (func_key_id, destination_type_id) REFERENCES func_key(id, destination_type_id);


--
-- Name: func_key_dest_group_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_group
    ADD CONSTRAINT func_key_dest_group_group_id_fkey FOREIGN KEY (group_id) REFERENCES groupfeatures(id);


--
-- Name: func_key_dest_queue_func_key_id_destination_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_queue
    ADD CONSTRAINT func_key_dest_queue_func_key_id_destination_type_id_fkey FOREIGN KEY (func_key_id, destination_type_id) REFERENCES func_key(id, destination_type_id);


--
-- Name: func_key_dest_queue_queue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_queue
    ADD CONSTRAINT func_key_dest_queue_queue_id_fkey FOREIGN KEY (queue_id) REFERENCES queuefeatures(id);


--
-- Name: func_key_dest_user_func_key_id_destination_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_user
    ADD CONSTRAINT func_key_dest_user_func_key_id_destination_type_id_fkey FOREIGN KEY (func_key_id, destination_type_id) REFERENCES func_key(id, destination_type_id);


--
-- Name: func_key_dest_user_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_dest_user
    ADD CONSTRAINT func_key_dest_user_user_id_fkey FOREIGN KEY (user_id) REFERENCES userfeatures(id);


--
-- Name: func_key_destination_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key
    ADD CONSTRAINT func_key_destination_type_id_fkey FOREIGN KEY (destination_type_id) REFERENCES func_key_destination_type(id);


--
-- Name: func_key_mapping_func_key_id_destination_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_mapping
    ADD CONSTRAINT func_key_mapping_func_key_id_destination_type_id_fkey FOREIGN KEY (func_key_id, destination_type_id) REFERENCES func_key(id, destination_type_id);


--
-- Name: func_key_mapping_template_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key_mapping
    ADD CONSTRAINT func_key_mapping_template_id_fkey FOREIGN KEY (template_id) REFERENCES func_key_template(id);


--
-- Name: func_key_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY func_key
    ADD CONSTRAINT func_key_type_id_fkey FOREIGN KEY (type_id) REFERENCES func_key_type(id);


--
-- Name: record_campaign_queue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY record_campaign
    ADD CONSTRAINT record_campaign_queue_id_fkey FOREIGN KEY (queue_id) REFERENCES queuefeatures(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: recording_agent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY recording
    ADD CONSTRAINT recording_agent_id_fkey FOREIGN KEY (agent_id) REFERENCES agentfeatures(id) ON UPDATE CASCADE ON DELETE SET NULL;


--
-- Name: recording_campaign_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY recording
    ADD CONSTRAINT recording_campaign_id_fkey FOREIGN KEY (campaign_id) REFERENCES record_campaign(id);


--
-- Name: stat_agent_periodic_agent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_agent_periodic
    ADD CONSTRAINT stat_agent_periodic_agent_id_fkey FOREIGN KEY (agent_id) REFERENCES stat_agent(id);


--
-- Name: stat_call_on_queue_agent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_call_on_queue
    ADD CONSTRAINT stat_call_on_queue_agent_id_fkey FOREIGN KEY (agent_id) REFERENCES stat_agent(id);


--
-- Name: stat_call_on_queue_queue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_call_on_queue
    ADD CONSTRAINT stat_call_on_queue_queue_id_fkey FOREIGN KEY (queue_id) REFERENCES stat_queue(id);


--
-- Name: stat_queue_periodic_queue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY stat_queue_periodic
    ADD CONSTRAINT stat_queue_periodic_queue_id_fkey FOREIGN KEY (queue_id) REFERENCES stat_queue(id);


--
-- Name: user_entity_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_entity_id_fkey FOREIGN KEY (entity_id) REFERENCES entity(id) ON DELETE RESTRICT;


--
-- Name: user_line_extension_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY user_line
    ADD CONSTRAINT user_line_extension_id_fkey FOREIGN KEY (extension_id) REFERENCES extensions(id);


--
-- Name: user_line_line_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY user_line
    ADD CONSTRAINT user_line_line_id_fkey FOREIGN KEY (line_id) REFERENCES linefeatures(id);


--
-- Name: user_line_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY user_line
    ADD CONSTRAINT user_line_user_id_fkey FOREIGN KEY (user_id) REFERENCES userfeatures(id);


--
-- Name: userfeatures_cti_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY userfeatures
    ADD CONSTRAINT userfeatures_cti_profile_id_fkey FOREIGN KEY (cti_profile_id) REFERENCES cti_profile(id) ON DELETE RESTRICT;


--
-- Name: userfeatures_func_key_private_template_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY userfeatures
    ADD CONSTRAINT userfeatures_func_key_private_template_id_fkey FOREIGN KEY (func_key_private_template_id) REFERENCES func_key_template(id);


--
-- Name: userfeatures_func_key_template_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asterisk
--

ALTER TABLE ONLY userfeatures
    ADD CONSTRAINT userfeatures_func_key_template_id_fkey FOREIGN KEY (func_key_template_id) REFERENCES func_key_template(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: accessfeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE accessfeatures FROM PUBLIC;
REVOKE ALL ON TABLE accessfeatures FROM asterisk;
GRANT ALL ON TABLE accessfeatures TO asterisk;


--
-- Name: accessfeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE accessfeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE accessfeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE accessfeatures_id_seq TO asterisk;


--
-- Name: accesswebservice; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE accesswebservice FROM PUBLIC;
REVOKE ALL ON TABLE accesswebservice FROM asterisk;
GRANT ALL ON TABLE accesswebservice TO asterisk;


--
-- Name: accesswebservice_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE accesswebservice_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE accesswebservice_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE accesswebservice_id_seq TO asterisk;


--
-- Name: agent_login_status; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE agent_login_status FROM PUBLIC;
REVOKE ALL ON TABLE agent_login_status FROM asterisk;
GRANT ALL ON TABLE agent_login_status TO asterisk;


--
-- Name: agent_membership_status; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE agent_membership_status FROM PUBLIC;
REVOKE ALL ON TABLE agent_membership_status FROM asterisk;
GRANT ALL ON TABLE agent_membership_status TO asterisk;


--
-- Name: agentfeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE agentfeatures FROM PUBLIC;
REVOKE ALL ON TABLE agentfeatures FROM asterisk;
GRANT ALL ON TABLE agentfeatures TO asterisk;


--
-- Name: agentfeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE agentfeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE agentfeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE agentfeatures_id_seq TO asterisk;


--
-- Name: agentglobalparams; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE agentglobalparams FROM PUBLIC;
REVOKE ALL ON TABLE agentglobalparams FROM asterisk;
GRANT ALL ON TABLE agentglobalparams TO asterisk;


--
-- Name: agentglobalparams_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE agentglobalparams_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE agentglobalparams_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE agentglobalparams_id_seq TO asterisk;


--
-- Name: agentgroup; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE agentgroup FROM PUBLIC;
REVOKE ALL ON TABLE agentgroup FROM asterisk;
GRANT ALL ON TABLE agentgroup TO asterisk;


--
-- Name: agentgroup_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE agentgroup_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE agentgroup_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE agentgroup_id_seq TO asterisk;


--
-- Name: agentqueueskill; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE agentqueueskill FROM PUBLIC;
REVOKE ALL ON TABLE agentqueueskill FROM asterisk;
GRANT ALL ON TABLE agentqueueskill TO asterisk;


--
-- Name: attachment; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE attachment FROM PUBLIC;
REVOKE ALL ON TABLE attachment FROM asterisk;
GRANT ALL ON TABLE attachment TO asterisk;


--
-- Name: attachment_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE attachment_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE attachment_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE attachment_id_seq TO asterisk;


--
-- Name: call_log; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE call_log FROM PUBLIC;
REVOKE ALL ON TABLE call_log FROM asterisk;
GRANT ALL ON TABLE call_log TO asterisk;


--
-- Name: call_log_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE call_log_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE call_log_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE call_log_id_seq TO asterisk;


--
-- Name: callerid; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE callerid FROM PUBLIC;
REVOKE ALL ON TABLE callerid FROM asterisk;
GRANT ALL ON TABLE callerid TO asterisk;


--
-- Name: callfilter; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE callfilter FROM PUBLIC;
REVOKE ALL ON TABLE callfilter FROM asterisk;
GRANT ALL ON TABLE callfilter TO asterisk;


--
-- Name: callfilter_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE callfilter_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE callfilter_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE callfilter_id_seq TO asterisk;


--
-- Name: callfiltermember; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE callfiltermember FROM PUBLIC;
REVOKE ALL ON TABLE callfiltermember FROM asterisk;
GRANT ALL ON TABLE callfiltermember TO asterisk;


--
-- Name: callfiltermember_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE callfiltermember_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE callfiltermember_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE callfiltermember_id_seq TO asterisk;


--
-- Name: cel; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cel FROM PUBLIC;
REVOKE ALL ON TABLE cel FROM asterisk;
GRANT ALL ON TABLE cel TO asterisk;


--
-- Name: cel_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE cel_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cel_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE cel_id_seq TO asterisk;


--
-- Name: context; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE context FROM PUBLIC;
REVOKE ALL ON TABLE context FROM asterisk;
GRANT ALL ON TABLE context TO asterisk;


--
-- Name: contextinclude; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE contextinclude FROM PUBLIC;
REVOKE ALL ON TABLE contextinclude FROM asterisk;
GRANT ALL ON TABLE contextinclude TO asterisk;


--
-- Name: contextmember; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE contextmember FROM PUBLIC;
REVOKE ALL ON TABLE contextmember FROM asterisk;
GRANT ALL ON TABLE contextmember TO asterisk;


--
-- Name: contextnumbers; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE contextnumbers FROM PUBLIC;
REVOKE ALL ON TABLE contextnumbers FROM asterisk;
GRANT ALL ON TABLE contextnumbers TO asterisk;


--
-- Name: contexttype; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE contexttype FROM PUBLIC;
REVOKE ALL ON TABLE contexttype FROM asterisk;
GRANT ALL ON TABLE contexttype TO asterisk;


--
-- Name: contexttype_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE contexttype_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE contexttype_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE contexttype_id_seq TO asterisk;


--
-- Name: cti_preference; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_preference FROM PUBLIC;
REVOKE ALL ON TABLE cti_preference FROM asterisk;
GRANT ALL ON TABLE cti_preference TO asterisk;


--
-- Name: cti_preference_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE cti_preference_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cti_preference_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE cti_preference_id_seq TO asterisk;


--
-- Name: cti_profile; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_profile FROM PUBLIC;
REVOKE ALL ON TABLE cti_profile FROM asterisk;
GRANT ALL ON TABLE cti_profile TO asterisk;


--
-- Name: cti_profile_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE cti_profile_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cti_profile_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE cti_profile_id_seq TO asterisk;


--
-- Name: cti_profile_preference; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_profile_preference FROM PUBLIC;
REVOKE ALL ON TABLE cti_profile_preference FROM asterisk;
GRANT ALL ON TABLE cti_profile_preference TO asterisk;


--
-- Name: cti_profile_service; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_profile_service FROM PUBLIC;
REVOKE ALL ON TABLE cti_profile_service FROM asterisk;
GRANT ALL ON TABLE cti_profile_service TO asterisk;


--
-- Name: cti_profile_xlet; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_profile_xlet FROM PUBLIC;
REVOKE ALL ON TABLE cti_profile_xlet FROM asterisk;
GRANT ALL ON TABLE cti_profile_xlet TO asterisk;


--
-- Name: cti_service; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_service FROM PUBLIC;
REVOKE ALL ON TABLE cti_service FROM asterisk;
GRANT ALL ON TABLE cti_service TO asterisk;


--
-- Name: cti_service_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE cti_service_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cti_service_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE cti_service_id_seq TO asterisk;


--
-- Name: cti_xlet; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_xlet FROM PUBLIC;
REVOKE ALL ON TABLE cti_xlet FROM asterisk;
GRANT ALL ON TABLE cti_xlet TO asterisk;


--
-- Name: cti_xlet_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE cti_xlet_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cti_xlet_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE cti_xlet_id_seq TO asterisk;


--
-- Name: cti_xlet_layout; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cti_xlet_layout FROM PUBLIC;
REVOKE ALL ON TABLE cti_xlet_layout FROM asterisk;
GRANT ALL ON TABLE cti_xlet_layout TO asterisk;


--
-- Name: cti_xlet_layout_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE cti_xlet_layout_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cti_xlet_layout_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE cti_xlet_layout_id_seq TO asterisk;


--
-- Name: cticontexts; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE cticontexts FROM PUBLIC;
REVOKE ALL ON TABLE cticontexts FROM asterisk;
GRANT ALL ON TABLE cticontexts TO asterisk;


--
-- Name: cticontexts_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE cticontexts_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE cticontexts_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE cticontexts_id_seq TO asterisk;


--
-- Name: ctidirectories; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctidirectories FROM PUBLIC;
REVOKE ALL ON TABLE ctidirectories FROM asterisk;
GRANT ALL ON TABLE ctidirectories TO asterisk;


--
-- Name: ctidirectories_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctidirectories_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctidirectories_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctidirectories_id_seq TO asterisk;


--
-- Name: ctidirectoryfields; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctidirectoryfields FROM PUBLIC;
REVOKE ALL ON TABLE ctidirectoryfields FROM asterisk;
GRANT ALL ON TABLE ctidirectoryfields TO asterisk;


--
-- Name: ctidisplays; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctidisplays FROM PUBLIC;
REVOKE ALL ON TABLE ctidisplays FROM asterisk;
GRANT ALL ON TABLE ctidisplays TO asterisk;


--
-- Name: ctidisplays_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctidisplays_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctidisplays_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctidisplays_id_seq TO asterisk;


--
-- Name: ctilog; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctilog FROM PUBLIC;
REVOKE ALL ON TABLE ctilog FROM asterisk;
GRANT ALL ON TABLE ctilog TO asterisk;


--
-- Name: ctilog_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctilog_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctilog_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctilog_id_seq TO asterisk;


--
-- Name: ctimain; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctimain FROM PUBLIC;
REVOKE ALL ON TABLE ctimain FROM asterisk;
GRANT ALL ON TABLE ctimain TO asterisk;


--
-- Name: ctimain_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctimain_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctimain_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctimain_id_seq TO asterisk;


--
-- Name: ctiphonehints; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctiphonehints FROM PUBLIC;
REVOKE ALL ON TABLE ctiphonehints FROM asterisk;
GRANT ALL ON TABLE ctiphonehints TO asterisk;


--
-- Name: ctiphonehints_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctiphonehints_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctiphonehints_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctiphonehints_id_seq TO asterisk;


--
-- Name: ctiphonehintsgroup; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctiphonehintsgroup FROM PUBLIC;
REVOKE ALL ON TABLE ctiphonehintsgroup FROM asterisk;
GRANT ALL ON TABLE ctiphonehintsgroup TO asterisk;


--
-- Name: ctiphonehintsgroup_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctiphonehintsgroup_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctiphonehintsgroup_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctiphonehintsgroup_id_seq TO asterisk;


--
-- Name: ctipresences; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctipresences FROM PUBLIC;
REVOKE ALL ON TABLE ctipresences FROM asterisk;
GRANT ALL ON TABLE ctipresences TO asterisk;


--
-- Name: ctipresences_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctipresences_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctipresences_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctipresences_id_seq TO asterisk;


--
-- Name: ctireversedirectories; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctireversedirectories FROM PUBLIC;
REVOKE ALL ON TABLE ctireversedirectories FROM asterisk;
GRANT ALL ON TABLE ctireversedirectories TO asterisk;


--
-- Name: ctireversedirectories_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctireversedirectories_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctireversedirectories_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctireversedirectories_id_seq TO asterisk;


--
-- Name: ctisheetactions; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctisheetactions FROM PUBLIC;
REVOKE ALL ON TABLE ctisheetactions FROM asterisk;
GRANT ALL ON TABLE ctisheetactions TO asterisk;


--
-- Name: ctisheetactions_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctisheetactions_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctisheetactions_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctisheetactions_id_seq TO asterisk;


--
-- Name: ctisheetevents; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctisheetevents FROM PUBLIC;
REVOKE ALL ON TABLE ctisheetevents FROM asterisk;
GRANT ALL ON TABLE ctisheetevents TO asterisk;


--
-- Name: ctisheetevents_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctisheetevents_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctisheetevents_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctisheetevents_id_seq TO asterisk;


--
-- Name: ctistatus; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ctistatus FROM PUBLIC;
REVOKE ALL ON TABLE ctistatus FROM asterisk;
GRANT ALL ON TABLE ctistatus TO asterisk;


--
-- Name: ctistatus_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ctistatus_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ctistatus_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ctistatus_id_seq TO asterisk;


--
-- Name: dhcp; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE dhcp FROM PUBLIC;
REVOKE ALL ON TABLE dhcp FROM asterisk;
GRANT ALL ON TABLE dhcp TO asterisk;


--
-- Name: dhcp_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE dhcp_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE dhcp_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE dhcp_id_seq TO asterisk;


--
-- Name: dialaction; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE dialaction FROM PUBLIC;
REVOKE ALL ON TABLE dialaction FROM asterisk;
GRANT ALL ON TABLE dialaction TO asterisk;


--
-- Name: dialpattern; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE dialpattern FROM PUBLIC;
REVOKE ALL ON TABLE dialpattern FROM asterisk;
GRANT ALL ON TABLE dialpattern TO asterisk;


--
-- Name: dialpattern_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE dialpattern_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE dialpattern_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE dialpattern_id_seq TO asterisk;


--
-- Name: directories; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE directories FROM PUBLIC;
REVOKE ALL ON TABLE directories FROM asterisk;
GRANT ALL ON TABLE directories TO asterisk;


--
-- Name: directories_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE directories_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE directories_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE directories_id_seq TO asterisk;


--
-- Name: entity; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE entity FROM PUBLIC;
REVOKE ALL ON TABLE entity FROM asterisk;
GRANT ALL ON TABLE entity TO asterisk;


--
-- Name: entity_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE entity_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE entity_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE entity_id_seq TO asterisk;


--
-- Name: extensions; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE extensions FROM PUBLIC;
REVOKE ALL ON TABLE extensions FROM asterisk;
GRANT ALL ON TABLE extensions TO asterisk;


--
-- Name: extensions_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE extensions_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE extensions_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE extensions_id_seq TO asterisk;


--
-- Name: features; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE features FROM PUBLIC;
REVOKE ALL ON TABLE features FROM asterisk;
GRANT ALL ON TABLE features TO asterisk;


--
-- Name: features_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE features_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE features_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE features_id_seq TO asterisk;


--
-- Name: func_key; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key FROM PUBLIC;
REVOKE ALL ON TABLE func_key FROM asterisk;
GRANT ALL ON TABLE func_key TO asterisk;


--
-- Name: func_key_dest_conference; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_dest_conference FROM PUBLIC;
REVOKE ALL ON TABLE func_key_dest_conference FROM asterisk;
GRANT ALL ON TABLE func_key_dest_conference TO asterisk;


--
-- Name: func_key_dest_group; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_dest_group FROM PUBLIC;
REVOKE ALL ON TABLE func_key_dest_group FROM asterisk;
GRANT ALL ON TABLE func_key_dest_group TO asterisk;


--
-- Name: func_key_dest_queue; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_dest_queue FROM PUBLIC;
REVOKE ALL ON TABLE func_key_dest_queue FROM asterisk;
GRANT ALL ON TABLE func_key_dest_queue TO asterisk;


--
-- Name: func_key_dest_user; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_dest_user FROM PUBLIC;
REVOKE ALL ON TABLE func_key_dest_user FROM asterisk;
GRANT ALL ON TABLE func_key_dest_user TO asterisk;


--
-- Name: func_key_destination_type; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_destination_type FROM PUBLIC;
REVOKE ALL ON TABLE func_key_destination_type FROM asterisk;
GRANT ALL ON TABLE func_key_destination_type TO asterisk;


--
-- Name: func_key_destination_type_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE func_key_destination_type_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE func_key_destination_type_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE func_key_destination_type_id_seq TO asterisk;


--
-- Name: func_key_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE func_key_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE func_key_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE func_key_id_seq TO asterisk;


--
-- Name: func_key_mapping; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_mapping FROM PUBLIC;
REVOKE ALL ON TABLE func_key_mapping FROM asterisk;
GRANT ALL ON TABLE func_key_mapping TO asterisk;


--
-- Name: func_key_template; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_template FROM PUBLIC;
REVOKE ALL ON TABLE func_key_template FROM asterisk;
GRANT ALL ON TABLE func_key_template TO asterisk;


--
-- Name: func_key_template_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE func_key_template_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE func_key_template_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE func_key_template_id_seq TO asterisk;


--
-- Name: func_key_type; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE func_key_type FROM PUBLIC;
REVOKE ALL ON TABLE func_key_type FROM asterisk;
GRANT ALL ON TABLE func_key_type TO asterisk;


--
-- Name: func_key_type_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE func_key_type_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE func_key_type_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE func_key_type_id_seq TO asterisk;


--
-- Name: general; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE general FROM PUBLIC;
REVOKE ALL ON TABLE general FROM asterisk;
GRANT ALL ON TABLE general TO asterisk;


--
-- Name: general_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE general_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE general_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE general_id_seq TO asterisk;


--
-- Name: groupfeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE groupfeatures FROM PUBLIC;
REVOKE ALL ON TABLE groupfeatures FROM asterisk;
GRANT ALL ON TABLE groupfeatures TO asterisk;


--
-- Name: groupfeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE groupfeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE groupfeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE groupfeatures_id_seq TO asterisk;


--
-- Name: iaxcallnumberlimits; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE iaxcallnumberlimits FROM PUBLIC;
REVOKE ALL ON TABLE iaxcallnumberlimits FROM asterisk;
GRANT ALL ON TABLE iaxcallnumberlimits TO asterisk;


--
-- Name: iaxcallnumberlimits_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE iaxcallnumberlimits_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE iaxcallnumberlimits_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE iaxcallnumberlimits_id_seq TO asterisk;


--
-- Name: incall; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE incall FROM PUBLIC;
REVOKE ALL ON TABLE incall FROM asterisk;
GRANT ALL ON TABLE incall TO asterisk;


--
-- Name: incall_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE incall_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE incall_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE incall_id_seq TO asterisk;


--
-- Name: ldapfilter; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ldapfilter FROM PUBLIC;
REVOKE ALL ON TABLE ldapfilter FROM asterisk;
GRANT ALL ON TABLE ldapfilter TO asterisk;


--
-- Name: ldapfilter_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ldapfilter_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ldapfilter_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ldapfilter_id_seq TO asterisk;


--
-- Name: ldapserver; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE ldapserver FROM PUBLIC;
REVOKE ALL ON TABLE ldapserver FROM asterisk;
GRANT ALL ON TABLE ldapserver TO asterisk;


--
-- Name: ldapserver_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE ldapserver_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE ldapserver_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE ldapserver_id_seq TO asterisk;


--
-- Name: linefeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE linefeatures FROM PUBLIC;
REVOKE ALL ON TABLE linefeatures FROM asterisk;
GRANT ALL ON TABLE linefeatures TO asterisk;


--
-- Name: linefeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE linefeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE linefeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE linefeatures_id_seq TO asterisk;


--
-- Name: mail; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE mail FROM PUBLIC;
REVOKE ALL ON TABLE mail FROM asterisk;
GRANT ALL ON TABLE mail TO asterisk;


--
-- Name: mail_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE mail_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE mail_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE mail_id_seq TO asterisk;


--
-- Name: meetmefeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE meetmefeatures FROM PUBLIC;
REVOKE ALL ON TABLE meetmefeatures FROM asterisk;
GRANT ALL ON TABLE meetmefeatures TO asterisk;


--
-- Name: meetmefeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE meetmefeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE meetmefeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE meetmefeatures_id_seq TO asterisk;


--
-- Name: meetmeguest; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE meetmeguest FROM PUBLIC;
REVOKE ALL ON TABLE meetmeguest FROM asterisk;
GRANT ALL ON TABLE meetmeguest TO asterisk;


--
-- Name: meetmeguest_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE meetmeguest_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE meetmeguest_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE meetmeguest_id_seq TO asterisk;


--
-- Name: monitoring; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE monitoring FROM PUBLIC;
REVOKE ALL ON TABLE monitoring FROM asterisk;
GRANT ALL ON TABLE monitoring TO asterisk;


--
-- Name: monitoring_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE monitoring_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE monitoring_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE monitoring_id_seq TO asterisk;


--
-- Name: musiconhold; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE musiconhold FROM PUBLIC;
REVOKE ALL ON TABLE musiconhold FROM asterisk;
GRANT ALL ON TABLE musiconhold TO asterisk;


--
-- Name: musiconhold_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE musiconhold_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE musiconhold_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE musiconhold_id_seq TO asterisk;


--
-- Name: netiface; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE netiface FROM PUBLIC;
REVOKE ALL ON TABLE netiface FROM asterisk;
GRANT ALL ON TABLE netiface TO asterisk;


--
-- Name: netiface_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE netiface_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE netiface_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE netiface_id_seq TO asterisk;


--
-- Name: outcall; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE outcall FROM PUBLIC;
REVOKE ALL ON TABLE outcall FROM asterisk;
GRANT ALL ON TABLE outcall TO asterisk;


--
-- Name: outcall_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE outcall_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE outcall_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE outcall_id_seq TO asterisk;


--
-- Name: outcalltrunk; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE outcalltrunk FROM PUBLIC;
REVOKE ALL ON TABLE outcalltrunk FROM asterisk;
GRANT ALL ON TABLE outcalltrunk TO asterisk;


--
-- Name: paging; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE paging FROM PUBLIC;
REVOKE ALL ON TABLE paging FROM asterisk;
GRANT ALL ON TABLE paging TO asterisk;


--
-- Name: paging_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE paging_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE paging_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE paging_id_seq TO asterisk;


--
-- Name: paginguser; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE paginguser FROM PUBLIC;
REVOKE ALL ON TABLE paginguser FROM asterisk;
GRANT ALL ON TABLE paginguser TO asterisk;


--
-- Name: phonebook; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE phonebook FROM PUBLIC;
REVOKE ALL ON TABLE phonebook FROM asterisk;
GRANT ALL ON TABLE phonebook TO asterisk;


--
-- Name: phonebook_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE phonebook_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE phonebook_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE phonebook_id_seq TO asterisk;


--
-- Name: phonebookaddress; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE phonebookaddress FROM PUBLIC;
REVOKE ALL ON TABLE phonebookaddress FROM asterisk;
GRANT ALL ON TABLE phonebookaddress TO asterisk;


--
-- Name: phonebookaddress_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE phonebookaddress_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE phonebookaddress_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE phonebookaddress_id_seq TO asterisk;


--
-- Name: phonebooknumber; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE phonebooknumber FROM PUBLIC;
REVOKE ALL ON TABLE phonebooknumber FROM asterisk;
GRANT ALL ON TABLE phonebooknumber TO asterisk;


--
-- Name: phonebooknumber_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE phonebooknumber_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE phonebooknumber_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE phonebooknumber_id_seq TO asterisk;


--
-- Name: phonefunckey; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE phonefunckey FROM PUBLIC;
REVOKE ALL ON TABLE phonefunckey FROM asterisk;
GRANT ALL ON TABLE phonefunckey TO asterisk;


--
-- Name: pickup; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE pickup FROM PUBLIC;
REVOKE ALL ON TABLE pickup FROM asterisk;
GRANT ALL ON TABLE pickup TO asterisk;


--
-- Name: pickupmember; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE pickupmember FROM PUBLIC;
REVOKE ALL ON TABLE pickupmember FROM asterisk;
GRANT ALL ON TABLE pickupmember TO asterisk;


--
-- Name: provisioning; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE provisioning FROM PUBLIC;
REVOKE ALL ON TABLE provisioning FROM asterisk;
GRANT ALL ON TABLE provisioning TO asterisk;


--
-- Name: provisioning_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE provisioning_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE provisioning_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE provisioning_id_seq TO asterisk;


--
-- Name: queue; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queue FROM PUBLIC;
REVOKE ALL ON TABLE queue FROM asterisk;
GRANT ALL ON TABLE queue TO asterisk;


--
-- Name: queue_info; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queue_info FROM PUBLIC;
REVOKE ALL ON TABLE queue_info FROM asterisk;
GRANT ALL ON TABLE queue_info TO asterisk;


--
-- Name: queue_info_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE queue_info_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE queue_info_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE queue_info_id_seq TO asterisk;


--
-- Name: queue_log; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queue_log FROM PUBLIC;
REVOKE ALL ON TABLE queue_log FROM asterisk;
GRANT ALL ON TABLE queue_log TO asterisk;


--
-- Name: queue_log_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE queue_log_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE queue_log_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE queue_log_id_seq TO asterisk;


--
-- Name: queuefeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queuefeatures FROM PUBLIC;
REVOKE ALL ON TABLE queuefeatures FROM asterisk;
GRANT ALL ON TABLE queuefeatures TO asterisk;


--
-- Name: queuefeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE queuefeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE queuefeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE queuefeatures_id_seq TO asterisk;


--
-- Name: queuemember; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queuemember FROM PUBLIC;
REVOKE ALL ON TABLE queuemember FROM asterisk;
GRANT ALL ON TABLE queuemember TO asterisk;


--
-- Name: queuepenalty; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queuepenalty FROM PUBLIC;
REVOKE ALL ON TABLE queuepenalty FROM asterisk;
GRANT ALL ON TABLE queuepenalty TO asterisk;


--
-- Name: queuepenalty_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE queuepenalty_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE queuepenalty_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE queuepenalty_id_seq TO asterisk;


--
-- Name: queuepenaltychange; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queuepenaltychange FROM PUBLIC;
REVOKE ALL ON TABLE queuepenaltychange FROM asterisk;
GRANT ALL ON TABLE queuepenaltychange TO asterisk;


--
-- Name: queueskill; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queueskill FROM PUBLIC;
REVOKE ALL ON TABLE queueskill FROM asterisk;
GRANT ALL ON TABLE queueskill TO asterisk;


--
-- Name: queueskill_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE queueskill_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE queueskill_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE queueskill_id_seq TO asterisk;


--
-- Name: queueskillcat; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queueskillcat FROM PUBLIC;
REVOKE ALL ON TABLE queueskillcat FROM asterisk;
GRANT ALL ON TABLE queueskillcat TO asterisk;


--
-- Name: queueskillcat_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE queueskillcat_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE queueskillcat_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE queueskillcat_id_seq TO asterisk;


--
-- Name: queueskillrule; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE queueskillrule FROM PUBLIC;
REVOKE ALL ON TABLE queueskillrule FROM asterisk;
GRANT ALL ON TABLE queueskillrule TO asterisk;


--
-- Name: queueskillrule_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE queueskillrule_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE queueskillrule_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE queueskillrule_id_seq TO asterisk;


--
-- Name: record_campaign_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE record_campaign_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE record_campaign_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE record_campaign_id_seq TO asterisk;


--
-- Name: resolvconf; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE resolvconf FROM PUBLIC;
REVOKE ALL ON TABLE resolvconf FROM asterisk;
GRANT ALL ON TABLE resolvconf TO asterisk;


--
-- Name: resolvconf_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE resolvconf_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE resolvconf_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE resolvconf_id_seq TO asterisk;


--
-- Name: rightcall; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE rightcall FROM PUBLIC;
REVOKE ALL ON TABLE rightcall FROM asterisk;
GRANT ALL ON TABLE rightcall TO asterisk;


--
-- Name: rightcall_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE rightcall_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE rightcall_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE rightcall_id_seq TO asterisk;


--
-- Name: rightcallexten; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE rightcallexten FROM PUBLIC;
REVOKE ALL ON TABLE rightcallexten FROM asterisk;
GRANT ALL ON TABLE rightcallexten TO asterisk;


--
-- Name: rightcallexten_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE rightcallexten_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE rightcallexten_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE rightcallexten_id_seq TO asterisk;


--
-- Name: rightcallmember; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE rightcallmember FROM PUBLIC;
REVOKE ALL ON TABLE rightcallmember FROM asterisk;
GRANT ALL ON TABLE rightcallmember TO asterisk;


--
-- Name: rightcallmember_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE rightcallmember_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE rightcallmember_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE rightcallmember_id_seq TO asterisk;


--
-- Name: sccpdevice; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE sccpdevice FROM PUBLIC;
REVOKE ALL ON TABLE sccpdevice FROM asterisk;
GRANT ALL ON TABLE sccpdevice TO asterisk;


--
-- Name: sccpdevice_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE sccpdevice_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE sccpdevice_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE sccpdevice_id_seq TO asterisk;


--
-- Name: sccpgeneralsettings; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE sccpgeneralsettings FROM PUBLIC;
REVOKE ALL ON TABLE sccpgeneralsettings FROM asterisk;
GRANT ALL ON TABLE sccpgeneralsettings TO asterisk;


--
-- Name: sccpgeneralsettings_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE sccpgeneralsettings_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE sccpgeneralsettings_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE sccpgeneralsettings_id_seq TO asterisk;


--
-- Name: sccpline; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE sccpline FROM PUBLIC;
REVOKE ALL ON TABLE sccpline FROM asterisk;
GRANT ALL ON TABLE sccpline TO asterisk;


--
-- Name: sccpline_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE sccpline_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE sccpline_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE sccpline_id_seq TO asterisk;


--
-- Name: schedule; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE schedule FROM PUBLIC;
REVOKE ALL ON TABLE schedule FROM asterisk;
GRANT ALL ON TABLE schedule TO asterisk;


--
-- Name: schedule_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE schedule_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE schedule_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE schedule_id_seq TO asterisk;


--
-- Name: schedule_path; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE schedule_path FROM PUBLIC;
REVOKE ALL ON TABLE schedule_path FROM asterisk;
GRANT ALL ON TABLE schedule_path TO asterisk;


--
-- Name: schedule_time; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE schedule_time FROM PUBLIC;
REVOKE ALL ON TABLE schedule_time FROM asterisk;
GRANT ALL ON TABLE schedule_time TO asterisk;


--
-- Name: schedule_time_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE schedule_time_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE schedule_time_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE schedule_time_id_seq TO asterisk;


--
-- Name: serverfeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE serverfeatures FROM PUBLIC;
REVOKE ALL ON TABLE serverfeatures FROM asterisk;
GRANT ALL ON TABLE serverfeatures TO asterisk;


--
-- Name: serverfeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE serverfeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE serverfeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE serverfeatures_id_seq TO asterisk;


--
-- Name: session; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE session FROM PUBLIC;
REVOKE ALL ON TABLE session FROM asterisk;
GRANT ALL ON TABLE session TO asterisk;


--
-- Name: sipauthentication; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE sipauthentication FROM PUBLIC;
REVOKE ALL ON TABLE sipauthentication FROM asterisk;
GRANT ALL ON TABLE sipauthentication TO asterisk;


--
-- Name: sipauthentication_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE sipauthentication_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE sipauthentication_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE sipauthentication_id_seq TO asterisk;


--
-- Name: stat_agent; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stat_agent FROM PUBLIC;
REVOKE ALL ON TABLE stat_agent FROM asterisk;
GRANT ALL ON TABLE stat_agent TO asterisk;


--
-- Name: stat_agent_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE stat_agent_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE stat_agent_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE stat_agent_id_seq TO asterisk;


--
-- Name: stat_agent_periodic; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stat_agent_periodic FROM PUBLIC;
REVOKE ALL ON TABLE stat_agent_periodic FROM asterisk;
GRANT ALL ON TABLE stat_agent_periodic TO asterisk;


--
-- Name: stat_agent_periodic_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE stat_agent_periodic_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE stat_agent_periodic_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE stat_agent_periodic_id_seq TO asterisk;


--
-- Name: stat_call_on_queue; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stat_call_on_queue FROM PUBLIC;
REVOKE ALL ON TABLE stat_call_on_queue FROM asterisk;
GRANT ALL ON TABLE stat_call_on_queue TO asterisk;


--
-- Name: stat_call_on_queue_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE stat_call_on_queue_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE stat_call_on_queue_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE stat_call_on_queue_id_seq TO asterisk;


--
-- Name: stat_queue; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stat_queue FROM PUBLIC;
REVOKE ALL ON TABLE stat_queue FROM asterisk;
GRANT ALL ON TABLE stat_queue TO asterisk;


--
-- Name: stat_queue_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE stat_queue_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE stat_queue_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE stat_queue_id_seq TO asterisk;


--
-- Name: stat_queue_periodic; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stat_queue_periodic FROM PUBLIC;
REVOKE ALL ON TABLE stat_queue_periodic FROM asterisk;
GRANT ALL ON TABLE stat_queue_periodic TO asterisk;


--
-- Name: stat_queue_periodic_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE stat_queue_periodic_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE stat_queue_periodic_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE stat_queue_periodic_id_seq TO asterisk;


--
-- Name: staticiax; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE staticiax FROM PUBLIC;
REVOKE ALL ON TABLE staticiax FROM asterisk;
GRANT ALL ON TABLE staticiax TO asterisk;


--
-- Name: staticiax_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE staticiax_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE staticiax_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE staticiax_id_seq TO asterisk;


--
-- Name: staticmeetme; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE staticmeetme FROM PUBLIC;
REVOKE ALL ON TABLE staticmeetme FROM asterisk;
GRANT ALL ON TABLE staticmeetme TO asterisk;


--
-- Name: staticmeetme_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE staticmeetme_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE staticmeetme_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE staticmeetme_id_seq TO asterisk;


--
-- Name: staticqueue; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE staticqueue FROM PUBLIC;
REVOKE ALL ON TABLE staticqueue FROM asterisk;
GRANT ALL ON TABLE staticqueue TO asterisk;


--
-- Name: staticqueue_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE staticqueue_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE staticqueue_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE staticqueue_id_seq TO asterisk;


--
-- Name: staticsip; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE staticsip FROM PUBLIC;
REVOKE ALL ON TABLE staticsip FROM asterisk;
GRANT ALL ON TABLE staticsip TO asterisk;


--
-- Name: staticsip_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE staticsip_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE staticsip_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE staticsip_id_seq TO asterisk;


--
-- Name: staticvoicemail; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE staticvoicemail FROM PUBLIC;
REVOKE ALL ON TABLE staticvoicemail FROM asterisk;
GRANT ALL ON TABLE staticvoicemail TO asterisk;


--
-- Name: staticvoicemail_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE staticvoicemail_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE staticvoicemail_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE staticvoicemail_id_seq TO asterisk;


--
-- Name: stats_conf; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stats_conf FROM PUBLIC;
REVOKE ALL ON TABLE stats_conf FROM asterisk;
GRANT ALL ON TABLE stats_conf TO asterisk;


--
-- Name: stats_conf_agent; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stats_conf_agent FROM PUBLIC;
REVOKE ALL ON TABLE stats_conf_agent FROM asterisk;
GRANT ALL ON TABLE stats_conf_agent TO asterisk;


--
-- Name: stats_conf_group; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stats_conf_group FROM PUBLIC;
REVOKE ALL ON TABLE stats_conf_group FROM asterisk;
GRANT ALL ON TABLE stats_conf_group TO asterisk;


--
-- Name: stats_conf_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE stats_conf_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE stats_conf_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE stats_conf_id_seq TO asterisk;


--
-- Name: stats_conf_incall; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stats_conf_incall FROM PUBLIC;
REVOKE ALL ON TABLE stats_conf_incall FROM asterisk;
GRANT ALL ON TABLE stats_conf_incall TO asterisk;


--
-- Name: stats_conf_queue; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stats_conf_queue FROM PUBLIC;
REVOKE ALL ON TABLE stats_conf_queue FROM asterisk;
GRANT ALL ON TABLE stats_conf_queue TO asterisk;


--
-- Name: stats_conf_user; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stats_conf_user FROM PUBLIC;
REVOKE ALL ON TABLE stats_conf_user FROM asterisk;
GRANT ALL ON TABLE stats_conf_user TO asterisk;


--
-- Name: stats_conf_xivouser; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE stats_conf_xivouser FROM PUBLIC;
REVOKE ALL ON TABLE stats_conf_xivouser FROM asterisk;
GRANT ALL ON TABLE stats_conf_xivouser TO asterisk;


--
-- Name: trunkfeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE trunkfeatures FROM PUBLIC;
REVOKE ALL ON TABLE trunkfeatures FROM asterisk;
GRANT ALL ON TABLE trunkfeatures TO asterisk;


--
-- Name: trunkfeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE trunkfeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE trunkfeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE trunkfeatures_id_seq TO asterisk;


--
-- Name: user; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE "user" FROM PUBLIC;
REVOKE ALL ON TABLE "user" FROM asterisk;
GRANT ALL ON TABLE "user" TO asterisk;


--
-- Name: user_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE user_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE user_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE user_id_seq TO asterisk;


--
-- Name: user_line; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE user_line FROM PUBLIC;
REVOKE ALL ON TABLE user_line FROM asterisk;
GRANT ALL ON TABLE user_line TO asterisk;


--
-- Name: user_line_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE user_line_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE user_line_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE user_line_id_seq TO asterisk;


--
-- Name: usercustom; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE usercustom FROM PUBLIC;
REVOKE ALL ON TABLE usercustom FROM asterisk;
GRANT ALL ON TABLE usercustom TO asterisk;


--
-- Name: usercustom_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE usercustom_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE usercustom_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE usercustom_id_seq TO asterisk;


--
-- Name: userfeatures; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE userfeatures FROM PUBLIC;
REVOKE ALL ON TABLE userfeatures FROM asterisk;
GRANT ALL ON TABLE userfeatures TO asterisk;


--
-- Name: userfeatures_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE userfeatures_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE userfeatures_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE userfeatures_id_seq TO asterisk;


--
-- Name: useriax; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE useriax FROM PUBLIC;
REVOKE ALL ON TABLE useriax FROM asterisk;
GRANT ALL ON TABLE useriax TO asterisk;


--
-- Name: useriax_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE useriax_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE useriax_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE useriax_id_seq TO asterisk;


--
-- Name: usersip; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE usersip FROM PUBLIC;
REVOKE ALL ON TABLE usersip FROM asterisk;
GRANT ALL ON TABLE usersip TO asterisk;


--
-- Name: usersip_id_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE usersip_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE usersip_id_seq FROM asterisk;
GRANT ALL ON SEQUENCE usersip_id_seq TO asterisk;


--
-- Name: voicemail; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON TABLE voicemail FROM PUBLIC;
REVOKE ALL ON TABLE voicemail FROM asterisk;
GRANT ALL ON TABLE voicemail TO asterisk;


--
-- Name: voicemail_uniqueid_seq; Type: ACL; Schema: public; Owner: asterisk
--

REVOKE ALL ON SEQUENCE voicemail_uniqueid_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE voicemail_uniqueid_seq FROM asterisk;
GRANT ALL ON SEQUENCE voicemail_uniqueid_seq TO asterisk;


--
-- PostgreSQL database dump complete
--

