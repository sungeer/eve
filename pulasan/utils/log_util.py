import logging

from pulasan.configs import settings

app_name = settings.app_name

logger = logging.getLogger(app_name)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
