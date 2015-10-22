# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='slack_log_handler',
    version='0.2',
    author='Mathias Ose',
    author_email='mathias.ose@gmail.com',

    packages=['slack_log_handler'],
    install_requires=[
        "slacker==0.7.3"
    ]
)
