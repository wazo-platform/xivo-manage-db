/*
 * Copyright (C) 2014  Avencall
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

BEGIN;

DROP TABLE IF EXISTS "operator" CASCADE;

DROP TABLE IF EXISTS "operator_destination" CASCADE;

DROP TABLE IF EXISTS "operator_trunk" CASCADE;

DROP TABLE IF EXISTS "outcalldundipeer" CASCADE;

DROP TABLE IF EXISTS "parkinglot" CASCADE;

DROP TABLE IF EXISTS "voicemenu" CASCADE;

ALTER TABLE "accessfeatures" RENAME COLUMN "feature" to "feature_old";
ALTER TABLE "accessfeatures"
    ADD COLUMN "feature" VARCHAR(64) DEFAULT 'phonebook' NOT NULL CHECK("feature"='phonebook'),
    DROP COLUMN "feature_old",
    ADD CONSTRAINT "accessfeatures_host_feature_key" UNIQUE ("host", "feature");
DROP TYPE IF EXISTS "accessfeatures_feature";

DROP INDEX IF EXISTS "agentfeatures__uidx__number";
ALTER TABLE "agentfeatures"
    ADD CONSTRAINT "agentfeatures_number_key" UNIQUE (number),
    ALTER "group" DROP DEFAULT;

ALTER TABLE "agentgroup" ALTER "description" DROP NOT NULL;

DROP INDEX IF EXISTS "attachment__uidx__object_type__object_id";
ALTER TABLE "attachment"
    ADD CONSTRAINT "attachment_pkey" PRIMARY KEY (id),
    ADD CONSTRAINT "attachment_object_type_object_id_key" UNIQUE (object_type, object_id);

DROP INDEX IF EXISTS "callfilter__uidx__name";
ALTER TABLE "callfilter"
    ADD UNIQUE (name);

DROP INDEX IF EXISTS "callfiltermember__uidx__callfilterid_type_typeval";
ALTER TABLE "callfiltermember"
    ALTER "typeval" SET DEFAULT '0',
    ALTER "bstype" SET NOT NULL,
    ADD CONSTRAINT "callfiltermember_callfilterid_type_typeval_key" UNIQUE (callfilterid, type, typeval);

DROP INDEX IF EXISTS "contexttype__uidx__name";
ALTER TABLE "contexttype"
    ADD CONSTRAINT "contexttype_name_key" UNIQUE (name);

ALTER TABLE "cti_profile" ALTER "name" SET NOT NULL;

ALTER TABLE "cticontexts" ALTER "description" DROP NOT NULL;

ALTER TABLE "ctidisplays" ALTER "description" DROP NOT NULL;

ALTER TABLE "ctiphonehintsgroup" ALTER "name" SET NOT NULL;

ALTER TABLE "ctipresences" ALTER "name" SET NOT NULL;

DROP INDEX IF EXISTS "ctistatus_presence_name";
ALTER TABLE "ctistatus"
    ALTER "name" SET NOT NULL,
    ADD CONSTRAINT "ctistatus_presence_id_name_key" UNIQUE (presence_id, name);

ALTER TABLE "dialaction"
    ALTER "actionarg1" DROP DEFAULT,
    ALTER "actionarg2" DROP DEFAULT;

DROP INDEX IF EXISTS "dialpattern__idx__type_typeid";

DROP INDEX IF EXISTS "extensions__uidx__exten_context";
ALTER TABLE "extensions"
    ADD CONSTRAINT "extensions_exten_context_key" UNIQUE (exten, context);

ALTER TABLE "func_key_mapping"
    DROP CONSTRAINT "func_key_mapping_pkey",
    ADD PRIMARY KEY ("template_id", "func_key_id", "destination_type_id");

ALTER TABLE "general" ALTER "exchange_exten" DROP DEFAULT;

DROP INDEX IF EXISTS "incall__uidx__exten_context";
ALTER TABLE "incall"
    ADD CONSTRAINT "incall_exten_context_key" UNIQUE (exten, context);

DROP INDEX IF EXISTS "ldapfilter__uidx__name";
ALTER TABLE "ldapfilter"
    ADD CONSTRAINT "ldapfilter_name_key" UNIQUE (name);

DROP INDEX IF EXISTS "linefeatures__uidx__name";
DROP INDEX IF EXISTS "linefeatures__uidx__protocol_protocolid";
ALTER TABLE "linefeatures"
    ADD CONSTRAINT "linefeatures_protocol_protocolid_key" UNIQUE (protocol, protocolid),
    ADD CONSTRAINT "linefeatures_name_key" UNIQUE (name);

DROP INDEX IF EXISTS "meetmefeatures__uidx__meetmeid";
DROP INDEX IF EXISTS "meetmefeatures__uidx__name";
ALTER TABLE "meetmefeatures"
    ADD CONSTRAINT "meetmefeatures_meetmeid_key" UNIQUE (meetmeid),
    ADD CONSTRAINT "meetmefeatures_name_key" UNIQUE (name);

DROP INDEX IF EXISTS "musiconhold__uidx__filename_category_var_name";
ALTER TABLE "musiconhold"
    ADD UNIQUE ("filename", "category", "var_name");

DROP INDEX IF EXISTS "outcall__uidx__name";
ALTER TABLE "outcall"
    ADD CONSTRAINT "outcall_name_key" UNIQUE (name),
    ALTER "description" DROP NOT NULL;

DROP INDEX IF EXISTS "paging__uidx__number";
ALTER TABLE "paging"
    ADD CONSTRAINT "paging_number_key" UNIQUE (number);

ALTER TABLE "pickup"
    ALTER "description" DROP DEFAULT,
    ALTER "description" DROP NOT NULL;

DO $$ 
    BEGIN
		ALTER TABLE "queue_log" ADD COLUMN "id" SERIAL PRIMARY KEY;
		GRANT ALL ON SEQUENCE "queue_log_id_seq" TO asterisk;
	EXCEPTION
		WHEN duplicate_column THEN RAISE NOTICE 'column id already exists in queue_log.';
    END;
$$;

ALTER TABLE "queue" ALTER "defaultrule" DROP DEFAULT;

DROP INDEX IF EXISTS "queuefeatures__uidx__name";
ALTER TABLE "queuefeatures"
    ADD UNIQUE ("name");

DROP INDEX IF EXISTS "queuemember__uidx__queue_name_channel_usertype_userid_category";
ALTER TABLE "queuemember"
    ADD UNIQUE ("queue_name", "channel", "usertype", "userid", "category");

DROP INDEX IF EXISTS "queueskill__idx__catid";
DROP INDEX IF EXISTS "queueskill__uidx__name";
ALTER TABLE "queueskill"
    ADD UNIQUE ("name");

DROP INDEX IF EXISTS "queueskillcat__uidx__name";
ALTER TABLE "queueskillcat"
    ADD CONSTRAINT "queueskillcat_name_key" UNIQUE (name);

ALTER TABLE "record_campaign"
    DROP CONSTRAINT IF EXISTS "campaign_name_u",
    ADD CONSTRAINT "record_campaign_campaign_name_key" UNIQUE (campaign_name);

DROP INDEX IF EXISTS "rightcall__uidx__name";
ALTER TABLE "rightcall"
    ALTER "description" DROP NOT NULL,
    ADD CONSTRAINT "rightcall_name_key" UNIQUE (name);

DROP INDEX IF EXISTS "rightcallexten__uidx__rightcallid_exten";
ALTER TABLE "rightcallexten"
    ADD CONSTRAINT "rightcallexten_rightcallid_exten_key" UNIQUE (rightcallid, exten);

DROP INDEX IF EXISTS "rightcallmember__uidx__rightcallid_type_typeval";
ALTER TABLE "rightcallmember"
    ALTER "typeval" SET DEFAULT '0',
    ADD CONSTRAINT "rightcallmember_rightcallid_type_typeval_key" UNIQUE (rightcallid, type, typeval);

ALTER TABLE "schedule"
    ALTER "timezone" DROP DEFAULT,
    ALTER "fallback_actionid" DROP DEFAULT,
    ALTER "fallback_actionargs" DROP DEFAULT;

ALTER TABLE "schedule_time"
    ALTER "hours" DROP DEFAULT,
    ALTER "weekdays" DROP DEFAULT,
    ALTER "monthdays" DROP DEFAULT,
    ALTER "months" DROP DEFAULT,
    ALTER "actionid" DROP DEFAULT,
    ALTER "actionargs" DROP DEFAULT;

ALTER TABLE "serverfeatures" RENAME COLUMN "feature" to "feature_old";
ALTER TABLE "serverfeatures"
    ADD COLUMN "feature" VARCHAR(64) DEFAULT 'phonebook' NOT NULL CHECK("feature"='phonebook'),
    DROP COLUMN "feature_old",
    ADD CONSTRAINT "serverfeatures_serverid_feature_type_key" UNIQUE (serverid, feature, type);
DROP TYPE IF EXISTS "serverfeatures_feature";

DROP INDEX IF EXISTS "trunkfeatures__uidx__protocol_protocolid";
ALTER TABLE "trunkfeatures"
    ADD CONSTRAINT "trunkfeatures_protocol_protocolid_key" UNIQUE (protocol, protocolid),
    ALTER "description" DROP NOT NULL;

DROP INDEX IF EXISTS "user_line_extension__uidx__user_id_line_id";
ALTER TABLE "user_line"
    DROP CONSTRAINT "user_line__extensions_id_fkey",
    ADD FOREIGN KEY ("extension_id") REFERENCES "extensions"("id"),
    DROP CONSTRAINT "user_line__linefeatures_id_fkey",
    ADD FOREIGN KEY ("line_id") REFERENCES "linefeatures"("id"),
    DROP CONSTRAINT "user_line__userfeatures_id_fkey",
    ADD FOREIGN KEY ("user_id") REFERENCES "userfeatures"("id"),
    ADD CONSTRAINT "user_line_user_id_line_id_key" UNIQUE (user_id, line_id);

DROP INDEX IF EXISTS "usercustom__uidx__interface_intfsuffix_category";
ALTER TABLE "usercustom"
    ADD CONSTRAINT "usercustom_interface_intfsuffix_category_key" UNIQUE (interface, intfsuffix, category);

DROP INDEX IF EXISTS "useriax__uidx__name";
ALTER TABLE "useriax"
    ADD CONSTRAINT "useriax_name_key" UNIQUE (name);

DROP INDEX IF EXISTS "usersip__uidx__name";
ALTER TABLE "usersip"
    ADD CONSTRAINT "usersip_name_key" UNIQUE (name),
    ALTER "transport" DROP DEFAULT,
    ALTER "remotesecret" DROP DEFAULT,
    ALTER "callbackextension" DROP DEFAULT,
    ALTER "contactpermit" DROP DEFAULT,
    ALTER "contactdeny" DROP DEFAULT,
    ALTER "unsolicited_mailbox" DROP DEFAULT,
    ALTER "disallowed_methods" DROP DEFAULT;

DROP INDEX IF EXISTS "voicemail__uidx__mailbox_context";
ALTER TABLE "voicemail"
    ADD CONSTRAINT "voicemail_mailbox_context_key" UNIQUE (mailbox, context);


COMMIT;
