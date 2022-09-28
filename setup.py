#!/usr/bin/env python

import setuptools
from distutils.core import setup
import os

setup(
    name='pigrometer',
    version=os.environ.get('PIGROMETER_VERSION', 'no_version'),
    description='A webapp for monitoring temperature and humidity with a raspberry pi',
    author='Brian Moody',
    url='https://github.com/BrianKmdy/TempMonitor',
    packages=['pigrometer'],
    setup_requires=['wheel']
)