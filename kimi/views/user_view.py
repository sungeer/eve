from quart import request, Blueprint

from kimi.models.user_model import UserModel
from kimi.utils.resp_util import jsonify, abort
from kimi.utils import jwt_util

route = Blueprint('user', __name__)


@route.post('/get-access-token')
async def get_access_token():
    body = await request.json
    phone_number = body['phone_number']
    password = body['password']

    db_user = await UserModel().get_user_by_phone(phone_number)
    if not db_user:
        return abort(404, 'User not found')

    db_password = db_user['password_hash']
    is_pwd = jwt_util.validate_password(password, db_password)
    if not is_pwd:
        return abort(403, 'Incorrect password')

    access_token = jwt_util.generate_token({'id': db_user['id']})
    jwt_token = {'access_token': access_token, 'token_type': 'bearer'}
    return jsonify(jwt_token)
