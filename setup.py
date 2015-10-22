# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='slacker_log_handler',
    packages=['slacker_log_handler'],
    version='1.0',
    description='Posts log events to Slack via API',
    url='https://github.com/mathiasose/slacker_log_handler',
    download_url='https://github.com/mathiasose/slacker_log_handler/tarball/1.0',
    author='Mathias Ose',
    author_email='mathias.ose@gmail.com',
    keywords=['slack', 'logging'],
    install_requires=[
        "slacker==0.7.3"
    ]
)
