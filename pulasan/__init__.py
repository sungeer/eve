from quart import Quart

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
    from werkzeug.exceptions import HTTPException

    from pulasan.utils.log_util import logger
    from pulasan.utils.tools import abort
    from pulasan.utils import constants

    @app.errorhandler(HTTPException)
    async def http_exception_handler(exc):
        http_code = exc.code
        message = constants.http_map.get(http_code, exc.description)
        error_code = constants.error_map.get(http_code, http_code)
        return abort(error_code, message)

    @app.errorhandler(500)
    async def internal_server_error(exc):
        return abort(70700, 'An internal server error occurred.')


app = create_app()
