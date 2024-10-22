from quart import Blueprint

from pulasan.utils.tools import jsonify
from pulasan.utils.log_util import logger

route = Blueprint('chat', __name__)


@route.post('/')
async def index():
    try:
        1 / 0
    except ZeroDivisionError:
        logger.opt(exception=True).error('abc')
    return jsonify()
