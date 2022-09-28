#!/usr/bin/env python

import setuptools
from distutils.core import setup
import os

GIT_REF = os.environ.get('PIGROMETER_VERSION')
GIT_COMMIT = os.environ.get('PIGROMETER_VERSION')
print(GIT_REF)
print(GIT_COMMIT)

setup(
    name='pigrometer',
    version='no_version',
    description='A webapp for monitoring temperature and humidity with a raspberry pi',
    author='Brian Moody',
    url='https://github.com/BrianKmdy/TempMonitor',
    packages=['pigrometer'],
    setup_requires=['wheel']
)