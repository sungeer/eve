from quart import Blueprint

from pulasan.views import user_view

user_url = Blueprint('user', __name__)

user_url.add_url_rule('/get-access-token', 'get_access_token', user_view.get_access_token, methods=['POST'])
