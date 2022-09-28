#!/usr/bin/env python

import setuptools
from distutils.core import setup
import os

__version__ = 'no_version'

GIT_REF = os.environ.get('GIT_REF')
GIT_COMMIT = os.environ.get('GIT_COMMIT')

if GIT_REF is not None:
    split_ref = GIT_REF.split('/')
    if split_ref[1] == 'tags':
        __version__ = split_ref[-1].split('v')[-1]
    elif GIT_COMMIT is not None:
        __version__ = f'{split_ref[-1]}-{GIT_COMMIT[:7]}'

setup(
    name='pigrometer',
    version=__version__,
    description='A webapp for monitoring temperature and humidity with a raspberry pi',
    author='Brian Moody',
    url='https://github.com/BrianKmdy/TempMonitor',
    packages=['pigrometer'],
    setup_requires=['wheel']
)