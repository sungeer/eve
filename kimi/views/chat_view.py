from quart import Blueprint, current_app

from kimi.utils.resp_util import jsonify

route = Blueprint('chat', __name__)


@route.post('/')
async def index():
    try:
        1 / 0
    except ZeroDivisionError:
        current_app.logger.error('zero division error')
    return jsonify()
