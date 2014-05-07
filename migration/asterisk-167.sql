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

ALTER TABLE "agentfeatures" ALTER "group" DROP DEFAULT;
ALTER TABLE "agentgroup" ALTER "description" DROP NOT NULL;
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
ALTER TABLE "general" ALTER "exchange_exten" DROP DEFAULT;
ALTER TABLE "outcall" ALTER "description" DROP NOT NULL;
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

COMMIT;
