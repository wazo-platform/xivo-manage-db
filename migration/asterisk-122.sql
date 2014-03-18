/*
 * Copyright (C) 2013-2014  Avencall
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

UPDATE "ctidirectoryfields"
    SET "value" = 'extenumbers.exten'
    WHERE "value" = 'linefeatures.number';

UPDATE "ctidirectoryfields"
    SET "value" = 'extenumbers.context'
    WHERE "value" = 'linefeatures.context';

UPDATE "ctidirectories"
    SET "match_direct" = replace("match_direct", '"linefeatures.number"', '"extenumbers.exten"')
    WHERE "match_direct" LIKE '%"linefeatures.number"%';

UPDATE "ctidirectories"
    SET "match_direct" = replace("match_direct", '"linefeatures.context"', '"extenumbers.context"')
    WHERE "match_direct" LIKE '%"linefeatures.context"%';

COMMIT;
