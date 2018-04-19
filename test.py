import logging
import os
from platform import python_version

from slacker_log_handler import SlackerLogHandler, NoStacktraceFormatter

SLACK_API_TOKEN = os.getenv('SLACK_API_TOKEN')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL')

slack_handler = SlackerLogHandler(SLACK_API_TOKEN, SLACK_CHANNEL, stack_trace=True, ping_users=["@ose", "slackbot"], ping_level=logging.ERROR)

logger = logging.getLogger('debug_application')
logger.addHandler(slack_handler)
logger.setLevel(logging.DEBUG)

formatter = NoStacktraceFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
slack_handler.setFormatter(formatter)

logger.info('Python version is {}'.format(python_version()))

logger.debug('Test DEBUG')
logger.info('Test INFO')
logger.warning('Test WARNING')
logger.error('Test ERROR')
logger.fatal('Test FATAL')
logger.critical('Test CRITICAL')

try:
    raise Exception('Test exception')
except Exception as e:
    logger.exception(e)
