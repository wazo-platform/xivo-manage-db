#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2014-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from setuptools import setup, find_packages


setup(
    name='xivo-db',
    version='0.1',
    description='Wazo DB LIB',
    author='Wazo Authors',
    author_email='dev.wazo@gmail.com',
    url='http://wazo.community',
    license='GPLv3',
    packages=find_packages('.'),
    scripts=['bin/pg-drop-db',
             'bin/pg-populate-db',
             'bin/xivo-check-db',
             'bin/xivo-init-db',
             'bin/xivo-update-db'],
)
