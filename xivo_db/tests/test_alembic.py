# -*- coding: UTF-8 -*-

# Copyright (C) 2014 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import unittest
from hamcrest import assert_that, equal_to
from xivo_db import alembic


class TestAlembic(unittest.TestCase):

    def test_parse_alembic_current_output_no_head(self):
        output = '57cca045b7d4\n'

        status = alembic._parse_alembic_current_output(output)

        assert_that(status.revision, equal_to('57cca045b7d4'))
        assert_that(status.is_head, equal_to(False))

    def test_parse_alembic_current_output_head(self):
        output = '57cca045b7d4 (head)\n'

        status = alembic._parse_alembic_current_output(output)

        assert_that(status.revision, equal_to('57cca045b7d4'))
        assert_that(status.is_head, equal_to(True))

    def test_parse_alembic_bad_output(self):
        output = ''

        self.assertRaises(Exception, alembic._parse_alembic_current_output, output)
