from quart import request

from pulasan.models.user_model import UserModel
from pulasan.utils.tools import jsonify, abort
from pulasan.utils import jwt_util


async def index():
    return jsonify()
