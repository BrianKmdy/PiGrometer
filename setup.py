#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(
    name='Pi Temperature Monitor',
    version='0.1',
    description='A webapp for monitoring temperature and humidity with a raspberry pi',
    author='Brian Moody',
    url='https://github.com/BrianKmdy/TempMonitor',
    packages=['tempmonitor'],
    setup_requires=['wheel']
)