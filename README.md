slack_log_handler
===================

Python log handler that posts to a Slack channel.
Posts to the Slack API using https://github.com/os/slacker.

Created with the intention of using for a Django project,
but some effort has been made to make it generic enough that any Python project could use it.

For a simpler implementation using webhooks instead of slacker,
see http://www.pythian.com/blog/logging-for-slackers/

## Options
### api_key (required)
Generate a key at https://api.slack.com/

### channel (required)
Set which channel you want to post to, e.g. "#general".

### username
The username that will post to Slack. Defaults to "Python logger".

### icon_url
URL to an image to use as the icon for the logger user

### icon_emoji 	
emoji to use as the icon. Overrides icon_url.
If neither icon_url nor icon_emoji is set,
:heavy_exclamation_mark: will be used.


## Suggested Django configuration

* Add 'slack_logger' to INSTALLED_APPS
* Set SLACK_API_KEY


### Sample Django logging configuration
Logging reference: https://docs.djangoproject.com/en/1.7/topics/logging/

Sends INFO and ERRORS to Slack, as well as errors to admin emails.

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
                'level':'ERROR',
                'api_key': SLACK_API_KEY,
                'class':'slack_log_handler.SlackLogHandler',
                'channel':'#general'
            },
            'slack-info': {
                'level':'INFO',
                'api_key': SLACK_API_KEY,
                'class':'slack_log_handler.SlackLogHandler',
                'propagate': True,
            },
        }
    }

## License
Apache 2.0

Slacker is also under Apache 2.0.

https://api.slack.com/terms-of-service
