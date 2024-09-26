from quart import Blueprint

from pulasan.views import chat_view

chat_url = Blueprint('chat', __name__)

chat_url.add_url_rule('/', 'index', chat_view.index)
