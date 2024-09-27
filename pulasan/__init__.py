from quart import Quart
from werkzeug.http import HTTP_STATUS_CODES

from pulasan.configs import settings


def create_app():
    app = Quart('pulasan')

    register_blueprints(app)
    register_errors(app)
    return app


def register_blueprints(app):
    from pulasan.urls import user_url, chat_url

    app.register_blueprint(chat_url.chat_url)
    app.register_blueprint(user_url.user_url, url_prefix='/user')


def register_errors(app):
    from pulasan.utils.log_util import logger
    from pulasan.utils.tools import abort

    @app.errorhandler(Exception)
    async def global_exception_handler(error):
        http_code = getattr(error, 'code', 500)
        message = HTTP_STATUS_CODES.get(http_code, str(error))
        logger.exception(error)
        return abort(http_code, message)


app = create_app()
