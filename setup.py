# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='slack-logger',
    version='0.1',
    author='Mathias Ose',
    author_email='mathias.ose@gmail.com',

    packages=['slack_logger'],
    install_requires=[
        "slacker==0.4.0"
    ]
)