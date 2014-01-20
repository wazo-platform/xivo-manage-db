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

UPDATE "musiconhold" SET "var_val" = replace("var_val", 'pf-xivo', 'xivo') WHERE "var_val" LIKE '%pf-xivo%';
UPDATE "dialaction" SET "actionarg1" = replace("actionarg1", 'pf-xivo', 'xivo') WHERE "actionarg1" LIKE '%pf-xivo%';
UPDATE "ctimain" SET "tlscertfile" = replace("tlscertfile", 'pf-xivo', 'xivo') WHERE "tlscertfile" LIKE '%pf-xivo%';
UPDATE "ctimain" SET "tlsprivkeyfile" = replace("tlsprivkeyfile", 'pf-xivo', 'xivo') WHERE "tlsprivkeyfile" LIKE '%pf-xivo%';
UPDATE "ctisheetactions" SET "sheet_qtui" = replace("sheet_qtui", 'pf-xivo', 'xivo') WHERE "sheet_qtui" LIKE '%pf-xivo%';
UPDATE "staticsip" SET "var_val" = replace("var_val", 'pf-xivo', 'xivo') WHERE "var_val" LIKE '%pf-xivo%';
UPDATE "schedule" SET "fallback_actionid" = replace("fallback_actionid", 'pf-xivo', 'xivo') WHERE "fallback_actionid" LIKE '%pf-xivo%';

COMMIT;
