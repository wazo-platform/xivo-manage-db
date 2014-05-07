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

DROP INDEX IF EXISTS "agentfeatures__uidx__number";
ALTER TABLE "agentfeatures"
    ADD CONSTRAINT "agentfeatures_number_key" UNIQUE (number),
    ALTER "group" DROP DEFAULT;

ALTER TABLE "agentgroup" ALTER "description" DROP NOT NULL;

DROP INDEX IF EXISTS "callfilter__uidx__name";
ALTER TABLE "callfilter"
    ADD CONSTRAINT "callfilter_name_key" UNIQUE (name);

ALTER TABLE "callfiltermember"
	ALTER "bstype" SET NOT NULL,
	ALTER "typeval" SET DEFAULT '0';

ALTER TABLE "cti_profile" ALTER "name" SET NOT NULL;

ALTER TABLE "cticontexts" ALTER "description" DROP NOT NULL;

ALTER TABLE "ctidisplays" ALTER "description" DROP NOT NULL;

ALTER TABLE "ctiphonehintsgroup" ALTER "name" SET NOT NULL;

ALTER TABLE "ctipresences" ALTER "name" SET NOT NULL;

ALTER TABLE "ctistatus" ALTER "name" SET NOT NULL;

ALTER TABLE "dialaction"
	ALTER "actionarg1" DROP DEFAULT,
	ALTER "actionarg2" DROP DEFAULT;

ALTER TABLE "func_key_mapping"
	DROP CONSTRAINT "func_key_mapping_pkey",
	ADD PRIMARY KEY ("template_id", "func_key_id", "destination_type_id");

ALTER TABLE "general" ALTER "exchange_exten" DROP DEFAULT;

DROP INDEX IF EXISTS "outcall__uidx__name";
ALTER TABLE "outcall"
    ADD CONSTRAINT "outcall_name_key" UNIQUE (name),
    ALTER "description" DROP NOT NULL;

ALTER TABLE "pickup"
	ALTER "description" DROP DEFAULT,
	ALTER "description" DROP NOT NULL;

ALTER TABLE "queue" ALTER "defaultrule" DROP DEFAULT;

ALTER TABLE "rightcall" ALTER "description" DROP NOT NULL;

ALTER TABLE "rightcallmember" ALTER "typeval" SET DEFAULT '0';

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

ALTER TABLE "user_line"
	DROP CONSTRAINT "user_line__extensions_id_fkey",
	ADD FOREIGN KEY ("extension_id") REFERENCES "extensions"("id"),
	DROP CONSTRAINT "user_line__linefeatures_id_fkey",
	ADD FOREIGN KEY ("line_id") REFERENCES "linefeatures"("id"),
	DROP CONSTRAINT "user_line__userfeatures_id_fkey",
	ADD FOREIGN KEY ("user_id") REFERENCES "userfeatures"("id");


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

DROP INDEX IF EXISTS "queueskill__idx__catid";

COMMIT;
