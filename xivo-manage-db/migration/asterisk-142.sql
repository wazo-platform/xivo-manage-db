/*
 * Copyright (C) 2013  Avencall
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

UPDATE "features" SET "var_val" = '5'
    WHERE "features"."var_name" = 'transferdigittimeout'
    AND "features"."var_val" = '3';

UPDATE "features" SET "var_val" = '1500'
    WHERE "features"."var_name" = 'featuredigittimeout'
    AND "features"."var_val" = '500';

COMMIT;
