from quart import Blueprint

from pulasan.views import admin_view

admin_url = Blueprint('admin', __name__)

admin_url.add_url_rule('/get-logs', 'get_logs', admin_view.get_logs)
