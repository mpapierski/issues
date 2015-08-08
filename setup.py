#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup


setup(
    name='issues',
    author='Michał Papierski',
    author_email='michal@papierski.net',
    packages=['issues'],
    entry_points={
        'console_scripts': [
            'issues = issues.cli:main',
        ],
    },
    tests_require=[
        'nose==1.3.7',
        'mock==1.3.0'
    ],
    install_requires=[
        'click==4.1',
        'requests==2.7.0'
    ],
)
