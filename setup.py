#!/usr/bin/env python3
# Copyright 2014-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages


setup(
    name='xivo-db',
    version='0.1',
    description='Wazo DB LIB',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    license='GPLv3',
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'xivo-check-db=xivo_db.check_db:main',
            'xivo-init-db=xivo_db.init_db:main',
            'xivo-update-db=xivo_db.update_db:main',
        ],
    },
    scripts=[
        'bin/pg-drop-db',
        'bin/pg-populate-db',
    ],
)
