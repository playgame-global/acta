#!/usr/bin/env python

from setuptools import setup

setup(
    name='Acta',
    version='0.1.0',
    description='Event based protocol for HTTP APIs',
    long_description="REST is great until it's not, especially in abstracting modern user behaviors. This is where Acta comes in.",
    author='Batista Harahap',
    author_email='batista@bango29.com',
    url='https://github.com/coralhq/acta',
    license='MIT',
    packages=['acta'],
    install_requires=['voluptuous'],
    zip_safe=False)
