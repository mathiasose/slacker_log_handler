import json
import traceback
from logging import Handler, CRITICAL, ERROR, WARNING, INFO, FATAL, DEBUG, NOTSET

import six
import slacker

ERROR_COLOR = 'danger'  # color name is built in to Slack API
WARNING_COLOR = 'warning'  # color name is built in to Slack API
INFO_COLOR = '#439FE0'

COLORS = {
    CRITICAL: ERROR_COLOR,
    FATAL: ERROR_COLOR,
    ERROR: ERROR_COLOR,
    WARNING: WARNING_COLOR,
    INFO: INFO_COLOR,
    DEBUG: INFO_COLOR,
    NOTSET: INFO_COLOR,
}

DEFAULT_EMOJI = ':heavy_exclamation_mark:'


class SlackerLogHandler(Handler):
    def __init__(self, api_key, channel, stack_trace=False, username='Python logger', icon_url=None, icon_emoji=None,
                 fail_silent=False):
        Handler.__init__(self)
        self.slacker = slacker.Slacker(api_key)
        self.channel = channel
        self.stack_trace = stack_trace
        self.username = username
        self.icon_url = icon_url
        self.icon_emoji = icon_emoji if (icon_emoji or icon_url) else DEFAULT_EMOJI
        self.fail_silent = fail_silent

        if not self.channel.startswith('#'):
            self.channel = '#' + self.channel

    def build_msg(self, record):
        return six.text_type(self.format(record))

    def build_trace(self, record, fallback):
        trace = {
            'fallback': fallback,
            'color': COLORS.get(self.level, INFO_COLOR)
        }

        if record.exc_info:
            trace['text'] = '\n'.join(traceback.format_exception(*record.exc_info))

        return trace

    def emit(self, record):
        message = self.build_msg(record)
        trace = self.build_trace(record, fallback=message)
        attachments = json.dumps([trace])

        try:
            self.slacker.chat.post_message(
                text=message,
                channel=self.channel,
                username=self.username,
                icon_url=self.icon_url,
                icon_emoji=self.icon_emoji,
                attachments=attachments,
            )
        except slacker.Error as e:
            if self.fail_silent:
                pass
            else:
                raise e
