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

ALTER TABLE "agentgroup" ALTER "description" DROP NOT NULL;
ALTER TABLE "callfiltermember" ALTER "bstype" SET NOT NULL;
ALTER TABLE "cti_profile" ALTER "name" SET NOT NULL;
ALTER TABLE "cticontexts" ALTER "description" DROP NOT NULL;
ALTER TABLE "ctidisplays" ALTER "description" DROP NOT NULL;
ALTER TABLE "ctiphonehintsgroup" ALTER "name" SET NOT NULL;
ALTER TABLE "ctipresences" ALTER "name" SET NOT NULL;
ALTER TABLE "ctistatus" ALTER "name" SET NOT NULL;
ALTER TABLE "directories" ALTER "name" SET NOT NULL;
ALTER TABLE "monitoring"
	ALTER "alert_emails" DROP DEFAULT,
	ALTER "dahdi_monitor_ports" DROP DEFAULT;

COMMIT;
