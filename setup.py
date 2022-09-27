#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(
    name='pigrometer',
    version='0.4',
    description='A webapp for monitoring temperature and humidity with a raspberry pi',
    author='Brian Moody',
    url='https://github.com/BrianKmdy/TempMonitor',
    packages=['pigrometer'],
    setup_requires=['wheel']
)