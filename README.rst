slacker_log_handler
=====================

.. image:: https://img.shields.io/pypi/v/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/dm/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/wheel/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/format/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/pyversions/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

.. image:: https://img.shields.io/pypi/status/slacker_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/slacker_log_handler

Python log handler that posts to a Slack channel. Posts to the Slack API
using https://github.com/os/slacker.

For a different implementation using webhooks instead of Slacker, see
https://github.com/claudetech/python-slack-log or read
http://www.pythian.com/blog/logging-for-slackers/

Created with the intention of using for a Django project, but some
effort has been made to make it generic enough that any Python project
could use it.

Installation
------------

.. code-block:: bash

    pip install slacker-log-handler

Options
-------

api_key (required)
~~~~~~~~~~~~~~~~~~~

Generate a key at https://api.slack.com/

channel (required)
~~~~~~~~~~~~~~~~~~

Set which channel you want to post to, e.g. "#general".

username
~~~~~~~~

The username that will post to Slack. Defaults to "Python logger".

icon_url
~~~~~~~~~

URL to an image to use as the icon for the logger user

icon_emoji
~~~~~~~~~~~

emoji to use as the icon. Overrides icon_url. If neither icon_url nor
icon_emoji is set, :heavy_exclamation_mark: will be used.

Suggested Django configuration
------------------------------

-  Add ``slacker_log_handler`` to ``INSTALLED_APPS``
-  Set ``SLACK_API_KEY``

Sample Django logging configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Logging reference: https://docs.djangoproject.com/en/1.7/topics/logging/

Sends INFO and ERRORS to Slack, as well as errors to admin emails.

.. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'slack-error': {
                'level': 'ERROR',
                'api_key': SLACK_API_KEY,
                'class': 'slacker_log_handler.SlackerLogHandler',
                'channel': '#general'
            },
            'slack-info': {
                'level': 'INFO',
                'api_key': SLACK_API_KEY,
                'class': 'slacker_log_handler.SlackerLogHandler',
                'propagate': True,
            },
        }
    }

License
-------

Apache 2.0

Slacker is also under Apache 2.0.

https://api.slack.com/terms-of-service
