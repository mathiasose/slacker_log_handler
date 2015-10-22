import json
import traceback
from logging import Handler, CRITICAL, ERROR, WARNING

from slacker import Slacker

ERROR_COLOR = 'danger'  # color name is built in to Slack API
WARNING_COLOR = 'warning'  # color name is built in to Slack API
INFO_COLOR = '#439FE0'

COLORS = {
    CRITICAL: ERROR_COLOR,
    ERROR: ERROR_COLOR,
    WARNING: WARNING_COLOR
}


class SlackerLogHandler(Handler):
    def __init__(self, api_key, channel, stack_trace=False, username='Python logger', icon_url=None, icon_emoji=None):
        Handler.__init__(self)
        self.slack_chat = Slacker(api_key)
        self.channel = channel
        self.stack_trace = stack_trace
        self.username = username
        self.icon_url = icon_url
        self.icon_emoji = icon_emoji if (icon_emoji or icon_url) else ':heavy_exclamation_mark:'

        if not self.channel.startswith('#'):
            self.channel = '#' + self.channel

    def emit(self, record):
        message = str(record.getMessage())
        attachments = [{
            'fallback': message,
            'color': COLORS.get(self.level, INFO_COLOR),
            'text': '\n'.join(traceback.format_exception(*record.exc_info))
        }]
        self.slack_chat.chat.post_message(
            text=message,
            channel=self.channel,
            username=self.username,
            icon_url=self.icon_url,
            icon_emoji=self.icon_emoji,
            attachments=json.dumps(attachments)
        )
