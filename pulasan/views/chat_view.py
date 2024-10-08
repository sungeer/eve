from pulasan.utils.tools import jsonify
from pulasan.utils.log_util import logger


async def index():
    try:
        1 / 0
    except ZeroDivisionError:
        logger.opt(exception=True).error('abc')
    return jsonify()
